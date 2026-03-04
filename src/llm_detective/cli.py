import asyncio
import sys
import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from openai import AuthenticationError, APIError, APITimeoutError
from llm_detective.fingerprints import get_riddles
from llm_detective.examiner import run_examination
from llm_detective.analyzer import analyze_responses

app = typer.Typer()
console = Console()

@app.command()
def check(
    key: str = typer.Option(..., "--key", help="API Key"),
    url: str = typer.Option("https://api.openai.com/v1", "--url", help="Base URL"),
    model: str = typer.Option("gpt-4", "--model", help="Model name"),
    timeout: int = typer.Option(30, "--timeout", help="Timeout in seconds")
):
    """Check if an LLM API is genuine"""
    console.print("🔍 LLM Detective - Analyzing API...\n", style="bold cyan")

    riddles = get_riddles()

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task(description="Testing with fingerprint questions...", total=None)
            responses = asyncio.run(run_examination(key, url, model, riddles, timeout))

        result = analyze_responses(responses, riddles)

        console.print()
        if result.verdict == "VERIFIED":
            console.print(f"✅ VERIFIED: Likely {model}", style="bold green")
            console.print(f"   Confidence: {result.confidence:.0f}%")
            console.print(f"   {result.details}")
        elif result.verdict == "WARNING":
            console.print(f"⚠️  WARNING: Suspicious behavior detected", style="bold yellow")
            console.print(f"   Confidence: {result.confidence:.0f}%")
            console.print(f"   {result.details}")
        else:
            console.print(f"❌ FRAUD DETECTED: Not {model}", style="bold red")
            console.print(f"   Confidence: {result.confidence:.0f}%")
            console.print(f"   {result.details}")

    except APITimeoutError:
        console.print("❌ Timeout: API took too long to respond", style="bold red")
        sys.exit(1)
    except AuthenticationError:
        console.print("❌ Authentication failed: Invalid API key", style="bold red")
        sys.exit(1)
    except APIError as e:
        console.print(f"❌ API error: {e.message}", style="bold red")
        sys.exit(1)
    except Exception as e:
        console.print(f"❌ Network error: {str(e)}", style="bold red")
        sys.exit(1)

if __name__ == "__main__":
    app()

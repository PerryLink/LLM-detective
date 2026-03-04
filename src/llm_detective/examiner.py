import asyncio
from typing import List
from openai import AsyncOpenAI
from llm_detective.models import Riddle, Response

async def run_examination(
    api_key: str,
    base_url: str,
    model: str,
    riddles: List[Riddle],
    timeout: int = 30
) -> List[Response]:
    client = AsyncOpenAI(api_key=api_key, base_url=base_url, timeout=timeout)

    async def ask_riddle(riddle: Riddle) -> Response:
        response = await client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": riddle.prompt}]
        )
        return Response(
            riddle_id=riddle.id,
            content=response.choices[0].message.content,
            model=model
        )

    responses = await asyncio.gather(*[ask_riddle(r) for r in riddles])
    return list(responses)

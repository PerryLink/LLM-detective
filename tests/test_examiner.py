import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from llm_detective.examiner import run_examination
from llm_detective.models import Riddle

@pytest.fixture
def sample_riddles():
    return [
        Riddle("r1", "prompt1", 1.0, [], [], []),
        Riddle("r2", "prompt2", 1.0, [], [], []),
    ]

@pytest.mark.asyncio
async def test_run_examination_success(sample_riddles):
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Test response"

    with patch("llm_detective.examiner.AsyncOpenAI") as mock_client:
        mock_instance = AsyncMock()
        mock_instance.chat.completions.create = AsyncMock(return_value=mock_response)
        mock_client.return_value = mock_instance

        responses = await run_examination(
            api_key="test-key",
            base_url="https://api.openai.com/v1",
            model="gpt-4",
            riddles=sample_riddles,
            timeout=30
        )

        assert len(responses) == 2
        assert responses[0].content == "Test response"

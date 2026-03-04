import pytest
from llm_detective.analyzer import analyze_responses
from llm_detective.models import Response, Riddle

@pytest.fixture
def sample_riddles():
    return [
        Riddle("r1", "prompt1", 1.0, [r'"name"'], [r'name:'], [r'Name:']),
        Riddle("r2", "prompt2", 1.0, [r'\b3\b'], [r'\b2\b'], [r'\b2\b']),
    ]

def test_gpt4_detection(sample_riddles):
    responses = [
        Response("r1", '{"name": "John"}', "gpt-4"),
        Response("r2", "There are 3 killers", "gpt-4"),
    ]
    result = analyze_responses(responses, sample_riddles)
    assert result.verdict == "VERIFIED"
    assert result.confidence > 80

def test_fake_detection(sample_riddles):
    responses = [
        Response("r1", "{name: John}", "gpt-3.5"),
        Response("r2", "2", "gpt-3.5"),
    ]
    result = analyze_responses(responses, sample_riddles)
    assert result.verdict == "FRAUD"
    assert result.confidence < 40

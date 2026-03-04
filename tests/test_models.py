# tests/test_models.py
from llm_detective.models import Riddle, Response, AnalysisResult

def test_riddle_creation():
    riddle = Riddle(
        id="test1",
        prompt="Test prompt",
        weight=1.0,
        gpt4_patterns=["pattern1"],
        gpt35_patterns=["pattern2"],
        llama_patterns=["pattern3"]
    )
    assert riddle.id == "test1"
    assert riddle.weight == 1.0

def test_response_creation():
    response = Response(
        riddle_id="test1",
        content="Test content",
        model="gpt-4"
    )
    assert response.riddle_id == "test1"

def test_analysis_result_creation():
    result = AnalysisResult(
        verdict="VERIFIED",
        confidence=95.0,
        details="Test details",
        matched_model="gpt-4"
    )
    assert result.verdict == "VERIFIED"
    assert result.confidence == 95.0

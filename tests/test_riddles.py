from llm_detective.fingerprints.riddles import get_riddles

def test_get_riddles_returns_list():
    riddles = get_riddles()
    assert isinstance(riddles, list)
    assert len(riddles) == 3

def test_riddles_have_required_fields():
    riddles = get_riddles()
    for riddle in riddles:
        assert riddle.id
        assert riddle.prompt
        assert riddle.weight > 0
        assert len(riddle.gpt4_patterns) > 0

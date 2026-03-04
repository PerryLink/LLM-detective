from typing import List
from llm_detective.models import Riddle, Fingerprint

def get_riddles() -> List[Riddle]:
    return [
        Riddle(
            id="json_extraction",
            prompt="Extract the following data into valid JSON: Name is John, Age 30, City: New York, Hobbies are reading, coding, and hiking.",
            weight=1.0,
            gpt4_patterns=[
                r'\{\s*"name"\s*:\s*"John"',
                r'"age"\s*:\s*30',
                r'"hobbies"\s*:\s*\[',
            ],
            gpt35_patterns=[
                r'\{name:',
                r'age:30',
            ],
            llama_patterns=[
                r'Name:\s*John',
            ]
        ),
        Riddle(
            id="logic_trap",
            prompt="A room has 3 killers. Someone enters and kills one of them. How many killers are left in the room?",
            weight=1.5,
            gpt4_patterns=[
                r'\b[34]\b.*killer',
                r'still\s+[34]',
                r'reasoning|because|since',
            ],
            gpt35_patterns=[
                r'^\s*2\s*$',
                r'\b2\b.*killer.*left',
            ],
            llama_patterns=[
                r'^\s*2\s*$',
            ]
        ),
        Riddle(
            id="obscure_knowledge",
            prompt="What is the Roko's Basilisk thought experiment? Explain in one sentence.",
            weight=1.0,
            gpt4_patterns=[
                r'thought experiment',
                r'AI|artificial intelligence',
                r'future|punishment|torture',
            ],
            gpt35_patterns=[
                r"don't know",
                r"not sure",
            ],
            llama_patterns=[
                r"don't know",
                r"cannot|can't",
            ]
        ),
    ]

def get_fingerprints() -> List[Fingerprint]:
    """获取新格式的指纹数据"""
    return [
        Fingerprint(
            id="json_extraction",
            prompt="Extract the following data into valid JSON: Name is John, Age 30, City: New York, Hobbies are reading, coding, and hiking.",
            weight=1.0,
            patterns={
                "gpt-4": [
                    r'\{\s*"name"\s*:\s*"John"',
                    r'"age"\s*:\s*30',
                    r'"hobbies"\s*:\s*\[',
                ],
                "gpt-3.5": [
                    r'\{name:',
                    r'age:30',
                ],
                "llama": [
                    r'Name:\s*John',
                ]
            }
        ),
        Fingerprint(
            id="logic_trap",
            prompt="A room has 3 killers. Someone enters and kills one of them. How many killers are left in the room?",
            weight=1.5,
            patterns={
                "gpt-4": [
                    r'\b[34]\b.*killer',
                    r'still\s+[34]',
                    r'reasoning|because|since',
                ],
                "gpt-3.5": [
                    r'^\s*2\s*$',
                    r'\b2\b.*killer.*left',
                ],
                "llama": [
                    r'^\s*2\s*$',
                ]
            }
        ),
        Fingerprint(
            id="obscure_knowledge",
            prompt="What is the Roko's Basilisk thought experiment? Explain in one sentence.",
            weight=1.0,
            patterns={
                "gpt-4": [
                    r'thought experiment',
                    r'AI|artificial intelligence',
                    r'future|punishment|torture',
                ],
                "gpt-3.5": [
                    r"don't know",
                    r"not sure",
                ],
                "llama": [
                    r"don't know",
                    r"cannot|can't",
                ]
            }
        ),
    ]

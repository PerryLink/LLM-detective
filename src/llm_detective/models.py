from dataclasses import dataclass
from typing import List

@dataclass
class Riddle:
    id: str
    prompt: str
    weight: float
    gpt4_patterns: List[str]
    gpt35_patterns: List[str]
    llama_patterns: List[str]

@dataclass
class Fingerprint:
    """通用指纹模型"""
    id: str
    prompt: str
    weight: float
    patterns: dict[str, List[str]]  # {"gpt-4": [...], "gpt-3.5": [...], "llama": [...]}

@dataclass
class Response:
    riddle_id: str
    content: str
    model: str

@dataclass
class AnalysisResult:
    verdict: str  # "VERIFIED" | "WARNING" | "FRAUD"
    confidence: float  # 0-100
    details: str
    matched_model: str  # "gpt-4" | "gpt-3.5" | "llama-2" | "unknown"

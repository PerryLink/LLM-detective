import re
from typing import List
from .base import ModelDetector, DetectionResult
from .registry import DetectorRegistry

class GPT4Detector:
    @property
    def model_name(self) -> str:
        return "gpt-4"

    def detect(self, response: str, patterns: List[str]) -> DetectionResult:
        matched = []
        for pattern in patterns:
            if re.search(pattern, response, re.IGNORECASE):
                matched.append(pattern)

        score = len(matched) / len(patterns) if patterns else 0
        return DetectionResult(
            model_name=self.model_name,
            score=score,
            matched_patterns=matched
        )

DetectorRegistry.register(GPT4Detector())

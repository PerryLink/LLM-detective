from typing import Protocol, List
from llm_detective.models import AnalysisResult
from llm_detective.detectors.base import DetectionResult

class AnalysisStrategy(Protocol):
    """分析策略协议"""

    def analyze(
        self,
        detection_results: List[DetectionResult],
        config: "AnalysisConfig"
    ) -> AnalysisResult:
        """分析检测结果并返回最终判决"""
        ...

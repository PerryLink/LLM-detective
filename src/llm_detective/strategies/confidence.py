from typing import List
from llm_detective.models import AnalysisResult
from llm_detective.detectors.base import DetectionResult
from llm_detective.config import AnalysisConfig

class ConfidenceStrategy:
    """置信度分析策略"""

    def analyze(
        self,
        detection_results: List[DetectionResult],
        config: AnalysisConfig
    ) -> AnalysisResult:
        if not detection_results:
            return AnalysisResult(
                verdict="FRAUD",
                confidence=0.0,
                details="No detection results",
                matched_model="unknown"
            )

        # 找到得分最高的模型
        best_result = max(detection_results, key=lambda r: r.score)
        confidence = best_result.score * 100

        if confidence >= config.verified_threshold * 100:
            return AnalysisResult(
                verdict="VERIFIED",
                confidence=confidence,
                details=f"All responses match {best_result.model_name} patterns",
                matched_model=best_result.model_name
            )
        elif confidence >= config.warning_threshold * 100:
            return AnalysisResult(
                verdict="WARNING",
                confidence=confidence,
                details="Some responses suspicious",
                matched_model="unknown"
            )
        else:
            return AnalysisResult(
                verdict="FRAUD",
                confidence=confidence,
                details=f"Does not match {best_result.model_name} patterns",
                matched_model=best_result.model_name
            )

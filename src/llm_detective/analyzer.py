from typing import List
from llm_detective.models import Response, Riddle, AnalysisResult, Fingerprint
from llm_detective.detectors.registry import DetectorRegistry
from llm_detective.detectors.base import DetectionResult
from llm_detective.config import AnalysisConfig
from llm_detective.strategies.confidence import ConfidenceStrategy

# 导入检测器以触发注册
import llm_detective.detectors.gpt4
import llm_detective.detectors.gpt35
import llm_detective.detectors.llama

def analyze_responses(responses: List[Response], riddles: List[Riddle]) -> AnalysisResult:
    """旧版本分析函数,保持向后兼容"""
    # 转换为新格式
    fingerprints = []
    for riddle in riddles:
        fingerprint = Fingerprint(
            id=riddle.id,
            prompt=riddle.prompt,
            weight=riddle.weight,
            patterns={
                "gpt-4": riddle.gpt4_patterns,
                "gpt-3.5": riddle.gpt35_patterns,
                "llama": riddle.llama_patterns
            }
        )
        fingerprints.append(fingerprint)

    # 使用配置指定只检测 GPT-4,保持旧版本行为
    config = AnalysisConfig(enabled_detectors=["gpt-4"])
    return analyze_with_fingerprints(responses, fingerprints, config)

def analyze_with_fingerprints(
    responses: List[Response],
    fingerprints: List[Fingerprint],
    config: AnalysisConfig | None = None
) -> AnalysisResult:
    """使用新架构分析响应"""
    if config is None:
        config = AnalysisConfig()

    # 获取检测器
    if config.enabled_detectors:
        detectors = [DetectorRegistry.get(name) for name in config.enabled_detectors]
        detectors = [d for d in detectors if d is not None]
    else:
        detectors = DetectorRegistry.get_all()

    if not detectors:
        return AnalysisResult(
            verdict="FRAUD",
            confidence=0.0,
            details="No detectors available",
            matched_model="unknown"
        )

    # 为每个检测器计算总分
    fingerprint_map = {f.id: f for f in fingerprints}
    detector_scores = {d.model_name: {"score": 0.0, "total": 0.0} for d in detectors}

    for response in responses:
        fingerprint = fingerprint_map.get(response.riddle_id)
        if not fingerprint:
            continue

        for detector in detectors:
            patterns = fingerprint.patterns.get(detector.model_name, [])
            if patterns:
                result = detector.detect(response.content, patterns)
                detector_scores[detector.model_name]["score"] += result.score * fingerprint.weight
                detector_scores[detector.model_name]["total"] += fingerprint.weight

    # 计算每个检测器的最终得分
    detection_results = []
    for detector in detectors:
        scores = detector_scores[detector.model_name]
        final_score = scores["score"] / scores["total"] if scores["total"] > 0 else 0
        detection_results.append(
            DetectionResult(
                model_name=detector.model_name,
                score=final_score,
                matched_patterns=[]
            )
        )

    # 使用策略分析结果
    strategy = ConfidenceStrategy()
    return strategy.analyze(detection_results, config)

from typing import List
from .base import ModelDetector

class DetectorRegistry:
    """检测器注册表"""
    _detectors: dict[str, ModelDetector] = {}

    @classmethod
    def register(cls, detector: ModelDetector):
        """注册检测器"""
        cls._detectors[detector.model_name] = detector

    @classmethod
    def get_all(cls) -> List[ModelDetector]:
        """获取所有检测器"""
        return list(cls._detectors.values())

    @classmethod
    def get(cls, model_name: str) -> ModelDetector | None:
        """获取指定检测器"""
        return cls._detectors.get(model_name)

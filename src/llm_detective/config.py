from dataclasses import dataclass
from typing import List

@dataclass
class AnalysisConfig:
    """分析配置"""
    verified_threshold: float = 0.8
    warning_threshold: float = 0.4
    enabled_detectors: List[str] | None = None  # None = all

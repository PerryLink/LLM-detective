from typing import Protocol, List
from dataclasses import dataclass

@dataclass
class DetectionResult:
    """检测结果"""
    model_name: str
    score: float
    matched_patterns: List[str]

class ModelDetector(Protocol):
    """模型检测器协议"""

    @property
    def model_name(self) -> str:
        """返回检测的模型名称"""
        ...

    def detect(self, response: str, patterns: List[str]) -> DetectionResult:
        """检测响应是否匹配模型特征"""
        ...

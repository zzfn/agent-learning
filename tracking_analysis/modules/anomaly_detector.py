"""
异常检测模块
检测埋点数据中的异常情况
"""

import dspy


class AnomalyDetection(dspy.Signature):
    """检测埋点数据异常"""
    event_data = dspy.InputField(desc="埋点事件数据统计信息")
    historical_baseline = dspy.InputField(desc="历史基准数据")
    anomalies = dspy.OutputField(desc="发现的异常列表")
    severity = dspy.OutputField(desc="严重程度（紧急/警告/提示）")
    suggested_actions = dspy.OutputField(desc="建议的处理措施")


class AnomalyAnalyzer(dspy.Module):
    """异常分析器"""

    def __init__(self):
        super().__init__()
        self.detector = dspy.ChainOfThought(AnomalyDetection)

    def forward(self, event_data, historical_baseline=""):
        """
        检测异常
        event_data: 当前事件数据统计
        historical_baseline: 历史基准数据（可选）
        """
        if not historical_baseline:
            historical_baseline = "无历史基准数据"

        result = self.detector(
            event_data=event_data,
            historical_baseline=historical_baseline
        )

        return dspy.Prediction(
            anomalies=result.anomalies,
            severity=result.severity,
            suggested_actions=result.suggested_actions,
            reasoning=result.reasoning
        )


class DataQualityChecker(dspy.Signature):
    """检查埋点数据质量"""
    events = dspy.InputField(desc="埋点事件列表")
    quality_issues = dspy.OutputField(desc="数据质量问题")
    missing_properties = dspy.OutputField(desc="缺失的关键属性")
    recommendations = dspy.OutputField(desc="改进建议")


class QualityAnalyzer(dspy.Module):
    """数据质量分析器"""

    def __init__(self):
        super().__init__()
        self.checker = dspy.ChainOfThought(DataQualityChecker)

    def forward(self, events):
        """检查数据质量"""
        events_str = str(events)

        result = self.checker(events=events_str)

        return dspy.Prediction(
            quality_issues=result.quality_issues,
            missing_properties=result.missing_properties,
            recommendations=result.recommendations,
            reasoning=result.reasoning
        )

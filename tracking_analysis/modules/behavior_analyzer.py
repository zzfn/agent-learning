"""
用户行为分析模块
分析用户行为路径和模式
"""

import dspy


class UserJourneyAnalysis(dspy.Signature):
    """分析用户旅程"""
    event_sequence = dspy.InputField(desc="用户事件序列")
    user_goal = dspy.OutputField(desc="用户可能的目标")
    behavior_pattern = dspy.OutputField(desc="行为模式描述")
    pain_points = dspy.OutputField(desc="发现的痛点")
    optimization_suggestions = dspy.OutputField(desc="优化建议")


class JourneyAnalyzer(dspy.Module):
    """用户旅程分析器"""

    def __init__(self):
        super().__init__()
        self.analyzer = dspy.ChainOfThought(UserJourneyAnalysis)

    def forward(self, event_sequence):
        """
        分析用户旅程
        event_sequence: 按时间排序的事件列表
        """
        # 将事件序列格式化为字符串
        if isinstance(event_sequence, list):
            sequence_str = " -> ".join([
                f"{e.get('event_name', 'unknown')} ({e.get('timestamp', 'N/A')})"
                for e in event_sequence
            ])
        else:
            sequence_str = str(event_sequence)

        result = self.analyzer(event_sequence=sequence_str)

        return dspy.Prediction(
            user_goal=result.user_goal,
            behavior_pattern=result.behavior_pattern,
            pain_points=result.pain_points,
            optimization_suggestions=result.optimization_suggestions,
            reasoning=result.reasoning
        )


class FunnelAnalysis(dspy.Signature):
    """漏斗分析"""
    funnel_steps = dspy.InputField(desc="漏斗各步骤及转化率")
    conversion_insights = dspy.OutputField(desc="转化率洞察")
    bottleneck_steps = dspy.OutputField(desc="瓶颈步骤")
    improvement_strategies = dspy.OutputField(desc="改进策略")


class FunnelAnalyzer(dspy.Module):
    """漏斗分析器"""

    def __init__(self):
        super().__init__()
        self.analyzer = dspy.ChainOfThought(FunnelAnalysis)

    def forward(self, funnel_data):
        """
        分析转化漏斗
        funnel_data: 漏斗数据，包含各步骤和转化率
        """
        # 格式化漏斗数据
        if isinstance(funnel_data, dict):
            funnel_str = "\n".join([
                f"步骤 {i+1}: {step['name']} - "
                f"{step.get('users', 0)} 人 ({step.get('conversion_rate', 0)}%)"
                for i, step in enumerate(funnel_data.get('steps', []))
            ])
        else:
            funnel_str = str(funnel_data)

        result = self.analyzer(funnel_steps=funnel_str)

        return dspy.Prediction(
            conversion_insights=result.conversion_insights,
            bottleneck_steps=result.bottleneck_steps,
            improvement_strategies=result.improvement_strategies,
            reasoning=result.reasoning
        )


class CohortBehavior(dspy.Signature):
    """用户群体行为分析"""
    cohort_data = dspy.InputField(desc="用户群体数据和行为特征")
    key_differences = dspy.OutputField(desc="关键差异点")
    high_value_behaviors = dspy.OutputField(desc="高价值行为")
    engagement_strategies = dspy.OutputField(desc="提升参与度的策略")


class CohortAnalyzer(dspy.Module):
    """用户群体分析器"""

    def __init__(self):
        super().__init__()
        self.analyzer = dspy.ChainOfThought(CohortBehavior)

    def forward(self, cohort_data):
        """分析不同用户群体的行为差异"""
        result = self.analyzer(cohort_data=str(cohort_data))

        return dspy.Prediction(
            key_differences=result.key_differences,
            high_value_behaviors=result.high_value_behaviors,
            engagement_strategies=result.engagement_strategies,
            reasoning=result.reasoning
        )

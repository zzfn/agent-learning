"""
智能洞察生成器
从埋点数据中提取业务洞察
"""

import dspy


class BusinessInsight(dspy.Signature):
    """生成业务洞察"""
    analysis_results = dspy.InputField(desc="各模块的分析结果汇总")
    business_context = dspy.InputField(desc="业务上下文信息")
    key_insights = dspy.OutputField(desc="关键业务洞察（3-5条）")
    action_items = dspy.OutputField(desc="可执行的行动项")
    expected_impact = dspy.OutputField(desc="预期影响和收益")


class InsightGenerator(dspy.Module):
    """洞察生成器"""

    def __init__(self):
        super().__init__()
        self.generator = dspy.ChainOfThought(BusinessInsight)

    def forward(self, analysis_results, business_context=""):
        """
        生成业务洞察
        analysis_results: 各模块分析结果的汇总
        business_context: 业务背景信息
        """
        if not business_context:
            business_context = "电商/APP/Web 应用"

        result = self.generator(
            analysis_results=str(analysis_results),
            business_context=business_context
        )

        return dspy.Prediction(
            key_insights=result.key_insights,
            action_items=result.action_items,
            expected_impact=result.expected_impact,
            reasoning=result.reasoning
        )


class TrackingRecommendation(dspy.Signature):
    """推荐新增埋点"""
    current_events = dspy.InputField(desc="当前已有的埋点事件")
    business_goals = dspy.InputField(desc="业务目标")
    missing_events = dspy.OutputField(desc="建议新增的埋点事件")
    event_priorities = dspy.OutputField(desc="埋点优先级排序")
    implementation_guide = dspy.OutputField(desc="实施指南")


class TrackingAdvisor(dspy.Module):
    """埋点建议系统"""

    def __init__(self):
        super().__init__()
        self.advisor = dspy.ChainOfThought(TrackingRecommendation)

    def forward(self, current_events, business_goals):
        """
        推荐需要新增的埋点
        current_events: 当前已有的埋点列表
        business_goals: 业务目标描述
        """
        result = self.advisor(
            current_events=str(current_events),
            business_goals=business_goals
        )

        return dspy.Prediction(
            missing_events=result.missing_events,
            event_priorities=result.event_priorities,
            implementation_guide=result.implementation_guide,
            reasoning=result.reasoning
        )


class ReportGenerator(dspy.Signature):
    """生成分析报告"""
    all_findings = dspy.InputField(desc="所有分析发现的汇总")
    report_type = dspy.InputField(desc="报告类型（周报/月报/专项）")
    executive_summary = dspy.OutputField(desc="管理层摘要")
    detailed_findings = dspy.OutputField(desc="详细发现")
    next_steps = dspy.OutputField(desc="后续步骤")


class ReportCreator(dspy.Module):
    """报告生成器"""

    def __init__(self):
        super().__init__()
        self.creator = dspy.ChainOfThought(ReportGenerator)

    def forward(self, all_findings, report_type="周报"):
        """生成分析报告"""
        result = self.creator(
            all_findings=str(all_findings),
            report_type=report_type
        )

        return dspy.Prediction(
            executive_summary=result.executive_summary,
            detailed_findings=result.detailed_findings,
            next_steps=result.next_steps,
            reasoning=result.reasoning
        )

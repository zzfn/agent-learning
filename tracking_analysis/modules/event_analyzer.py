"""
埋点事件分析器
解析和理解埋点事件的含义
"""

import dspy


class EventParser(dspy.Signature):
    """解析埋点事件，理解其业务含义"""
    event_name = dspy.InputField(desc="埋点事件名称")
    event_properties = dspy.InputField(desc="事件属性（JSON格式）")
    business_meaning = dspy.OutputField(desc="事件的业务含义")
    user_intent = dspy.OutputField(desc="用户意图")
    importance_level = dspy.OutputField(desc="重要性级别（高/中/低）")


class EventAnalyzer(dspy.Module):
    """埋点事件分析器"""

    def __init__(self):
        super().__init__()
        self.parser = dspy.ChainOfThought(EventParser)

    def forward(self, event_name, event_properties=""):
        """分析单个埋点事件"""
        result = self.parser(
            event_name=event_name,
            event_properties=event_properties
        )

        return dspy.Prediction(
            business_meaning=result.business_meaning,
            user_intent=result.user_intent,
            importance_level=result.importance_level,
            reasoning=result.reasoning
        )


class BatchEventAnalyzer(dspy.Module):
    """批量埋点事件分析器"""

    def __init__(self):
        super().__init__()
        self.analyzer = EventAnalyzer()

    def forward(self, events):
        """
        分析多个埋点事件
        events: list of dict, 每个dict包含 event_name 和 event_properties
        """
        results = []
        for event in events:
            result = self.analyzer(
                event_name=event.get('event_name', ''),
                event_properties=str(event.get('properties', {}))
            )
            results.append({
                'event_name': event.get('event_name'),
                'analysis': result
            })

        return results

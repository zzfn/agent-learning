"""
Demo 1: 埋点事件分析
演示如何解析和理解埋点事件
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dspy
from dotenv import load_dotenv
from modules import EventAnalyzer, BatchEventAnalyzer
from data.sample_events import SAMPLE_EVENTS

# 加载环境变量
load_dotenv()

# 配置 DeepSeek
lm = dspy.LM(
    'deepseek/deepseek-chat',
    api_key=os.getenv('DEEPSEEK_API_KEY')
)
dspy.configure(lm=lm)


def main():
    print("=" * 70)
    print("埋点事件智能分析演示")
    print("=" * 70)

    # 示例 1: 单个事件分析
    print("\n【示例 1】单个埋点事件分析")
    print("-" * 70)

    analyzer = EventAnalyzer()

    event = SAMPLE_EVENTS[1]  # add_to_cart 事件
    print(f"\n分析事件: {event['event_name']}")
    print(f"事件属性: {event['properties']}")

    result = analyzer(
        event_name=event['event_name'],
        event_properties=str(event['properties'])
    )

    print(f"\n业务含义: {result.business_meaning}")
    print(f"用户意图: {result.user_intent}")
    print(f"重要性: {result.importance_level}")
    print(f"\n推理过程:\n{result.reasoning}")

    # 示例 2: 批量事件分析
    print("\n" + "=" * 70)
    print("【示例 2】批量埋点事件分析")
    print("-" * 70)

    batch_analyzer = BatchEventAnalyzer()

    print(f"\n正在分析 {len(SAMPLE_EVENTS)} 个埋点事件...")

    results = batch_analyzer(events=SAMPLE_EVENTS)

    print("\n分析结果汇总:")
    for i, item in enumerate(results, 1):
        print(f"\n{i}. {item['event_name']}")
        analysis = item['analysis']
        print(f"   业务含义: {analysis.business_meaning}")
        print(f"   用户意图: {analysis.user_intent}")
        print(f"   重要性: {analysis.importance_level}")

    # 示例 3: 关键事件识别
    print("\n" + "=" * 70)
    print("【示例 3】识别高价值埋点事件")
    print("-" * 70)

    high_importance_events = [
        item for item in results
        if '高' in item['analysis'].importance_level
    ]

    print(f"\n发现 {len(high_importance_events)} 个高重要性事件:")
    for item in high_importance_events:
        print(f"  • {item['event_name']}: {item['analysis'].business_meaning}")


if __name__ == "__main__":
    main()

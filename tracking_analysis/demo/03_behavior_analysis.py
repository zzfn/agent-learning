"""
Demo 3: 用户行为分析
演示用户旅程、漏斗和群体分析
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dspy
from dotenv import load_dotenv
from modules import JourneyAnalyzer, FunnelAnalyzer, CohortAnalyzer
from data.sample_events import (
    USER_JOURNEY,
    FUNNEL_DATA,
    COHORT_DATA
)

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
    print("用户行为智能分析演示")
    print("=" * 70)

    # 示例 1: 用户旅程分析
    print("\n【示例 1】用户旅程分析")
    print("-" * 70)

    journey_analyzer = JourneyAnalyzer()

    print("\n用户事件序列:")
    for i, event in enumerate(USER_JOURNEY[:8], 1):  # 只显示前8个
        print(f"  {i}. {event['timestamp']} - {event['event_name']}")
    print("  ...")

    result = journey_analyzer(event_sequence=USER_JOURNEY)

    print(f"\n用户目标: {result.user_goal}")
    print(f"\n行为模式: {result.behavior_pattern}")
    print(f"\n痛点: {result.pain_points}")
    print(f"\n优化建议: {result.optimization_suggestions}")
    print(f"\n推理过程:\n{result.reasoning}")

    # 示例 2: 漏斗分析
    print("\n" + "=" * 70)
    print("【示例 2】转化漏斗分析")
    print("-" * 70)

    funnel_analyzer = FunnelAnalyzer()

    print(f"\n漏斗名称: {FUNNEL_DATA['funnel_name']}")
    print("\n漏斗数据:")
    for i, step in enumerate(FUNNEL_DATA['steps'], 1):
        print(f"  步骤 {i}: {step['name']}")
        print(f"    用户数: {step['users']}")
        print(f"    转化率: {step['conversion_rate']}%")

    result = funnel_analyzer(funnel_data=FUNNEL_DATA)

    print(f"\n转化洞察: {result.conversion_insights}")
    print(f"\n瓶颈步骤: {result.bottleneck_steps}")
    print(f"\n改进策略: {result.improvement_strategies}")
    print(f"\n推理过程:\n{result.reasoning}")

    # 示例 3: 用户群体分析
    print("\n" + "=" * 70)
    print("【示例 3】用户群体对比分析")
    print("-" * 70)

    cohort_analyzer = CohortAnalyzer()

    print("\n用户群体数据:")
    for cohort_name, data in COHORT_DATA.items():
        print(f"\n  {cohort_name}:")
        print(f"    数量: {data['count']}")
        print(f"    平均会话时长: {data['avg_session_duration']}")
        print(f"    转化率: {data['conversion_rate']}")

    result = cohort_analyzer(cohort_data=COHORT_DATA)

    print(f"\n关键差异: {result.key_differences}")
    print(f"\n高价值行为: {result.high_value_behaviors}")
    print(f"\n提升策略: {result.engagement_strategies}")
    print(f"\n推理过程:\n{result.reasoning}")


if __name__ == "__main__":
    main()

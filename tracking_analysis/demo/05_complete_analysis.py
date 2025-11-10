"""
Demo 5: 完整的端到端分析
综合演示整个埋点分析系统的能力
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dspy
from dotenv import load_dotenv
from modules import (
    BatchEventAnalyzer,
    AnomalyAnalyzer,
    JourneyAnalyzer,
    FunnelAnalyzer,
    InsightGenerator,
    TrackingAdvisor
)
from data.sample_events import (
    SAMPLE_EVENTS,
    USER_JOURNEY,
    FUNNEL_DATA,
    ANOMALY_DATA,
    HISTORICAL_BASELINE,
    BUSINESS_GOALS
)

# 加载环境变量
load_dotenv()

# 配置 DeepSeek
lm = dspy.LM(
    'deepseek/deepseek-chat',
    api_key=os.getenv('DEEPSEEK_API_KEY')
)
dspy.configure(lm=lm)


def print_section(title):
    """打印章节标题"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main():
    print_section("业务埋点智能分析系统 - 完整演示")

    # 第一步：事件分析
    print_section("第 1 步：批量埋点事件分析")
    batch_analyzer = BatchEventAnalyzer()
    print(f"正在分析 {len(SAMPLE_EVENTS)} 个埋点事件...")
    event_results = batch_analyzer(events=SAMPLE_EVENTS)
    print(f"✓ 完成事件分析")

    # 第二步：异常检测
    print_section("第 2 步：异常检测")
    anomaly_analyzer = AnomalyAnalyzer()
    event_data_str = f"""
    事件: {ANOMALY_DATA['event']}
    今日: {ANOMALY_DATA['today_count']} 次
    昨日: {ANOMALY_DATA['yesterday_count']} 次
    周均: {ANOMALY_DATA['weekly_average']} 次
    变化: {ANOMALY_DATA['change_percentage']}%
    """
    anomaly_result = anomaly_analyzer(
        event_data=event_data_str,
        historical_baseline=HISTORICAL_BASELINE
    )
    print(f"✓ 完成异常检测")
    print(f"  严重程度: {anomaly_result.severity}")

    # 第三步：用户旅程分析
    print_section("第 3 步：用户旅程分析")
    journey_analyzer = JourneyAnalyzer()
    print(f"正在分析用户行为路径（{len(USER_JOURNEY)} 个事件）...")
    journey_result = journey_analyzer(event_sequence=USER_JOURNEY)
    print(f"✓ 完成旅程分析")
    print(f"  用户目标: {journey_result.user_goal}")

    # 第四步：漏斗分析
    print_section("第 4 步：转化漏斗分析")
    funnel_analyzer = FunnelAnalyzer()
    print(f"正在分析 {FUNNEL_DATA['funnel_name']}...")
    funnel_result = funnel_analyzer(funnel_data=FUNNEL_DATA)
    print(f"✓ 完成漏斗分析")
    print(f"  瓶颈: {funnel_result.bottleneck_steps}")

    # 第五步：生成综合洞察
    print_section("第 5 步：生成业务洞察")
    insight_generator = InsightGenerator()

    # 汇总所有分析结果
    all_analysis = f"""
    1. 埋点事件分析:
       共分析 {len(event_results)} 个事件
       高优先级事件: {len([r for r in event_results if '高' in r['analysis'].importance_level])} 个

    2. 异常检测:
       {anomaly_result.anomalies}

    3. 用户旅程:
       用户目标: {journey_result.user_goal}
       痛点: {journey_result.pain_points}

    4. 转化漏斗:
       瓶颈步骤: {funnel_result.bottleneck_steps}
       改进策略: {funnel_result.improvement_strategies}
    """

    insight_result = insight_generator(
        analysis_results=all_analysis,
        business_context="电商移动应用"
    )
    print(f"✓ 完成洞察生成")

    # 第六步：埋点建议
    print_section("第 6 步：智能埋点建议")
    tracking_advisor = TrackingAdvisor()
    current_events = [e['event_name'] for e in SAMPLE_EVENTS]
    tracking_result = tracking_advisor(
        current_events=current_events,
        business_goals=BUSINESS_GOALS
    )
    print(f"✓ 完成埋点建议")

    # 输出最终报告
    print_section("📊 完整分析报告")

    print("\n一、关键业务洞察")
    print(insight_result.key_insights)

    print("\n二、发现的主要问题")
    print(f"• 异常情况: {anomaly_result.anomalies}")
    print(f"• 用户痛点: {journey_result.pain_points}")
    print(f"• 转化瓶颈: {funnel_result.bottleneck_steps}")

    print("\n三、优先行动项")
    print(insight_result.action_items)

    print("\n四、埋点优化建议")
    print(tracking_result.missing_events)

    print("\n五、预期收益")
    print(insight_result.expected_impact)

    print_section("✅ 分析完成")
    print("\n系统已完成全面的埋点数据分析，为业务决策提供了数据支持。")


if __name__ == "__main__":
    main()

"""
Demo 4: 智能洞察与报告
演示业务洞察生成、埋点建议和报告生成
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dspy
from dotenv import load_dotenv
from modules import InsightGenerator, TrackingAdvisor, ReportCreator
from data.sample_events import SAMPLE_EVENTS, BUSINESS_GOALS

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
    print("智能洞察与报告生成演示")
    print("=" * 70)

    # 示例 1: 业务洞察生成
    print("\n【示例 1】业务洞察生成")
    print("-" * 70)

    insight_generator = InsightGenerator()

    # 模拟分析结果汇总
    analysis_summary = """
    1. 用户行为分析:
       - 用户在商品详情页平均停留 2.5 分钟
       - 加购率为 30%，但最终购买率仅 9%
       - 支付环节首次失败率达 40%

    2. 异常检测:
       - 今日结算事件下降 62.5%，显著低于历史基准
       - 可能原因：支付接口异常或页面加载问题

    3. 漏斗分析:
       - 最大流失发生在"加购"到"结算"环节（50%流失）
       - 支付完成率有待提升（60% -> 90%的目标）

    4. 用户群体:
       - 活跃用户转化率（8.5%）远高于新用户（2.5%）
       - 流失用户会话时长仅 1.5 分钟
    """

    business_context = "电商移动应用，主营 3C 数码产品"

    print("\n正在生成业务洞察...")

    result = insight_generator(
        analysis_results=analysis_summary,
        business_context=business_context
    )

    print(f"\n关键洞察:\n{result.key_insights}")
    print(f"\n行动项:\n{result.action_items}")
    print(f"\n预期影响:\n{result.expected_impact}")
    print(f"\n推理过程:\n{result.reasoning}")

    # 示例 2: 埋点建议
    print("\n" + "=" * 70)
    print("【示例 2】智能埋点建议")
    print("-" * 70)

    tracking_advisor = TrackingAdvisor()

    current_events_list = [e['event_name'] for e in SAMPLE_EVENTS]
    print("\n当前已有埋点:")
    for i, event in enumerate(current_events_list, 1):
        print(f"  {i}. {event}")

    print(f"\n业务目标:\n{BUSINESS_GOALS}")

    print("\n正在生成埋点建议...")

    result = tracking_advisor(
        current_events=current_events_list,
        business_goals=BUSINESS_GOALS
    )

    print(f"\n建议新增埋点:\n{result.missing_events}")
    print(f"\n优先级排序:\n{result.event_priorities}")
    print(f"\n实施指南:\n{result.implementation_guide}")
    print(f"\n推理过程:\n{result.reasoning}")

    # 示例 3: 分析报告生成
    print("\n" + "=" * 70)
    print("【示例 3】自动生成分析报告")
    print("-" * 70)

    report_creator = ReportCreator()

    all_findings = f"""
    {analysis_summary}

    关键洞察:
    {result.key_insights}

    建议行动:
    {result.action_items}
    """

    print("\n正在生成周报...")

    result = report_creator(
        all_findings=all_findings,
        report_type="周报"
    )

    print(f"\n管理层摘要:\n{result.executive_summary}")
    print(f"\n详细发现:\n{result.detailed_findings}")
    print(f"\n后续步骤:\n{result.next_steps}")
    print(f"\n推理过程:\n{result.reasoning}")


if __name__ == "__main__":
    main()

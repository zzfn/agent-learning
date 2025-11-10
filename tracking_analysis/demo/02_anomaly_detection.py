"""
Demo 2: 异常检测
演示如何检测埋点数据中的异常情况
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dspy
from dotenv import load_dotenv
from modules import AnomalyAnalyzer, QualityAnalyzer
from data.sample_events import (
    ANOMALY_DATA,
    HISTORICAL_BASELINE,
    SAMPLE_EVENTS
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
    print("埋点数据异常检测演示")
    print("=" * 70)

    # 示例 1: 数据异常检测
    print("\n【示例 1】检测数据异常")
    print("-" * 70)

    analyzer = AnomalyAnalyzer()

    event_data_str = f"""
    事件: {ANOMALY_DATA['event']}
    今日数据: {ANOMALY_DATA['today_count']} 次
    昨日数据: {ANOMALY_DATA['yesterday_count']} 次
    周平均: {ANOMALY_DATA['weekly_average']} 次
    变化幅度: {ANOMALY_DATA['change_percentage']}%
    """

    print(f"\n分析数据:\n{event_data_str}")

    anomaly_result = analyzer(
        event_data=event_data_str,
        historical_baseline=HISTORICAL_BASELINE
    )

    print(f"\n发现的异常:\n{anomaly_result.anomalies}")
    print(f"\n严重程度: {anomaly_result.severity}")
    print(f"\n建议措施:\n{anomaly_result.suggested_actions}")
    print(f"\n推理过程:\n{anomaly_result.reasoning}")

    # 示例 2: 数据质量检查
    print("\n" + "=" * 70)
    print("【示例 2】数据质量检查")
    print("-" * 70)

    quality_analyzer = QualityAnalyzer()

    # 模拟一些有问题的埋点数据
    events_with_issues = SAMPLE_EVENTS + [
        {'event_name': 'page_view', 'properties': {}},  # 缺少关键属性
        {'event_name': 'click', 'properties': {'x': 100, 'y': 200}},  # 属性不完整
    ]

    print(f"\n正在检查 {len(events_with_issues)} 个埋点事件的数据质量...")

    quality_result = quality_analyzer(events=events_with_issues)

    print(f"\n质量问题:\n{quality_result.quality_issues}")
    print(f"\n缺失属性:\n{quality_result.missing_properties}")
    print(f"\n改进建议:\n{quality_result.recommendations}")
    print(f"\n推理过程:\n{quality_result.reasoning}")

    # 示例 3: 综合诊断
    print("\n" + "=" * 70)
    print("【示例 3】综合诊断报告")
    print("-" * 70)

    print("\n系统诊断摘要:")
    print(f"  异常检测: {'⚠️ 发现异常' if '异常' in anomaly_result.anomalies or '下降' in anomaly_result.anomalies else '✓ 正常'}")
    print(f"  数据质量: {'⚠️ 存在问题' if '缺失' in quality_result.quality_issues else '✓ 良好'}")
    print("\n优先处理事项:")

    # 提取第一行建议
    first_action = anomaly_result.suggested_actions.split('\n')[0] if anomaly_result.suggested_actions else '无'
    first_recommendation = quality_result.recommendations.split('\n')[0] if quality_result.recommendations else '无'

    print(f"  1. {first_action}")
    print(f"  2. {first_recommendation}")


if __name__ == "__main__":
    main()

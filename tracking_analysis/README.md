# 业务埋点智能分析系统

基于 DSPy 框架构建的智能埋点数据分析系统，利用大语言模型的推理能力，自动化分析用户行为数据，生成业务洞察和优化建议。

## 系统简介

这是一个企业级的埋点数据分析解决方案，能够：

- 🔍 **自动解析埋点事件** - 理解每个埋点的业务含义和用户意图
- 🚨 **智能异常检测** - 发现数据异常和质量问题
- 👥 **用户行为分析** - 分析用户旅程、转化漏斗和群体差异
- 💡 **生成业务洞察** - 自动提取关键发现和优化建议
- 📊 **自动化报告** - 生成结构化的分析报告
- 🎯 **埋点建议** - 推荐需要新增的埋点事件

## 项目结构

```
tracking_analysis/
├── README.md              # 本文件
├── modules/               # 核心分析模块
│   ├── __init__.py
│   ├── event_analyzer.py        # 埋点事件分析器
│   ├── anomaly_detector.py      # 异常检测模块
│   ├── behavior_analyzer.py     # 用户行为分析
│   └── insight_generator.py     # 洞察生成器
├── data/                  # 示例数据
│   └── sample_events.py         # 示例埋点数据
└── demo/                  # 演示脚本
    ├── 01_event_analysis.py     # 事件分析演示
    ├── 02_anomaly_detection.py  # 异常检测演示
    ├── 03_behavior_analysis.py  # 行为分析演示
    ├── 04_insights_report.py    # 洞察报告演示
    └── 05_complete_analysis.py  # 完整流程演示
```

## 核心功能模块

### 1. 埋点事件分析器 (EventAnalyzer)

**功能**：解析和理解单个或批量埋点事件

```python
from modules import EventAnalyzer

analyzer = EventAnalyzer()
result = analyzer(
    event_name="add_to_cart",
    event_properties="{'product_id': 'SKU123', 'price': 299}"
)

print(result.business_meaning)  # 业务含义
print(result.user_intent)       # 用户意图
print(result.importance_level)  # 重要性级别
```

**输出示例**：
- 业务含义：用户将商品加入购物车，表示购买意向
- 用户意图：准备购买，处于决策阶段
- 重要性级别：高

### 2. 异常检测模块 (AnomalyAnalyzer)

**功能**：检测埋点数据中的异常情况

```python
from modules import AnomalyAnalyzer

analyzer = AnomalyAnalyzer()
result = analyzer(
    event_data="今日: 450次, 昨日: 1200次, 变化: -62.5%",
    historical_baseline="过去7天平均: 1100次"
)

print(result.anomalies)           # 发现的异常
print(result.severity)            # 严重程度
print(result.suggested_actions)   # 建议措施
```

**输出示例**：
- 异常：结算事件大幅下降62.5%，远低于正常范围
- 严重程度：紧急
- 建议措施：立即检查支付接口和页面加载

### 3. 用户行为分析 (BehaviorAnalyzer)

包含三个子模块：

#### 3.1 用户旅程分析 (JourneyAnalyzer)

```python
from modules import JourneyAnalyzer

analyzer = JourneyAnalyzer()
result = analyzer(event_sequence=user_events)

print(result.user_goal)                  # 用户目标
print(result.behavior_pattern)           # 行为模式
print(result.pain_points)                # 痛点
print(result.optimization_suggestions)   # 优化建议
```

#### 3.2 漏斗分析 (FunnelAnalyzer)

```python
from modules import FunnelAnalyzer

analyzer = FunnelAnalyzer()
result = analyzer(funnel_data=funnel_info)

print(result.conversion_insights)      # 转化洞察
print(result.bottleneck_steps)         # 瓶颈步骤
print(result.improvement_strategies)   # 改进策略
```

#### 3.3 用户群体分析 (CohortAnalyzer)

```python
from modules import CohortAnalyzer

analyzer = CohortAnalyzer()
result = analyzer(cohort_data=cohort_info)

print(result.key_differences)         # 关键差异
print(result.high_value_behaviors)    # 高价值行为
print(result.engagement_strategies)   # 参与度策略
```

### 4. 洞察生成器 (InsightGenerator)

**功能**：从分析结果中提取业务洞察

```python
from modules import InsightGenerator

generator = InsightGenerator()
result = generator(
    analysis_results=all_analysis,
    business_context="电商移动应用"
)

print(result.key_insights)       # 关键洞察
print(result.action_items)       # 行动项
print(result.expected_impact)    # 预期影响
```

### 5. 埋点建议系统 (TrackingAdvisor)

**功能**：推荐需要新增的埋点

```python
from modules import TrackingAdvisor

advisor = TrackingAdvisor()
result = advisor(
    current_events=['page_view', 'add_to_cart'],
    business_goals="提升转化率和用户留存"
)

print(result.missing_events)         # 建议新增的埋点
print(result.event_priorities)       # 优先级排序
print(result.implementation_guide)   # 实施指南
```

## 快速开始

### 1. 环境准备

确保已经配置好 DeepSeek API：

```bash
# 在项目根目录的 .env 文件中
DEEPSEEK_API_KEY=your-api-key-here
```

### 2. 运行演示

```bash
# 回到项目根目录
cd /Users/c.chen/dev/dspy-learning

# 运行事件分析演示
uv run python tracking_analysis/demo/01_event_analysis.py

# 运行异常检测演示
uv run python tracking_analysis/demo/02_anomaly_detection.py

# 运行行为分析演示
uv run python tracking_analysis/demo/03_behavior_analysis.py

# 运行洞察报告演示
uv run python tracking_analysis/demo/04_insights_report.py

# 运行完整流程演示
uv run python tracking_analysis/demo/05_complete_analysis.py
```

## 实际应用场景

### 场景1：日常数据监控

每日自动分析埋点数据，及时发现异常情况。

```python
# 定时任务脚本
analyzer = AnomalyAnalyzer()
result = analyzer(event_data=today_stats, historical_baseline=last_week)
if "紧急" in result.severity:
    send_alert(result.anomalies, result.suggested_actions)
```

### 场景2：产品迭代前分析

在产品功能上线前，分析当前用户行为，找出优化点。

```python
journey_analyzer = JourneyAnalyzer()
funnel_analyzer = FunnelAnalyzer()

# 分析用户旅程
journey_result = journey_analyzer(event_sequence=user_paths)

# 分析转化漏斗
funnel_result = funnel_analyzer(funnel_data=conversion_funnel)

# 生成优化建议
print(journey_result.optimization_suggestions)
print(funnel_result.improvement_strategies)
```

### 场景3：周/月报自动生成

自动生成结构化的数据分析报告。

```python
# 收集所有分析结果
all_findings = {
    'events': event_analysis,
    'anomalies': anomaly_detection,
    'behaviors': behavior_analysis,
    'insights': business_insights
}

# 生成报告
report_creator = ReportCreator()
report = report_creator(all_findings=all_findings, report_type="周报")

# 输出或发送报告
save_report(report.executive_summary, report.detailed_findings)
```

### 场景4：新功能埋点规划

在开发新功能前，规划需要添加的埋点。

```python
advisor = TrackingAdvisor()
result = advisor(
    current_events=existing_events,
    business_goals="新增社交分享功能，提升病毒传播系数"
)

# 获取埋点建议
print(result.missing_events)
print(result.event_priorities)
print(result.implementation_guide)
```

## 技术特点

### 1. 基于 DSPy 框架

- 使用 `ChainOfThought` 进行复杂推理
- 通过 `Signature` 定义结构化输入输出
- 模块化设计，易于扩展和维护

### 2. 智能化程度高

- 自动理解业务语义
- 上下文感知的分析
- 可解释的推理过程

### 3. 灵活可扩展

- 易于添加新的分析模块
- 支持自定义业务场景
- 可与现有数据系统集成

### 4. 实用性强

- 真实业务场景设计
- 直接可用的分析结果
- 可操作的优化建议

## 自定义和扩展

### 添加新的分析模块

```python
import dspy

class CustomAnalysis(dspy.Signature):
    """你的自定义分析"""
    input_data = dspy.InputField(desc="输入描述")
    output_result = dspy.OutputField(desc="输出描述")

class CustomAnalyzer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyzer = dspy.ChainOfThought(CustomAnalysis)

    def forward(self, data):
        result = self.analyzer(input_data=data)
        return result
```

### 集成到现有系统

```python
# 从数据库读取埋点数据
events = fetch_events_from_database()

# 使用分析系统
analyzer = BatchEventAnalyzer()
results = analyzer(events=events)

# 存储分析结果
save_analysis_results(results)
```

## 最佳实践

1. **定期运行异常检测** - 设置定时任务，每日自动检测数据异常
2. **结合业务上下文** - 在使用洞察生成器时，提供详细的业务背景
3. **持续优化埋点** - 定期使用埋点建议系统，完善数据采集
4. **建立历史基准** - 积累历史数据，提高异常检测准确性
5. **跨团队协作** - 分析结果分享给产品、运营、开发团队

## 注意事项

- ⚠️ 首次使用需要配置 DeepSeek API 密钥
- ⚠️ LLM 推理需要时间，大批量数据分析建议异步处理
- ⚠️ 输出结果需要人工审核，作为决策参考而非直接依据
- ⚠️ 注意保护用户隐私，避免在提示中包含敏感信息

## 性能优化建议

1. **批量处理** - 使用 `BatchEventAnalyzer` 而非循环调用
2. **缓存结果** - 对相同输入缓存 LLM 输出
3. **异步调用** - 多个独立分析可以并行执行
4. **精简输入** - 只传递必要的数据，减少 token 消耗

## 后续规划

- [ ] 支持实时流式数据分析
- [ ] 集成向量数据库，实现 RAG 增强
- [ ] 添加可视化仪表板
- [ ] 支持多种 LLM 提供商
- [ ] 增加 A/B 测试分析模块
- [ ] 支持自定义评估指标

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

---

**项目作者**: [您的名字]
**基于**: DSPy Framework
**LLM**: DeepSeek Chat

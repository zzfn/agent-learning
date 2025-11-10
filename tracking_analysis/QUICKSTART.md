# 快速开始指南

## 5 分钟上手业务埋点智能分析系统

### 第一步：运行第一个演示

```bash
# 在项目根目录执行
uv run python tracking_analysis/demo/01_event_analysis.py
```

你会看到系统自动分析埋点事件的结果：

```
业务含义: 用户将商品添加到购物车的操作...
用户意图: 用户意图是将感兴趣的商品暂时保存...
重要性: 高
```

### 第二步：了解系统能做什么

运行完整演示，查看所有功能：

```bash
uv run python tracking_analysis/demo/05_complete_analysis.py
```

系统会依次执行：
1. ✓ 批量埋点事件分析
2. ✓ 异常检测
3. ✓ 用户旅程分析
4. ✓ 转化漏斗分析
5. ✓ 生成业务洞察
6. ✓ 智能埋点建议

### 第三步：在自己的项目中使用

#### 分析你的埋点事件

```python
import dspy
from modules import EventAnalyzer

# 配置 DeepSeek
lm = dspy.LM('deepseek/deepseek-chat', api_key='your-key')
dspy.configure(lm=lm)

# 分析事件
analyzer = EventAnalyzer()
result = analyzer(
    event_name="your_event_name",
    event_properties="your event properties"
)

print(result.business_meaning)
print(result.user_intent)
```

#### 检测异常

```python
from modules import AnomalyAnalyzer

analyzer = AnomalyAnalyzer()
result = analyzer(
    event_data="今日: 500次, 昨日: 1000次",
    historical_baseline="周平均: 950次"
)

print(result.severity)  # 严重程度
print(result.suggested_actions)  # 建议措施
```

#### 分析用户旅程

```python
from modules import JourneyAnalyzer

analyzer = JourneyAnalyzer()
result = analyzer(event_sequence=your_user_events)

print(result.user_goal)  # 用户目标
print(result.pain_points)  # 痛点
```

### 第四步：查看更多示例

- `01_event_analysis.py` - 埋点事件分析
- `02_anomaly_detection.py` - 异常检测
- `03_behavior_analysis.py` - 行为分析
- `04_insights_report.py` - 洞察报告
- `05_complete_analysis.py` - 完整流程

### 常见问题

**Q: 系统需要什么数据格式？**

A: 埋点事件格式：
```python
{
    'event_name': '事件名称',
    'properties': {
        '属性1': '值1',
        '属性2': '值2'
    }
}
```

**Q: 可以分析实时数据吗？**

A: 可以！只需将实时采集的埋点数据传入相应的分析模块即可。

**Q: 如何集成到现有系统？**

A: 系统提供了独立的分析模块，可以作为微服务或定时任务集成到现有数据分析流程中。

### 下一步

- 阅读 [完整文档](README.md)
- 了解各个模块的详细用法
- 根据业务需求自定义分析逻辑

---

遇到问题？查看 README.md 或提交 Issue。

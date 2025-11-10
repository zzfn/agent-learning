# DSPy 学习项目

这是一个使用 uv 管理的 DSPy 学习项目，配置使用 DeepSeek API。

## 关于 DSPy

DSPy 是一个用于编程语言模型的框架，它将语言模型作为可编程组件，支持构建、优化和验证复杂的 LM 管道。

## 项目结构

```
dspy-learning/
├── README.md          # 本文件
├── pyproject.toml     # 项目配置和依赖
├── .env.example       # 环境变量配置示例
├── examples/          # 学习示例
│   ├── 01_basic.py    # 基础示例
│   ├── 02_chain_of_thought.py  # 思维链
│   └── 03_rag.py      # RAG 示例
└── .venv/             # 虚拟环境
```

## 快速开始

### 1. 设置 DeepSeek API 密钥

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，添加你的 DeepSeek API 密钥
# DEEPSEEK_API_KEY=your-deepseek-api-key-here
```

获取 API 密钥：访问 [DeepSeek 平台](https://platform.deepseek.com/api_keys)

### 2. 运行示例

```bash
# 基础示例 - 了解 DSPy 核心概念
uv run python examples/01_basic.py

# 思维链示例 - 复杂推理
uv run python examples/02_chain_of_thought.py

# RAG 示例 - 检索增强生成
uv run python examples/03_rag.py
```

## 为什么选择 DeepSeek？

- **性价比高**：API 调用费用相比其他服务商更经济
- **中文友好**：对中文任务有优秀的表现
- **兼容性好**：API 完全兼容 OpenAI 格式，迁移方便
- **性能优秀**：deepseek-chat 在多项基准测试中表现出色

## 学习路线

### 1. 基础概念 (`examples/01_basic.py`)
- 了解 DSPy 的基本结构
- 学习 Signature 定义输入输出
- 使用 Predict 模块进行预测
- 掌握简化的 Signature 语法

### 2. 思维链推理 (`examples/02_chain_of_thought.py`)
- 使用 ChainOfThought 模块
- 理解推理步骤的生成
- 比较 Predict 和 ChainOfThought 的区别
- 处理复杂的多步骤推理任务

### 3. 检索增强生成 (`examples/03_rag.py`)
- 基于上下文的问答
- 构建自定义 RAG 模块
- 多跳推理和信息综合
- 实际应用的最佳实践

## 配置其他 LLM 提供商

如果想使用其他 LLM 提供商，修改示例代码中的配置：

```python
# 使用 DeepSeek（当前配置）
lm = dspy.LM('deepseek/deepseek-chat', api_key=os.getenv('DEEPSEEK_API_KEY'))

# 使用 OpenAI
lm = dspy.LM('openai/gpt-4o-mini', api_key=os.getenv('OPENAI_API_KEY'))

# 使用 Anthropic Claude
lm = dspy.LM('anthropic/claude-3-5-sonnet-20241022', api_key=os.getenv('ANTHROPIC_API_KEY'))
```

## 有用的资源

- [DSPy 官方文档](https://dspy-docs.vercel.app/)
- [DSPy GitHub 仓库](https://github.com/stanfordnlp/dspy)
- [DSPy 示例和教程](https://github.com/stanfordnlp/dspy/tree/main/examples)
- [DeepSeek 平台](https://platform.deepseek.com/)
- [DeepSeek 文档](https://platform.deepseek.com/docs)

## 常用命令

```bash
# 添加新的依赖包
uv add package-name

# 运行 Python 脚本（自动使用虚拟环境）
uv run python script.py

# 手动激活虚拟环境
source .venv/bin/activate

# 查看已安装的包
uv pip list

# 更新所有依赖
uv lock --upgrade
```

## 下一步学习

1. **优化器学习**：探索 DSPy 的 Optimizer（如 BootstrapFewShot）
2. **实战项目**：构建一个完整的 RAG 应用
3. **评估系统**：学习如何评估和优化 LM 管道
4. **集成向量数据库**：使用 ChromaDB 或 Pinecone 进行真实检索

## 问题排查

### API 调用失败
- 确认 `.env` 文件中的 API 密钥正确
- 检查网络连接是否正常
- 验证 DeepSeek 账户余额是否充足

### 依赖问题
```bash
# 重新安装依赖
uv sync

# 清理并重建虚拟环境
rm -rf .venv
uv sync
```

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个学习项目！

# 《人工智能导论》课程作业 02 提交材料

## 任务一：论文导读

### 论文来源
- 论文标题：ChatMusician: An Open-Source LLM with Intrinsic Musical Abilities
- 出处：arXiv (2024年2月)
- 链接：https://arxiv.org/abs/2402.16153

### 导读生成与配图方式
- 使用的大模型：DeepSeek
- 导读内容：由大模型生成，包含研究背景与动机、核心方法、主要结果和个人小结
- 配图方式：手动插入配图说明，包括模型架构、音乐生成示例、性能对比和语料库组成

## 任务二：Chatbot 示例代码

### 采用的 API/平台
- API 类型：OpenAI 兼容接口
- 平台：DeepSeek API
- 基础 URL：https://api.deepseek.com/v1

### 运行方式
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 配置 API Key：
   - 方法一（推荐）：设置环境变量
     - `DEEPSEEK_API_KEY`: 你的 DeepSeek API Key
     - `DEEPSEEK_BASE_URL`: API 基础 URL（默认：https://api.deepseek.com/v1）
   - 方法二：直接修改 `chatbot_deepseek.py` 文件中的 API Key

3. 运行命令：
   ```bash
   python chatbot_deepseek.py
   ```

### 示例输入/输出
- 输入："你好，介绍一下你自己"
- 输出："你好！我是一个基于 DeepSeek 模型的 AI 助手，能够回答你的问题、提供信息和帮助你完成各种任务。我可以协助你学习、工作、娱乐等多个方面，有什么需要帮忙的吗？"

### 注意事项
- 确保你已经获取了有效的 DeepSeek API Key
- 不同的 API 提供商可能有不同的 base_url，需要根据实际情况调整
- 本示例使用 OpenAI 兼容接口，也可以用于调用其他支持该接口的模型

## 提交文件说明
- `导读_ChatMusician.md`：论文导读文档
- `chatbot_deepseek.py`：Chatbot 示例代码
- `requirements.txt`：依赖包配置文件
- `README.md`：提交说明文档
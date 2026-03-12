import os
from openai import OpenAI

# 配置 API 信息
api_key = os.getenv("DEEPSEEK_API_KEY", "your-api-key-here")
base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

# 初始化客户端
client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

# 论文信息
paper_info = """
论文标题：ChatMusician: An Open-Source LLM with Intrinsic Musical Abilities
作者：Ruibin Yuan 等
发表时间：2024年2月
arXiv链接：https://arxiv.org/abs/2402.16153

摘要：
While Large Language Models (LLMs) demonstrate impressive capabilities in text generation, we find that their ability has yet to be generalized to music, humanity's creative language. We introduce ChatMusician, an open-source LLM that integrates intrinsic musical abilities. It is based on continual pre-training and finetuning LLaMA2 on a text-compatible music representation, ABC notation, and the music is treated as a second language. ChatMusician can understand and generate music with a pure text tokenizer without any external multi-modal neural structures or tokenizers. Interestingly, endowing musical abilities does not harm language abilities, even achieving a slightly higher MMLU score. Our model is capable of composing well-structured, full-length music, conditioned on texts, chords, melodies, motifs, musical forms, etc, surpassing GPT-4 baseline. On our meticulously curated college-level music understanding benchmark, MusicTheoryBench, ChatMusician surpasses LLaMA2 and GPT-3.5 on zero-shot setting by a noticeable margin. Our work reveals that LLMs can be an excellent compressor for music, but there remains significant territory to be conquered. We release our 4B token music-language corpora MusicPile, the collected MusicTheoryBench, code, model and demo in GitHub.
"""

# 生成导读的提示
prompt = f"""
请基于以下论文信息，生成一篇结构完整的论文导读，包括：
1. 研究背景与动机
2. 核心方法
3. 主要结果
4. 个人小结

论文信息：
{paper_info}

导读要求：
- 语言流畅，逻辑清晰
- 内容准确反映论文核心内容
- 结构合理，层次分明
- 长度适中，约1000-1500字
"""

def generate_summary():
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个专业的学术论文导读生成器，能够准确理解论文内容并生成结构清晰的导读。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    summary = generate_summary()
    with open("paper_summary.md", "w", encoding="utf-8") as f:
        f.write(summary)
    print("论文导读已生成并保存到 paper_summary.md")
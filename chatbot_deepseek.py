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

def chat_with_deepseek(prompt):
    """与 DeepSeek 模型对话"""
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个 helpful 的 AI 助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("=== DeepSeek Chatbot 示例 ===")
    print("输入 'exit' 退出程序")
    print()
    
    while True:
        user_input = input("你: ")
        if user_input.lower() == 'exit':
            print("再见！")
            break
        
        print("DeepSeek: 思考中...")
        response = chat_with_deepseek(user_input)
        print(f"DeepSeek: {response}")
        print()
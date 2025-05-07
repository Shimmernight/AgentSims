import asyncio
from agent.utils.llm import get_caller

async def test_llm(model_name: str, prompt: str = "Hello, how are you?") -> None:
    """
    测试指定模型的调用功能。
    
    Args:
        model_name: 模型名称（如 "gpt-3.5", "deepseek/deepseek-chat-v3-0324:free"）。
        prompt: 输入的提示文本。
    """
    try:
        print(f"Testing model: {model_name}")
        caller = get_caller(model_name)
        response = await caller.ask(prompt)
        print(f"Response from {model_name}: {response}")
    except Exception as e:
        print(f"Error testing {model_name}: {e}")

async def main():
    # 测试支持的模型
    models_to_test = [
        "deepseek/deepseek-chat-v3-0324:free"
    ]
    
    for model in models_to_test:
        await test_llm(model)

if __name__ == "__main__":
    asyncio.run(main())
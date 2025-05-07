from typing import List, Dict, Any
import os
import json
from openai import OpenAI
from agent.utils.llmExpends.BasicCaller import BasicCaller

abs_path = os.path.dirname(os.path.realpath(__file__))

class OpenRouterCaller(BasicCaller):
    def __init__(self, model: str = "openrouter/auto") -> None:
        self.model = model  # 动态传入模型名称
        self.api_key = ""
        with open(os.path.join(abs_path, "..", "..", "..", "config", "api_key.json"), "r", encoding="utf-8") as api_file:
            api_keys = json.loads(api_file.read())
            self.api_key = api_keys["openrouter"]
        if not self.api_key:
            raise ValueError("OpenRouter API key not found")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )
    
    async def ask(self, prompt: str) -> str:
        counter = 0
        result = "{}"
        while counter < 3:
            try:
                completion = self.client.chat.completions.create(
                    model=self.model,
                    # extra_headers={
                    #     "HTTP-Referer": "https://yourdomain.com",  # OpenRouter 要求
                    #     "X-Title": "AgentSims",  # OpenRouter 要求
                    # },
                    messages=[
                        {"role": "user", "content": prompt},
                    ],
                )
                result = completion.choices[0].message.content
                return result
            except Exception as e:
                print(f"Error calling OpenRouter (attempt {counter + 1}): {e}")
                counter += 1
        return result
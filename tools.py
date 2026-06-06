"""
AI REST API Tools - AI REST API工具
支持API设计、生成、文档
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIRESTAPITools:
    """
    AI REST API工具
    支持：设计、生成、文档
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_rest_api(self, resource: str, operations: List[str]) -> Dict:
        """设计REST API"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        ops_text = ", ".join(operations)

        prompt = f"""请为{resource}设计REST API：

操作：{ops_text}

请返回JSON格式：
{{
    "endpoints": [
        {{"method": "GET", "path": "/api/xxx", "description": "描述"}}
    ],
    "models": [
        {{"name": "模型名", "fields": {{"字段": "类型"}}}}
    ],
    "error_codes": ["错误码"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"api": content}

    def generate_fastapi_code(self, resource: str, operations: List[str]) -> str:
        """生成FastAPI代码"""
        if not self.client:
            return "LLM客户端未配置"

        ops_text = ", ".join(operations)

        prompt = f"""请为{resource}生成FastAPI代码：

操作：{ops_text}

要求：
1. Pydantic模型
2. CRUD端点
3. 错误处理
4. 文档字符串"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_flask_code(self, resource: str, operations: List[str]) -> str:
        """生成Flask代码"""
        if not self.client:
            return "LLM客户端未配置"

        ops_text = ", ".join(operations)

        prompt = f"""请为{resource}生成Flask代码：

操作：{ops_text}

要求：
1. Blueprint
2. CRUD端点
3. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_openapi_spec(self, api_description: str, endpoints: List[Dict]) -> str:
        """生成OpenAPI规范"""
        if not self.client:
            return "LLM客户端未配置"

        endpoints_text = json.dumps(endpoints, ensure_ascii=False)

        prompt = f"""请生成OpenAPI 3.0规范：

描述：{api_description}
端点：{endpoints_text}

请返回完整的YAML格式："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_api_client(self, api_spec: str, language: str) -> str:
        """生成API客户端"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据API规范生成{language}客户端：

{api_spec[:2000]}

要求：
1. 类型安全
2. 错误处理
3. 异步支持"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def design_api_versioning(self, current_version: str, new_features: List[str]) -> Dict:
        """设计API版本管理"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        features_text = ", ".join(new_features)

        prompt = f"""请设计API版本管理：

当前版本：{current_version}
新功能：{features_text}

请返回JSON格式：
{{
    "strategy": "版本策略",
    "url_format": "URL格式",
    "deprecation": "废弃策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"versioning": content}


def create_tools(**kwargs) -> AIRESTAPITools:
    """创建REST API工具"""
    return AIRESTAPITools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI REST API Tools")
    print()

    # 测试
    api = tools.design_rest_api("用户", ["创建", "查询", "更新", "删除"])
    print(json.dumps(api, ensure_ascii=False, indent=2))

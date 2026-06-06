# 🔌 AI REST API Tools

AI REST API工具，支持API设计、生成、文档。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ REST API设计
- 🚀 FastAPI代码生成
- 🌶️ Flask代码生成
- 📋 OpenAPI规范生成
- 📱 API客户端生成
- 🔄 API版本管理

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_rest_api_tools import create_tools

tools = create_tools()

# API设计
api = tools.design_rest_api("用户", ["创建", "查询", "更新", "删除"])

# FastAPI代码
fastapi = tools.generate_fastapi_code("用户", ["CRUD"])

# Flask代码
flask = tools.generate_flask_code("用户", ["CRUD"])

# OpenAPI规范
openapi = tools.generate_openapi_spec("用户管理API", endpoints)

# API客户端
client = tools.generate_api_client(api_spec, "Python")

# 版本管理
versioning = tools.design_api_versioning("v1", ["新功能"])
```

## 📁 项目结构

```
ai-rest-api-tools/
├── tools.py       # REST API工具核心
└── README.md
```

## 📄 许可证

MIT License

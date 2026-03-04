# LLM Detective 🔍

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A CLI tool for verifying third-party LLM API authenticity through fingerprint testing.**

一个通过指纹测试验证第三方 LLM API 真伪的命令行工具。

---

## ✨ Features | 核心特性

**English:**
- **Fingerprint Testing** - Uses carefully designed riddles to detect model characteristics
- **Multi-Model Detection** - Supports GPT-4, GPT-3.5, and Llama model detection
- **Async Concurrent Testing** - Fast parallel API testing for efficiency
- **Confidence Scoring** - Provides detailed confidence scores and analysis
- **Extensible Architecture** - Easy to add new models and detection strategies

**中文:**
- **指纹测试** - 使用精心设计的谜题检测模型特征
- **多模型检测** - 支持 GPT-4、GPT-3.5 和 Llama 模型检测
- **异步并发测试** - 快速并行 API 测试,提高效率
- **置信度评分** - 提供详细的置信度评分和分析
- **可扩展架构** - 轻松添加新模型和检测策略

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Clone the repository | 克隆仓库
git clone https://github.com/PerryLink/llm-detective.git
cd llm-detective

# Install dependencies | 安装依赖
pip install -e .
```

### Usage | 使用指南

```bash
# Basic usage | 基本使用
sherlock check --key "your-api-key" --url "https://api.openai.com/v1" --model "gpt-4"

# Example output | 示例输出
# ✅ VERIFIED (Confidence: 95.5%)
# All responses match GPT-4 patterns
```

### Command Options | 命令选项

- `--key` - Your API key | 你的 API 密钥
- `--url` - API endpoint URL | API 端点 URL
- `--model` - Model name to test | 要测试的模型名称

## 📁 Project Structure | 项目结构

```
llm-detective/
├── src/llm_detective/
│   ├── models.py              # Data models | 数据模型
│   ├── config.py              # Configuration | 配置管理
│   ├── detectors/             # Model detectors | 模型检测器
│   │   ├── base.py            # Detector protocol | 检测器协议
│   │   ├── registry.py        # Detector registry | 检测器注册表
│   │   ├── gpt4.py            # GPT-4 detector | GPT-4 检测器
│   │   ├── gpt35.py           # GPT-3.5 detector | GPT-3.5 检测器
│   │   └── llama.py           # Llama detector | Llama 检测器
│   ├── strategies/            # Analysis strategies | 分析策略
│   │   ├── base.py            # Strategy protocol | 策略协议
│   │   └── confidence.py      # Confidence strategy | 置信度策略
│   ├── fingerprints/          # Fingerprint database | 指纹数据库
│   │   └── riddles.py         # Test riddles | 测试谜题
│   ├── analyzer.py            # Response analyzer | 响应分析器
│   ├── examiner.py            # API examiner | API 检查器
│   └── cli.py                 # CLI interface | 命令行界面
├── tests/                     # Test suite | 测试套件
├── pyproject.toml             # Project config | 项目配置
├── LICENSE                    # Apache 2.0 License | 许可证
├── CONTRIBUTING.md            # Contribution guide | 贡献指南
└── README.md                  # This file | 本文件
```

## 🛠️ Tech Stack | 技术栈

- **Python 3.9+** - Core language | 核心语言
- **OpenAI SDK** - API client | API 客户端
- **Typer** - CLI framework | 命令行框架
- **Rich** - Terminal formatting | 终端格式化
- **Pytest** - Testing framework | 测试框架

## 🏗️ Architecture | 架构设计

**English:**
The project uses a **Strategy Pattern + Registry Architecture** for extensibility:

- **Detectors** - Pluggable model detection strategies
- **Registry** - Dynamic detector management
- **Strategies** - Configurable analysis algorithms
- **Fingerprints** - Universal test pattern format

**中文:**
项目采用**策略模式 + 注册表架构**实现高扩展性:

- **检测器** - 可插拔的模型检测策略
- **注册表** - 动态检测器管理
- **策略** - 可配置的分析算法
- **指纹** - 通用测试模式格式

## 🧪 Testing | 测试

```bash
# Run all tests | 运行所有测试
pytest -v

# Run with coverage | 运行覆盖率测试
pytest --cov=llm_detective --cov-report=html
```

## 📝 License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

## 🤝 Contributing | 贡献

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献! 详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📧 Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

---

**Made with ❤️ by Chance Dean**

# Contributing to LLM Detective

## English

### Project Status

LLM Detective is currently a **personal project** maintained by Chance Dean ([@PerryLink](https://github.com/PerryLink)). While contributions are welcome, please note that this is an individual effort and response times may vary.

### Reporting Issues

If you encounter bugs or have feature requests:

1. Check existing [issues](https://github.com/PerryLink/llm-detective/issues) to avoid duplicates
2. Create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem or feature
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (Python version, OS, etc.)

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/PerryLink/llm-detective.git
   cd llm-detective
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   pip install -e ".[dev]"
   ```

4. **Run tests to verify setup**
   ```bash
   pytest -v
   ```

### Code Standards

This project follows **PEP 8** style guidelines:

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable and function names
- Add docstrings for public functions and classes
- Type hints are encouraged but not required

**Recommended tools:**
```bash
# Format code
black src/ tests/

# Check style
flake8 src/ tests/

# Type checking (optional)
mypy src/
```

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, readable code
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**
   ```bash
   pytest -v
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add new detection strategy for Claude models"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   - Open a pull request on GitHub
   - Describe what changes you made and why
   - Reference any related issues

6. **Wait for review**
   - The maintainer will review your PR
   - Address any feedback or requested changes
   - Once approved, your PR will be merged

### Questions?

Feel free to open an issue for questions or reach out via email at novelnexusai@outlook.com.

---

## 中文

### 项目状态

LLM Detective 目前是由 Chance Dean ([@PerryLink](https://github.com/PerryLink)) 维护的**个人项目**。虽然欢迎贡献,但请注意这是个人项目,响应时间可能会有所不同。

### 报告问题

如果你遇到 bug 或有功能请求:

1. 检查现有 [issues](https://github.com/PerryLink/llm-detective/issues) 避免重复
2. 创建新 issue 并包含:
   - 清晰、描述性的标题
   - 问题或功能的详细描述
   - 重现步骤(针对 bug)
   - 期望行为 vs 实际行为
   - 环境详情(Python 版本、操作系统等)

### 开发环境搭建

1. **Fork 并克隆仓库**
   ```bash
   git clone https://github.com/PerryLink/llm-detective.git
   cd llm-detective
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安装依赖**
   ```bash
   pip install -e .
   pip install -e ".[dev]"
   ```

4. **运行测试验证设置**
   ```bash
   pytest -v
   ```

### 代码规范

本项目遵循 **PEP 8** 风格指南:

- 使用 4 个空格缩进(不使用 tab)
- 最大行长度: 88 字符(Black 格式化器默认值)
- 使用描述性的变量和函数名
- 为公共函数和类添加文档字符串
- 鼓励使用类型提示但非必需

**推荐工具:**
```bash
# 格式化代码
black src/ tests/

# 检查风格
flake8 src/ tests/

# 类型检查(可选)
mypy src/
```

### Pull Request 流程

1. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **进行修改**
   - 编写清晰、可读的代码
   - 为新功能添加测试
   - 如需要更新文档

3. **测试你的修改**
   ```bash
   pytest -v
   ```

4. **使用清晰的消息提交**
   ```bash
   git commit -m "feat: add new detection strategy for Claude models"
   ```

5. **推送并创建 PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   - 在 GitHub 上打开 pull request
   - 描述你做了什么修改以及为什么
   - 引用相关的 issues

6. **等待审查**
   - 维护者会审查你的 PR
   - 处理任何反馈或请求的修改
   - 一旦批准,你的 PR 将被合并

### 有问题?

欢迎通过 issue 提问或发送邮件至 novelnexusai@outlook.com。

---

**Thank you for contributing! | 感谢你的贡献!**

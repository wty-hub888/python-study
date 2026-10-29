# python-study

Python 学习练习项目，包含两个示例脚本。

## 项目结构

```
.
├── aipattner.py          # Streamlit AI 伴侣（调用 DeepSeek 对话模型）
├── 文本操作.py            # 文件读取基础示例（读取 resources/望庐山瀑布.txt）
├── resources/
│   ├── logo.png
│   └── 望庐山瀑布.txt
└── .gitignore
```

## 环境准备

1. Python 3.10+
2. 安装依赖：

```bash
pip install streamlit openai
```

## 配置 API 密钥

`aipattner.py` 通过环境变量读取 DeepSeek 密钥，不要把密钥写进代码。

- Windows 用户级环境变量：变量名 `API_KEY`，值为你的 DeepSeek API Key
- 配置后重启 PyCharm / 终端生效

## 运行方式

### 1. 文件读取示例

```bash
python 文本操作.py
```

### 2. Streamlit AI 伴侣

```bash
streamlit run aipattner.py
```

浏览器打开终端提示的本地地址（默认 `http://localhost:8501`）即可使用。

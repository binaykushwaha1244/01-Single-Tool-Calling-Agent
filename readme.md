# 🤖 AI Tool Calling Agent using Groq & OpenAI SDK

A beginner-friendly AI Agent built using the **OpenAI Python SDK** and **Groq's Llama 3.3 model** that demonstrates **Tool Calling (Function Calling)**.

This project shows how a Large Language Model (LLM) can intelligently decide when it needs to execute a Python function before generating its final response.

The goal of this project is to understand **how AI Agents work internally**, without relying on frameworks like LangChain, CrewAI, AutoGen, or LlamaIndex.

---

# 📌 Project Overview

Large Language Models are excellent at understanding and generating natural language, but they **cannot directly access external information** such as:

- Current Weather
- Latest News
- Database Records
- Stock Prices
- REST APIs
- File Systems

Instead of guessing (hallucinating), the model can request a **tool** (Python function) to perform a task.

Your Python code executes that function, returns the result to the model, and then the model generates the final answer.

This process is called **Tool Calling** (also known as Function Calling).

---

# 🚀 Features

- Built using the OpenAI Python SDK
- Uses Groq's Llama 3.3 model
- Demonstrates Tool Calling from scratch
- No external AI frameworks
- Beginner friendly
- Easy to understand code
- Shows the complete Tool Calling lifecycle

---

# 🛠 Available Tools

This project currently contains two tools.

## 🌤 get_weather(location)

Returns dummy weather information.

Example:

```
User:
What's the weather in India?
```

↓

Model calls

```
get_weather(location="India")
```

↓

Python returns

```
The weather in India is sunny with a high of minus 25 degree Celsius.
```

---

## 📰 get_news(topic)

Returns dummy news information.

Example:

```
User:
What's the recent news in India?
```

↓

Model calls

```
get_news(topic="India")
```

↓

Python returns

```
The latest news about India is that it's trending worldwide.
```

---

# 🔄 Execution Flow

The current implementation follows this exact workflow.

```
User
    │
    ▼
First API Call
    │
    ▼
Model decides which tool to call
    │
    ▼
if get_weather
        OR
if get_news
    │
    ▼
Execute Python Function
    │
    ▼
Append Tool Result to Messages
    │
    ▼
Second API Call
    │
    ▼
Final Natural Language Response
```

---

# 🧠 Why Two API Calls?

One of the most confusing parts of Tool Calling is understanding why **two API calls** are required.

### First API Call

The model analyzes the user's request and decides whether it needs to use a tool.

Example:

```
User:
What's the weather in India?
```

The model responds with something similar to:

```
Call get_weather(location="India")
```

Notice that **the model does not answer the user yet.**

Instead, it asks your Python program to execute a function.

---

### Python Executes the Function

Your Python code executes

```python
get_weather("India")
```

and gets

```
The weather in India is sunny with a high of minus 25 degree Celsius.
```

---

### Second API Call

Now the function result is sent back to the model.

Only then does the model generate a proper natural language response for the user.

---

# 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚠ Current Limitation

Although **two tools are registered**, this project currently processes **only one tool call per request**.

This means it works for:

✅

```
What's the weather in India?
```

or

```
What's the latest news in India?
```

But it does **not** yet support:

❌

```
What's the weather and latest news in India?
```

The current implementation executes **only one tool function** (`get_weather` or `get_news`) depending on what the model requests.

Supporting multiple tool calls will be added in a future version.

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/your-repository.git
```

Move into the project

```bash
cd your-repository
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶ Running the Project

```bash
python main.py
```

Change the user prompt inside `messages`.

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What's the recent weather in India?"
    }
]
```

or

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What's the recent news in India?"
    }
]
```

---

# 📚 What You'll Learn

By reading this project, you'll understand:

- What AI Agents are
- What Tool Calling means
- How LLMs decide to call functions
- How Python executes requested tools
- Why Tool Calling requires two API calls
- How tool outputs are sent back to the model
- How the final response is generated

---

# 💡 Why This Project?

Most AI Agent tutorials immediately introduce frameworks such as:

- LangChain
- CrewAI
- AutoGen
- LlamaIndex

While those frameworks are powerful, they hide much of the underlying logic.

This project focuses on understanding the **fundamental building blocks** first.

Once you understand this repository, learning advanced AI Agent frameworks becomes much easier because you'll already know what is happening behind the scenes.

---

# 🚧 Future Improvements

Planned features include:

- Multiple Tool Calls
- Dynamic Tool Registry
- Dictionary-based Tool Dispatcher
- Real Weather API
- Real News API
- Streaming Responses
- Memory Support
- Multi-Agent Workflow
- Autonomous AI Agent

---

# 🛠 Technologies Used

- Python
- OpenAI Python SDK
- Groq API
- Llama 3.3 70B Versatile
- JSON
- python-dotenv

---

# ⭐ Example

```
User:
What's the weather in India?
```

↓

LLM decides

```
Call get_weather()
```

↓

Python executes

```python
get_weather("India")
```

↓

Returns

```
The weather in India is sunny with a high of minus 25 degree Celsius.
```

↓

LLM generates

```
The weather in India is sunny with a high of minus 25 degree Celsius.
```

---

# 📖 Learning Goal

This repository is intended as an educational project to help beginners understand how modern AI Agents perform Tool Calling using the OpenAI SDK and Groq API before moving on to larger AI Agent frameworks.
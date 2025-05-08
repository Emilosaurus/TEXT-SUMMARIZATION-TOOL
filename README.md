# 🧠 Text Summarization using T5-small (PyTorch)

This project demonstrates the use of Hugging Face's `t5-small` model for abstractive text summarization using the PyTorch framework. It enables users to input any text and receive a concise summary powered by the T5 transformer architecture.

## 🚀 Features

- 🔍 Accepts raw text input from the user
- ✂️ Generates summaries using `t5-small`
- ⚙️ Built using PyTorch and Hugging Face Transformers
- 💡 Minimal interface with maximum functionality

## 🛠️ Requirements

- Python 3.8+
- PyTorch
- Transformers
- SymPy (version 1.12 required due to compatibility)

Install dependencies with:

```bash
pip install torch transformers sympy==1.12
```

## 📦 Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

2. Run the summarizer:

```bash
python summarize.py
```

3. Enter or paste the text when prompted and get a concise summary.

---

## 📄 Model Details

- **Model Used:** `t5-small`
- **Framework:** PyTorch (`framework="pt"`)
- **Task:** Abstractive summarization
- **Hugging Face Pipeline:** `pipeline("summarization")`

---

## 👨‍💻 Intern Details

**Company:** CODTECH IT SOLUTIONS  
**Name:** Emil Saj Abraham  
**Intern ID:** CT08DL252  
**Domain:** AI  
**Duration:** 8 weeks  
**Mentor:** Neela Santhosh
# TEXT SUMMARIZATION TOOL
 
project:
  name: Text Summarization using T5-small
  description: >
    A transformer-based text summarization tool using the Hugging Face T5-small model
    and PyTorch framework to generate concise summaries from user input.

requirements:
  python: ">=3.8"
  dependencies:
    - torch
    - transformers
    - sympy==1.12

model:
  name: t5-small
  framework: pytorch
  task: summarization
  prefix: summarize:
  parameters:
    max_length: 100
    min_length: 30
    do_sample: false

usage:
  input_type: user_text
  output_type: summary
  interface: CLI

internship_info:
  company: CODTECH IT SOLUTIONS
  name: Emil Saj Abraham
  intern_id: CT08DL252
  domain: AI
  duration: 8 weeks
  mentor: Neela Santhosh

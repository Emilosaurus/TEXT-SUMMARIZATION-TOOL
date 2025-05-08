from transformers import pipeline

def summarize_text(text, max_length=130, min_length=30):
    # Load BART summarizer
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Perform summarization
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]['summary_text']

if __name__ == "__main__":
    # Sample input article
    input_text = """
    Artificial Intelligence (AI) is rapidly transforming various sectors, from healthcare and finance to education 
    and transportation. In healthcare, AI-powered tools assist doctors in diagnosing diseases with higher accuracy. 
    Financial institutions use AI for fraud detection and algorithmic trading. Meanwhile, educational platforms leverage 
    AI to offer personalized learning experiences. However, the widespread adoption of AI raises ethical concerns, including 
    data privacy, job displacement, and algorithmic bias. It is crucial for policymakers and tech leaders to address 
    these challenges to ensure responsible AI development.
    """

    print("Original Text:\n", input_text.strip(), "\n")
    summary = summarize_text(input_text)
    print("Generated Summary:\n", summary)

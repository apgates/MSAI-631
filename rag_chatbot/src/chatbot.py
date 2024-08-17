from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.retrieval import retrieve

def generate_response(document, query):
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    input_text = f"{query} Context: {document}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def chatbot(query):
    with open("data/documents.txt", "r") as f:
        documents = f.readlines()
    document = retrieve(query, documents)
    response = generate_response(document, query)
    return response

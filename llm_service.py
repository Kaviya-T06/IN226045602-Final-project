from transformers import pipeline

# Load lightweight model
generator = pipeline("text-generation", model="google/flan-t5-base")

def generate_answer(context, query):
    prompt = f"""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """

    result = generator(prompt, max_length=200, do_sample=False)

    return result[0]["generated_text"]
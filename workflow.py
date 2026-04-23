from src.retrieval import retrieve
from src.llm_service import generate_answer
from src.hitl import escalate_to_human
def process_query(query):
    docs = retrieve(query)

    if not docs:
        return escalate_to_human(query)

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, query)

    # Simple decision logic
    if "I don't know" in answer or len(answer.strip()) < 20:
        return escalate_to_human(query)

    return answer
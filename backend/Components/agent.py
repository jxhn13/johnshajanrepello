from .retriever import is_safe_query, decompose_query, search_web, extract_content
from .synthesis import synthesize_answer
from .safety import is_safe_output

def handle_query(query):
    if not is_safe_query(query):
        return {"answer": "\u26a0\ufe0f Your query contains disallowed content. Please rephrase and try again."}, 400

    subqueries = decompose_query(query)
    all_documents = []
    for subq in subqueries:
        links = search_web(subq)
        for link in links:
            content = extract_content(link['link'])
            if content:
                all_documents.append({
                    "title": link['title'],
                    "url": link['link'],
                    "content": content
                })

    if not all_documents:
        return {"answer": "I couldn’t find information right now. You can try rephrasing the question or ask later."}, 404

    answer = synthesize_answer(query, all_documents)

    if is_safe_output(answer):
        return {"answer": answer}, 200
    else:
        return {"answer": "\u26a0\ufe0f The generated response was flagged as potentially unsafe. Please try rephrasing your query."}, 400
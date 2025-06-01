import os
import cohere
import logging
from dotenv import load_dotenv

load_dotenv() 
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

COHERE_API_KEY=os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY environment variable is not set.")
co = cohere.Client(COHERE_API_KEY)

def synthesize_answer(query, documents):
    if not documents:
        return "Sorry, I couldn't find any relevant information to answer your question."

    text_chunks = "\n\n".join([
        f"[Source {i+1}] ({doc['title']}):\n{doc['content'][:1000]}" for i, doc in enumerate(documents)
    ])

    prompt = f"""You are a helpful AI assistant. Answer the question below by synthesizing relevant points from the given sources. When citing, use phrases like “According to [Source 1], ...” as well as citation markers like [Source 1], [Source 2], etc.
Question: {query}

Sources:
{text_chunks}

Answer:"""

    try:
        response = co.generate(model="command", prompt=prompt, max_tokens=300, temperature=0.7)
        answer = response.generations[0].text.strip()
        sources = "\n\nSources:\n" + "\n".join(
            [f"[Source {i+1}] {doc['title']} - {doc['url']}" for i, doc in enumerate(documents)]
        )
        return f"{answer}{sources}"
    except cohere.CohereError as e:
        logger.error(f"Cohere API error: {e}")
        return "Sorry, there was an error processing your request."
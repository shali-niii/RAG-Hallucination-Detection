import json
import ollama

from rag.retriever import retrieve


MODEL = "qwen2.5:3b"
OUTPUT_PATH = "data/outputs/rag_output.json"


def generate_answer(question):
    documents = retrieve(question)

    evidence = "\n\n".join(
        f"Evidence {i}:\n{doc.page_content}"
        for i, doc in enumerate(documents, start=1)
    )

    prompt = f"""
You are a question-answering assistant.

Answer the question using ONLY the provided evidence.
Do not add information that is not supported by the evidence.

Question:
{question}

Evidence:
{evidence}

Answer:
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return documents, response["message"]["content"]


def save_output(question, documents, answer):
    output = {
        "question": question,
        "retrieved_evidence": [
            {
                "id": i,
                "text": document.page_content,
                "page": document.metadata.get("page", None)
            }
            for i, document in enumerate(documents, start=1)
        ],
        "generated_answer": answer
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4, ensure_ascii=False)

    print(f"\nOutput saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    question = input("Enter your question: ")

    documents, answer = generate_answer(question)

    print("\nRetrieved Evidence:\n")

    for i, document in enumerate(documents, start=1):
        print(f"--- Evidence {i} ---")
        print(document.page_content)
        print(f"Page: {document.metadata.get('page', 'Unknown')}")
        print()

    print("\nGenerated Answer:\n")
    print(answer)

    save_output(question, documents, answer)
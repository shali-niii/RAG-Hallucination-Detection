import json
from pathlib import Path

from generator.answer_generator import generate_answer


QUESTIONS_PATH = "data/questions/baseline_questions.txt"
OUTPUT_PATH = "data/outputs/baseline_results.json"


def main():
    questions = Path(QUESTIONS_PATH).read_text(encoding="utf-8").splitlines()

    results = []

    for i, question in enumerate(questions, start=1):
        question = question.strip()

        if not question:
            continue

        print(f"\nProcessing question {i}: {question}")

        documents, answer = generate_answer(question)

        result = {
            "question": question,
            "retrieved_evidence": [
                {
                    "id": j,
                    "text": document.page_content,
                    "page": document.metadata.get("page", None)
                }
                for j, document in enumerate(documents, start=1)
            ],
            "generated_answer": answer
        }

        results.append(result)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print(f"\nBaseline results saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
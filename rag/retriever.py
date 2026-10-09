from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


CHROMA_PATH = "data/chroma"


def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 5}
    )


def retrieve(question):
    retriever = get_retriever()
    return retriever.invoke(question)


if __name__ == "__main__":
    question = input("Enter your question: ")

    documents = retrieve(question)

    print(f"\nRetrieved {len(documents)} chunks:\n")

    for i, document in enumerate(documents, start=1):
        print(f"--- Evidence {i} ---")
        print(document.page_content)
        print(f"Page: {document.metadata.get('page', 'Unknown')}")
        print()
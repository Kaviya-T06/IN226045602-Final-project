from src.workflow import process_query

def main():
    print("🤖 RAG Customer Support Assistant (type 'exit' to quit)\n")

    while True:
        query = input("Ask your question: ")

        if query.lower() == "exit":
            break

        response = process_query(query)

        print("\n💬 Response:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()
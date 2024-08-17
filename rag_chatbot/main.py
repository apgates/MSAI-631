from src.chatbot import chatbot

def main():
    query = input("Ask me something: ")
    response = chatbot(query)
    print(response)

if __name__ == "__main__":
    main()


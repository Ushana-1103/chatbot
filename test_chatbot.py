import requests
import json

def test_chatbot():
    base_url = "http://localhost:8080/api/chat"
    
    test_cases = [
        "What are the symptoms of flu?",
        "I have a headache, what should I do?",
        "How can I prevent COVID-19?",
        "What are some general health tips?",
        "Tell me about diabetes",
        "I'm feeling stressed, any tips?",
        "What is the weather like today?"  # This is an unrelated query to test edge cases
    ]
    
    print("Testing chatbot responses:\n")
    print("-" * 50)
    
    for query in test_cases:
        print(f"Query: {query}")
        response = requests.post(
            base_url,
            json={"message": query}
        )
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {result['response']}")
        else:
            print(f"Error: {response.status_code}")
        print("-" * 50)

if __name__ == "__main__":
    test_chatbot() 
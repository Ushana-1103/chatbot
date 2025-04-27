import requests
import json

def evaluate_response(query, response, expected_keywords=None, category=None):
    score = 0
    max_score = 0
    
    # Check if response is not empty
    if response and len(response) > 0:
        score += 1
    max_score += 1
    
    # Check for relevant keywords
    if expected_keywords:
        found_keywords = sum(1 for keyword in expected_keywords if keyword.lower() in response.lower())
        score += found_keywords
        max_score += len(expected_keywords)
    
    # Check for medical disclaimer where appropriate
    if category in ['symptoms', 'conditions']:
        if 'consult' in response.lower() and 'healthcare' in response.lower():
            score += 1
        max_score += 1
    
    return score, max_score

def test_chatbot_accuracy():
    base_url = "http://localhost:8080/api/chat"
    total_score = 0
    total_possible = 0
    
    test_cases = [
        {
            'query': "What are the symptoms of flu?",
            'category': 'conditions',
            'expected_keywords': ['fever', 'cough', 'fatigue', 'headache', 'muscle']
        },
        {
            'query': "I have a headache, what should I do?",
            'category': 'symptoms',
            'expected_keywords': ['rest', 'water', 'pain', 'medication']
        },
        {
            'query': "How can I prevent COVID-19?",
            'category': 'conditions',
            'expected_keywords': ['mask', 'distance', 'wash', 'vaccine']
        },
        {
            'query': "Tell me about diabetes",
            'category': 'conditions',
            'expected_keywords': ['blood sugar', 'insulin', 'symptoms', 'treatment']
        },
        {
            'query': "I'm feeling stressed, any tips?",
            'category': 'mental_health',
            'expected_keywords': ['exercise', 'rest', 'relax', 'breathe']
        },
        {
            'query': "What is the weather like today?",  # Edge case
            'category': 'unrelated',
            'expected_keywords': ['question', 'help', 'health']  # Should provide helpful redirect
        }
    ]
    
    print("\nChatbot Accuracy Evaluation:\n")
    print("-" * 50)
    
    for test_case in test_cases:
        query = test_case['query']
        print(f"\nTesting: {query}")
        
        try:
            response = requests.post(
                base_url,
                json={"message": query}
            )
            
            if response.status_code == 200:
                result = response.json()
                response_text = result['response']
                score, max_score = evaluate_response(
                    query,
                    response_text,
                    test_case['expected_keywords'],
                    test_case['category']
                )
                
                accuracy = (score / max_score) * 100 if max_score > 0 else 0
                print(f"Category: {test_case['category']}")
                print(f"Accuracy: {accuracy:.1f}%")
                
                total_score += score
                total_possible += max_score
            else:
                print(f"Error: {response.status_code}")
                
        except Exception as e:
            print(f"Error testing query: {str(e)}")
    
    overall_accuracy = (total_score / total_possible) * 100 if total_possible > 0 else 0
    print("\n" + "=" * 50)
    print(f"\nOverall Chatbot Accuracy: {overall_accuracy:.1f}%")
    print("\nBreakdown:")
    print(f"Total Points: {total_score}/{total_possible}")
    print("=" * 50)

if __name__ == "__main__":
    test_chatbot_accuracy() 
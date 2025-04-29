from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from knowledge_base import get_health_info_natural, get_health_info, format_health_info, get_example_questions, get_symptom_management, get_related_symptoms
import random
import json
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Additional health information for quick reference
quick_health_info = {
    'flu': {
        'description': 'Influenza (flu) is a contagious respiratory illness caused by influenza viruses.',
        'symptoms': [
            'Fever or feeling feverish/chills',
            'Cough',
            'Sore throat',
            'Runny or stuffy nose',
            'Muscle or body aches',
            'Headaches',
            'Fatigue',
            'Some people may have vomiting and diarrhea'
        ],
        'prevention': [
            'Get annual flu vaccine',
            'Wash hands frequently',
            'Avoid close contact with sick people',
            'Cover mouth when coughing or sneezing',
            'Stay home when sick'
        ],
        'treatment': [
            'Rest and stay hydrated',
            'Over-the-counter medications for fever and pain',
            'Antiviral drugs if prescribed by a doctor',
            'Stay home to avoid spreading the virus'
        ]
    },
    'cold': {
        'description': 'The common cold is a viral infection of your nose and throat.',
        'symptoms': [
            'Runny or stuffy nose',
            'Sore throat',
            'Cough',
            'Congestion',
            'Slight body aches',
            'Mild headache',
            'Sneezing',
            'Low-grade fever'
        ],
        'prevention': [
            'Wash hands frequently',
            'Avoid touching face',
            'Stay away from sick people',
            'Get adequate sleep',
            'Maintain a healthy diet'
        ],
        'treatment': [
            'Rest and stay hydrated',
            'Use saline nasal spray',
            'Gargle with warm salt water',
            'Use over-the-counter cold medications',
            'Use a humidifier'
        ]
    },
    'covid': {
        'description': 'COVID-19 is a respiratory illness caused by the SARS-CoV-2 virus.',
        'symptoms': [
            'Fever or chills',
            'Cough',
            'Shortness of breath',
            'Fatigue',
            'Muscle or body aches',
            'Headache',
            'Loss of taste or smell',
            'Sore throat',
            'Congestion or runny nose',
            'Nausea or vomiting',
            'Diarrhea'
        ],
        'prevention': [
            'Get vaccinated and boosted',
            'Wear masks in crowded places',
            'Practice social distancing',
            'Wash hands frequently',
            'Stay home when sick'
        ],
        'treatment': [
            'Rest and stay hydrated',
            'Monitor symptoms',
            'Use over-the-counter medications for fever',
            'Seek medical attention if symptoms worsen',
            'Follow isolation guidelines if positive'
        ]
    },
    'allergy': {
        'description': 'Allergies occur when your immune system reacts to a foreign substance.',
        'symptoms': [
            'Sneezing',
            'Runny or stuffy nose',
            'Itchy eyes, nose, or throat',
            'Watery eyes',
            'Coughing',
            'Wheezing',
            'Shortness of breath',
            'Skin rashes or hives'
        ],
        'prevention': [
            'Identify and avoid triggers',
            'Keep windows closed during high pollen seasons',
            'Use air purifiers',
            'Wash bedding regularly',
            'Keep pets out of bedrooms'
        ],
        'treatment': [
            'Antihistamines',
            'Nasal sprays',
            'Eye drops',
            'Allergy shots (immunotherapy)',
            'Avoid known allergens'
        ]
    },
    'asthma': {
        'description': 'Asthma is a condition in which your airways narrow and swell and produce extra mucus.',
        'symptoms': [
            'Shortness of breath',
            'Chest tightness or pain',
            'Wheezing when exhaling',
            'Trouble sleeping due to breathing problems',
            'Coughing or wheezing attacks'
        ],
        'prevention': [
            'Identify and avoid triggers',
            'Use air purifiers',
            'Keep indoor air clean',
            'Stay indoors on high pollen days',
            'Get regular exercise'
        ],
        'treatment': [
            'Quick-relief inhalers',
            'Long-term control medications',
            'Allergy medications',
            'Bronchodilators',
            'Follow an asthma action plan'
        ]
    },
    'hypertension': {
        'description': 'High blood pressure is a common condition where the long-term force of blood against artery walls is high enough to cause health problems.',
        'symptoms': [
            'Often no symptoms',
            'Severe headaches',
            'Fatigue or confusion',
            'Vision problems',
            'Chest pain',
            'Difficulty breathing',
            'Irregular heartbeat'
        ],
        'prevention': [
            'Maintain healthy weight',
            'Exercise regularly',
            'Reduce sodium intake',
            'Limit alcohol',
            'Manage stress',
            'Quit smoking'
        ],
        'treatment': [
            'Lifestyle changes',
            'Blood pressure medications',
            'Regular monitoring',
            'Healthy diet (DASH diet)',
            'Regular exercise'
        ]
    },
    'diabetes': {
        'description': 'Diabetes is a chronic condition that affects how your body turns food into energy.',
        'symptoms': [
            'Increased thirst',
            'Frequent urination',
            'Extreme hunger',
            'Unexplained weight loss',
            'Fatigue',
            'Blurred vision',
            'Slow-healing sores'
        ],
        'prevention': [
            'Maintain healthy weight',
            'Exercise regularly',
            'Eat healthy foods',
            'Monitor blood sugar',
            'Regular check-ups'
        ],
        'treatment': [
            'Blood sugar monitoring',
            'Insulin therapy',
            'Oral medications',
            'Healthy diet',
            'Regular exercise',
            'Regular check-ups'
        ]
    }
}

# Add more example questions
example_questions_by_category = {
    'general_health': [
        "What are some general health tips?",
        "How can I maintain good health?",
        "What are the basics of staying healthy?",
        "What should I do to stay healthy?",
        "How can I improve my overall health?"
    ],
    'nutrition': [
        "What should I eat for a healthy diet?",
        "How many servings of fruits and vegetables should I eat?",
        "What are the main food groups?",
        "What are some healthy eating tips?",
        "How can I improve my nutrition?"
    ],
    'exercise': [
        "How much exercise should I get?",
        "What types of exercise are important?",
        "What are the benefits of regular exercise?",
        "How often should I exercise?",
        "What are some good exercises for beginners?"
    ],
    'mental_health': [
        "How can I improve my mental health?",
        "What are some mental health strategies?",
        "What are warning signs of mental health issues?",
        "How can I manage stress?",
        "What are some self-care practices?"
    ],
    'sleep': [
        "How much sleep do I need?",
        "What are good sleep habits?",
        "How can I improve my sleep?",
        "What is sleep hygiene?",
        "What are some tips for better sleep?"
    ],
    'conditions': [
        "Tell me about flu",
        "What are the symptoms of a cold?",
        "How can I prevent COVID-19?",
        "What should I know about allergies?",
        "How can I manage asthma?",
        "What is hypertension?",
        "How can I control diabetes?"
    ],
    'symptoms': [
        "I feel weak and nauseous?",
        "I feel weak, what should I do?",
        "I'm feeling nauseous, help!",
        "I have a headache, what can I do?",
        "I'm feeling tired all the time",
        "What should I do if I feel sick?",
        "I'm feeling stressed, any tips?",
        "I feel dizzy, what's wrong?"
    ]
}

def get_example_questions_by_category(category):
    return example_questions_by_category.get(category, [])

def get_all_example_questions():
    all_questions = []
    for category_questions in example_questions_by_category.values():
        all_questions.extend(category_questions)
    return all_questions

def get_quick_health_info(topic):
    topic = topic.lower()
    if topic in quick_health_info:
        return quick_health_info[topic]
    return None

def format_quick_health_info(info):
    if not info:
        return None
    
    formatted_response = []
    
    # Add description
    formatted_response.append(f"🔹 Description:\n{info['description']}\n")
    
    # Add symptoms
    formatted_response.append("🔹 Symptoms:")
    for symptom in info['symptoms']:
        formatted_response.append(f"• {symptom}")
    formatted_response.append("")
    
    # Add prevention
    formatted_response.append("🔹 Prevention:")
    for item in info['prevention']:
        formatted_response.append(f"• {item}")
    formatted_response.append("")
    
    # Add treatment
    formatted_response.append("🔹 Treatment:")
    for item in info['treatment']:
        formatted_response.append(f"• {item}")
    
    return "\n".join(formatted_response)

def chatbot_response(user_input):
    try:
        # Convert input to lowercase and strip whitespace
        user_input = user_input.lower().strip()
        
        # Check for general health queries
        general_health_keywords = ['general health', 'health tips', 'healthy lifestyle', 'stay healthy', 'healthy living', 'wellness tips']
        if any(keyword in user_input for keyword in general_health_keywords):
            general_health_info = get_health_info('general_health')
            if general_health_info:
                response = "Here are some general health tips to help you maintain a healthy lifestyle:\n\n"
                response += f"{general_health_info['description']}\n\n"
                response += "Key Health Tips:\n"
                for tip in general_health_info['tips']:
                    response += f"• {tip}\n"
                response += "\nWarning Signs to Watch For:\n"
                for sign in general_health_info['warning_signs']:
                    response += f"• {sign}\n"
                return response

        # Check for common health-related phrases
        common_phrases = {
            'hello': 'Hello! How can I help you with your health questions today?',
            'hi': 'Hi! I\'m here to help with your health questions. What would you like to know?',
            'help': 'I can help you with information about various health topics. Try asking about:\n- General health tips\n- Nutrition advice\n- Exercise recommendations\n- Mental health strategies\n- Sleep hygiene\n- Common conditions (flu, cold, COVID-19, etc.)\n- Symptom management',
            'thank': 'You\'re welcome! Feel free to ask if you have any other health questions.',
            'bye': 'Goodbye! Take care of your health!'
        }
        
        for phrase, response in common_phrases.items():
            if phrase in user_input:
                return response

        # Check for quick health information first
        quick_info = get_quick_health_info(user_input)
        if quick_info:
            return format_quick_health_info(quick_info)

        # Try to get health information using natural language processing
        health_info = get_health_info_natural(user_input)
        if health_info:
            return format_health_info(health_info)

        # Check for specific health conditions
        for condition in ['flu', 'cold', 'covid', 'allergy', 'asthma', 'hypertension', 'diabetes']:
            if condition in user_input:
                info = get_quick_health_info(condition)
                if info:
                    return format_quick_health_info(info)

        # Check for symptom-related queries
        symptom_keywords = ['symptom', 'feel', 'feeling', 'have', 'suffering', 'experiencing']
        if any(keyword in user_input for keyword in symptom_keywords):
            # Extract potential symptoms from the input
            symptoms = [word for word in user_input.split() if word in ['weak', 'nauseous', 'headache', 'tired', 'sick', 'stressed', 'dizzy']]
            if symptoms:
                response = "Here's what you can do:\n\n"
                for symptom in symptoms:
                    management = get_symptom_management(symptom)
                    if management:
                        response += f"For {symptom}:\n"
                        for item in management:
                            response += f"• {item}\n"
                        response += "\n"
                if response != "Here's what you can do:\n\n":
                    return response + "\nRemember to consult a healthcare professional if symptoms persist or worsen."

        # If no specific information is found, provide a general response with example questions
        example_questions = get_all_example_questions()
        random_questions = random.sample(example_questions, min(5, len(example_questions)))
        
        response = "I'm not sure I understand your question. Here are some example questions you can ask:\n\n"
        for question in random_questions:
            response += f"• {question}\n"
        
        response += "\nYou can also ask about:\n"
        response += "• Specific conditions (flu, cold, COVID-19, allergies, asthma, etc.)\n"
        response += "• Symptoms you're experiencing\n"
        response += "• General health advice\n"
        response += "• Nutrition and exercise tips\n"
        response += "• Mental health and sleep advice\n\n"
        response += "Remember, I'm here to provide general health information. For specific medical advice, please consult a healthcare professional."
        
        return response

    except Exception as e:
        print(f"Error in chatbot_response: {str(e)}")
        return "I'm sorry, I encountered an error while processing your request. Please try rephrasing your question or ask about a different health topic."

# Feedback storage
FEEDBACK_FILE = 'feedback.json'

def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r') as f:
            return json.load(f)
    return []

def save_feedback(feedback_data):
    feedback_list = load_feedback()
    feedback_list.append(feedback_data)
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedback_list, f, indent=4)

@app.route('/')
def index():
    logger.debug("Received request for index page")
    return render_template('index.html')

@app.route('/test')
def test():
    logger.debug("Received request for test endpoint")
    return "Server is working!"

@app.route('/api/chat', methods=['POST'])
def chat():
    logger.debug("Received chat request")
    data = request.json
    user_message = data.get('message', '')
    response = chatbot_response(user_message)
    return jsonify({'response': response})

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.get_json()
        feedback_data = {
            'message_id': data.get('messageId'),
            'feedback': data.get('feedback'),
            'message': data.get('message'),
            'timestamp': datetime.now().isoformat()
        }
        
        save_feedback(feedback_data)
        return jsonify({'status': 'success', 'message': 'Feedback received'})
    except Exception as e:
        logger.error(f"Error processing feedback: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    print("Starting Baymax server...")
    print("Server will be available at:")
    print("http://localhost:8080")
    print("http://127.0.0.1:8080")
    print("Press Ctrl+C to stop the server")
    try:
        app.run(host='127.0.0.1', port=8080, debug=True)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        input("Press Enter to exit...") 
# HealthBot Knowledge Base
# This file contains the health-related information and responses for the chatbot

# Dictionary to store health information
health_info = {
    # Common terms mapping
    "common_terms": {
        "flu": ["influenza", "the flu", "flu symptoms", "fever", "chills", "body ache"],
        "cold": ["common cold", "cold symptoms", "cold virus", "runny nose", "sore throat", "congestion"],
        "covid": ["covid-19", "coronavirus", "covid symptoms", "pandemic", "respiratory illness"],
        "allergy": ["allergies", "allergic reaction", "allergic symptoms", "hay fever", "seasonal allergies"],
        "asthma": ["asthma attack", "asthmatic", "asthma symptoms", "breathing problems", "wheezing"],
        "hypertension": ["high blood pressure", "high bp", "hypertensive", "elevated blood pressure"],
        "diabetes": ["diabetic", "blood sugar", "diabetes symptoms", "type 1 diabetes", "type 2 diabetes"],
        "headache": ["head pain", "migraine", "headache symptoms", "tension headache", "cluster headache"],
        "nausea": ["feeling sick", "queasy", "nauseous", "upset stomach", "vomiting"],
        "weakness": ["fatigue", "tiredness", "weak", "exhaustion", "low energy"],
        "stress": ["anxiety", "pressure", "stressed", "worried", "tense"],
        "sleep": ["insomnia", "sleep problems", "sleep issues", "trouble sleeping", "restless sleep"],
        "exercise": ["physical activity", "workout", "fitness", "training", "sports"],
        "nutrition": ["diet", "eating", "food", "healthy eating", "meal planning"],
        "mental_health": ["psychological", "emotional", "mental well-being", "depression", "anxiety"],
        "heart": ["cardiac", "heart disease", "heart attack", "chest pain", "cardiovascular"],
        "skin": ["dermatology", "skin problems", "rash", "acne", "eczema"],
        "digestion": ["stomach", "gastrointestinal", "indigestion", "heartburn", "bloating"],
        "pain": ["ache", "sore", "discomfort", "injury", "chronic pain"],
        "emergency": ["urgent", "critical", "severe", "life-threatening", "911"]
    },

    # General Health Information
    "general_health": {
        "description": "Maintaining good health involves a combination of proper nutrition, regular exercise, adequate sleep, and stress management.",
        "tips": [
            "Eat a balanced diet with plenty of fruits and vegetables",
            "Stay hydrated by drinking at least 8 glasses of water daily",
            "Get 7-9 hours of quality sleep each night",
            "Manage stress through meditation, yoga, or other relaxation techniques",
            "Maintain regular physical activity",
            "Schedule regular health check-ups",
            "Practice good hygiene habits",
            "Limit alcohol consumption and avoid smoking",
            "Maintain a healthy weight",
            "Practice safe sex and get regular STI screenings",
            "Wear sunscreen and protect your skin",
            "Stay up to date with vaccinations",
            "Practice good oral hygiene",
            "Learn basic first aid and CPR"
        ],
        "warning_signs": [
            "Unexplained weight loss or gain",
            "Persistent fatigue",
            "Changes in bowel or bladder habits",
            "Unusual bleeding or discharge",
            "Persistent pain or discomfort",
            "Changes in skin appearance",
            "Difficulty breathing",
            "Changes in vision or hearing",
            "Mood changes or depression",
            "Memory problems or confusion"
        ]
    },

    # Nutrition and Diet
    "nutrition": {
        "description": "Proper nutrition is essential for maintaining good health and preventing diseases.",
        "food_groups": {
            "fruits_vegetables": "Aim for 5-9 servings daily, including a variety of colors",
            "proteins": "Include lean meats, fish, beans, and nuts",
            "grains": "Choose whole grains over refined grains",
            "dairy": "Opt for low-fat or non-fat dairy products",
            "fats": "Focus on healthy fats like olive oil, avocados, and nuts"
        },
        "dietary_guidelines": [
            "Limit processed foods and added sugars",
            "Control portion sizes",
            "Read nutrition labels",
            "Stay within daily calorie needs",
            "Include fiber-rich foods"
        ]
    },

    # Exercise and Physical Activity
    "exercise": {
        "description": "Regular physical activity is crucial for maintaining physical and mental health.",
        "types": {
            "aerobic": "150 minutes of moderate or 75 minutes of vigorous activity weekly",
            "strength": "2-3 sessions per week targeting major muscle groups",
            "flexibility": "Daily stretching to maintain range of motion",
            "balance": "Exercises to prevent falls, especially for older adults"
        },
        "benefits": [
            "Improves cardiovascular health",
            "Strengthens muscles and bones",
            "Boosts mood and mental health",
            "Helps maintain healthy weight",
            "Reduces risk of chronic diseases"
        ]
    },

    # Mental Health
    "mental_health": {
        "description": "Mental health is as important as physical health for overall well-being.",
        "conditions": {
            "depression": {
                "symptoms": [
                    "Persistent sadness",
                    "Loss of interest in activities",
                    "Changes in sleep patterns",
                    "Changes in appetite",
                    "Fatigue",
                    "Difficulty concentrating",
                    "Feelings of worthlessness",
                    "Thoughts of death or suicide"
                ],
                "treatment": [
                    "Psychotherapy",
                    "Medication if prescribed",
                    "Regular exercise",
                    "Healthy sleep habits",
                    "Social support",
                    "Stress management"
                ]
            },
            "anxiety": {
                "symptoms": [
                    "Excessive worry",
                    "Restlessness",
                    "Difficulty concentrating",
                    "Irritability",
                    "Muscle tension",
                    "Sleep problems",
                    "Panic attacks"
                ],
                "management": [
                    "Cognitive behavioral therapy",
                    "Relaxation techniques",
                    "Regular exercise",
                    "Healthy diet",
                    "Adequate sleep",
                    "Stress reduction",
                    "Medication if prescribed"
                ]
            }
        },
        "self_care": [
            "Practice mindfulness and meditation",
            "Maintain social connections",
            "Set realistic goals",
            "Take breaks and practice self-care",
            "Get regular exercise",
            "Eat a balanced diet",
            "Get adequate sleep",
            "Limit alcohol and caffeine",
            "Practice relaxation techniques",
            "Seek professional help when needed"
        ]
    },

    # Sleep Health
    "sleep": {
        "description": "Quality sleep is essential for physical and mental recovery.",
        "recommendations": {
            "duration": "7-9 hours for adults, 8-10 hours for teenagers, 9-12 hours for children",
            "environment": "Cool, dark, and quiet room",
            "routine": "Consistent sleep schedule, even on weekends"
        },
        "sleep_hygiene": [
            "Limit screen time before bed",
            "Avoid caffeine and large meals before sleep",
            "Create a relaxing bedtime routine",
            "Keep the bedroom for sleep only",
            "Exercise regularly but not too close to bedtime",
            "Manage stress and anxiety",
            "Limit naps during the day",
            "Avoid alcohol before bed",
            "Keep a consistent sleep schedule",
            "Create a comfortable sleep environment"
        ],
        "sleep_disorders": {
            "insomnia": "Difficulty falling or staying asleep",
            "sleep_apnea": "Breathing interruptions during sleep",
            "restless_legs": "Uncomfortable sensations in legs during rest",
            "narcolepsy": "Excessive daytime sleepiness"
        }
    },

    # Common Health Conditions
    "conditions": {
        "heart_disease": {
            "description": "Heart disease refers to several types of heart conditions that can lead to serious health problems.",
            "symptoms": [
                "Chest pain or discomfort",
                "Shortness of breath",
                "Irregular heartbeat",
                "Fatigue",
                "Swelling in legs, ankles, or feet"
            ],
            "risk_factors": [
                "High blood pressure",
                "High cholesterol",
                "Smoking",
                "Diabetes",
                "Obesity",
                "Family history",
                "Age",
                "Stress"
            ],
            "prevention": [
                "Maintain healthy blood pressure",
                "Control cholesterol levels",
                "Don't smoke",
                "Exercise regularly",
                "Eat a heart-healthy diet",
                "Maintain healthy weight",
                "Manage stress",
                "Get regular check-ups"
            ]
        },
        "arthritis": {
            "description": "Arthritis is inflammation of one or more joints, causing pain and stiffness.",
            "types": {
                "osteoarthritis": "Most common type, caused by wear and tear of joint cartilage",
                "rheumatoid": "Autoimmune disease that affects the joints",
                "gout": "Caused by uric acid crystal buildup in joints",
                "psoriatic": "Associated with psoriasis"
            },
            "symptoms": [
                "Joint pain",
                "Stiffness",
                "Swelling",
                "Reduced range of motion",
                "Warmth around the joint"
            ],
            "management": [
                "Regular exercise",
                "Weight management",
                "Physical therapy",
                "Medications as prescribed",
                "Joint protection techniques",
                "Heat and cold therapy",
                "Assistive devices if needed"
            ]
        }
    },

    # Preventive Care
    "preventive_care": {
        "description": "Regular preventive care can help detect health issues early.",
        "recommendations": {
            "checkups": "Annual physical exam",
            "screenings": [
                "Blood pressure check",
                "Cholesterol screening",
                "Diabetes screening",
                "Cancer screenings as recommended",
                "Vision and dental check-ups"
            ],
            "vaccinations": "Stay up to date with recommended vaccines"
        }
    },

    # Healthy Aging
    "aging": {
        "description": "Maintaining health and quality of life as we age.",
        "tips": [
            "Stay physically active",
            "Maintain social connections",
            "Keep the mind active with learning",
            "Eat a balanced diet",
            "Get regular health check-ups",
            "Practice fall prevention",
            "Manage chronic conditions"
        ]
    },

    # Emergency Situations
    "emergency": {
        "description": "Know when to seek immediate medical attention and how to respond to emergencies.",
        "warning_signs": [
            "Chest pain or pressure",
            "Difficulty breathing",
            "Sudden severe pain",
            "Sudden dizziness or confusion",
            "Severe or persistent vomiting",
            "Sudden vision changes",
            "Uncontrolled bleeding",
            "Loss of consciousness",
            "Seizures",
            "Severe allergic reactions"
        ],
        "action": "Call emergency services (911) immediately if experiencing any of these symptoms. Stay calm and follow the dispatcher's instructions.",
        "first_aid": {
            "choking": "Perform the Heimlich maneuver if the person is conscious and cannot breathe",
            "bleeding": "Apply direct pressure to the wound with a clean cloth",
            "burns": "Cool the burn with running water for 10-15 minutes",
            "heart_attack": "Call 911, help the person sit down, and give aspirin if available",
            "stroke": "Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call 911"
        }
    },

    # Common Symptoms and Their Management
    "symptoms": {
        "weakness": {
            "description": "Feeling weak or fatigued can have various causes and solutions.",
            "possible_causes": [
                "Lack of sleep",
                "Poor nutrition",
                "Dehydration",
                "Stress or anxiety",
                "Underlying medical conditions"
            ],
            "management": [
                "Get adequate rest and sleep",
                "Stay hydrated",
                "Eat balanced meals regularly",
                "Exercise moderately",
                "Manage stress levels",
                "Consult a doctor if persistent"
            ]
        },
        "nausea": {
            "description": "Feeling nauseous or queasy can be managed with various approaches.",
            "possible_causes": [
                "Motion sickness",
                "Food poisoning",
                "Viral infections",
                "Pregnancy",
                "Medication side effects",
                "Anxiety or stress"
            ],
            "management": [
                "Stay hydrated with small sips of water",
                "Eat small, bland meals",
                "Avoid strong smells",
                "Get fresh air",
                "Try ginger tea or ginger ale",
                "Rest in a comfortable position",
                "Seek medical attention if severe or persistent"
            ]
        },
        "headache": {
            "description": "Headaches can range from mild to severe and have various causes.",
            "types": {
                "tension": "Most common, feels like pressure around head",
                "migraine": "Severe, often with nausea and light sensitivity",
                "cluster": "Intense pain around one eye",
                "sinus": "Pain in forehead and cheekbones"
            },
            "management": [
                "Rest in a quiet, dark room",
                "Stay hydrated",
                "Apply cold or warm compress",
                "Practice relaxation techniques",
                "Take over-the-counter pain relief if appropriate",
                "Seek medical attention if severe or persistent"
            ]
        },
        "fever": {
            "description": "Fever is a common symptom indicating the body is fighting an infection.",
            "management": [
                "Stay hydrated",
                "Rest",
                "Use fever-reducing medication if appropriate",
                "Keep cool with light clothing",
                "Monitor temperature regularly",
                "Seek medical attention if high fever or persistent"
            ]
        },
        "cough": {
            "description": "Coughing can be a symptom of various conditions.",
            "types": {
                "dry": "No mucus, often irritating",
                "wet": "Produces mucus or phlegm",
                "chronic": "Lasts more than 8 weeks"
            },
            "management": [
                "Stay hydrated",
                "Use cough drops or honey",
                "Use a humidifier",
                "Avoid irritants like smoke",
                "Get plenty of rest",
                "Seek medical attention if severe or persistent"
            ]
        }
    }
}

# List of example questions users can ask
example_questions = {
    "general_health": [
        "I feel weak, what should I do?",
        "I'm feeling nauseous, help!",
        "I have a headache, what can I do?",
        "I'm feeling tired all the time",
        "What should I do if I feel sick?",
        "I'm feeling stressed, any tips?",
        "I feel dizzy, what's wrong?"
    ],
    "nutrition": [
        "What should I eat for a healthy diet?",
        "How many servings of fruits and vegetables should I eat?",
        "What are the main food groups?",
        "What are some dietary guidelines?",
        "How can I improve my nutrition?"
    ],
    "exercise": [
        "How much exercise should I get?",
        "What types of exercise are important?",
        "What are the benefits of regular exercise?",
        "How often should I exercise?",
        "What are some good exercises for beginners?"
    ],
    "mental_health": [
        "How can I improve my mental health?",
        "What are some mental health strategies?",
        "What are warning signs of mental health issues?",
        "How can I manage stress?",
        "What are some self-care practices?"
    ],
    "sleep": [
        "How much sleep do I need?",
        "What are good sleep habits?",
        "How can I improve my sleep?",
        "What is sleep hygiene?",
        "What are some tips for better sleep?"
    ],
    "conditions": [
        "How can I manage high blood pressure?",
        "What should I know about diabetes?",
        "How can I lower my cholesterol?",
        "What are the symptoms of hypertension?",
        "How do I manage chronic conditions?"
    ],
    "preventive_care": [
        "What preventive care do I need?",
        "What health screenings should I get?",
        "How often should I get check-ups?",
        "What vaccinations do I need?",
        "What are important health screenings?"
    ],
    "aging": [
        "How can I stay healthy as I age?",
        "What are tips for healthy aging?",
        "How can I prevent falls?",
        "What should I know about aging health?",
        "How can I maintain quality of life as I age?"
    ],
    "emergency": [
        "When should I seek emergency care?",
        "What are emergency warning signs?",
        "What symptoms need immediate attention?",
        "When should I call emergency services?",
        "What are signs of a medical emergency?"
    ]
}

# Function to map natural language terms to medical terms
def map_natural_to_medical(term):
    term = term.lower()
    for medical_term, natural_terms in health_info["common_terms"].items():
        if term in natural_terms or term == medical_term:
            return medical_term
    return term

# Function to get health information with natural language support
def get_health_info_natural(topic):
    # First try to map the topic to a medical term
    mapped_topic = map_natural_to_medical(topic)
    
    # Check if it's a symptom
    if mapped_topic in health_info.get("symptoms", {}):
        return health_info["symptoms"][mapped_topic]
    
    # Check other categories
    if mapped_topic in health_info:
        return health_info[mapped_topic]
    
    return None

# Function to get health information
def get_health_info(topic):
    if topic in health_info:
        return health_info[topic]
    return None

# Function to format health information for display
def format_health_info(info):
    if not info:
        return "I don't have specific information about that topic. Please try another health-related question."
    
    formatted_response = []
    
    # Add description if available
    if "description" in info:
        formatted_response.append(f"🔹 Description:\n{info['description']}\n")
    
    # Add symptoms if available
    if "symptoms" in info:
        formatted_response.append("🔹 Symptoms:")
        if isinstance(info["symptoms"], list):
            for symptom in info["symptoms"]:
                formatted_response.append(f"• {symptom}")
        elif isinstance(info["symptoms"], dict):
            for symptom, description in info["symptoms"].items():
                formatted_response.append(f"• {symptom}: {description}")
        formatted_response.append("")
    
    # Add possible causes if available
    if "possible_causes" in info:
        formatted_response.append("🔹 Possible Causes:")
        for cause in info["possible_causes"]:
            formatted_response.append(f"• {cause}")
        formatted_response.append("")
    
    # Add types if available (for conditions like headaches)
    if "types" in info:
        formatted_response.append("🔹 Types:")
        if isinstance(info["types"], dict):
            for type_name, description in info["types"].items():
                formatted_response.append(f"• {type_name.title()}: {description}")
        elif isinstance(info["types"], list):
            for type_name in info["types"]:
                formatted_response.append(f"• {type_name}")
        formatted_response.append("")
    
    # Add management/treatment information
    if "management" in info:
        formatted_response.append("🔹 Management/Treatment:")
        for item in info["management"]:
            formatted_response.append(f"• {item}")
        formatted_response.append("")
    
    # Add prevention if available
    if "prevention" in info:
        formatted_response.append("🔹 Prevention:")
        for item in info["prevention"]:
            formatted_response.append(f"• {item}")
        formatted_response.append("")
    
    # Add treatment if available
    if "treatment" in info:
        formatted_response.append("🔹 Treatment:")
        for item in info["treatment"]:
            formatted_response.append(f"• {item}")
        formatted_response.append("")
    
    # Add recommendations if available
    if "recommendations" in info:
        formatted_response.append("🔹 Recommendations:")
        if isinstance(info["recommendations"], dict):
            for key, value in info["recommendations"].items():
                if isinstance(value, list):
                    formatted_response.append(f"  {key.replace('_', ' ').title()}:")
                    for item in value:
                        formatted_response.append(f"  • {item}")
                else:
                    formatted_response.append(f"• {key.replace('_', ' ').title()}: {value}")
        else:
            for item in info["recommendations"]:
                formatted_response.append(f"• {item}")
        formatted_response.append("")
    
    # Add tips if available
    if "tips" in info:
        formatted_response.append("🔹 Tips:")
        for tip in info["tips"]:
            formatted_response.append(f"• {tip}")
        formatted_response.append("")
    
    # Add warning signs if available
    if "warning_signs" in info:
        formatted_response.append("🔹 Warning Signs:")
        for sign in info["warning_signs"]:
            formatted_response.append(f"• {sign}")
        formatted_response.append("")
    
    # Add food groups if available
    if "food_groups" in info:
        formatted_response.append("🔹 Food Groups:")
        if isinstance(info["food_groups"], dict):
            for group, description in info["food_groups"].items():
                formatted_response.append(f"• {group.replace('_', ' ').title()}: {description}")
        formatted_response.append("")
    
    # Add dietary guidelines if available
    if "dietary_guidelines" in info:
        formatted_response.append("🔹 Dietary Guidelines:")
        for guideline in info["dietary_guidelines"]:
            formatted_response.append(f"• {guideline}")
        formatted_response.append("")
    
    # Add benefits if available
    if "benefits" in info:
        formatted_response.append("🔹 Benefits:")
        for benefit in info["benefits"]:
            formatted_response.append(f"• {benefit}")
        formatted_response.append("")
    
    # Add strategies if available
    if "strategies" in info:
        formatted_response.append("🔹 Strategies:")
        for strategy in info["strategies"]:
            formatted_response.append(f"• {strategy}")
        formatted_response.append("")
    
    # Add sleep hygiene if available
    if "sleep_hygiene" in info:
        formatted_response.append("🔹 Sleep Hygiene:")
        for item in info["sleep_hygiene"]:
            formatted_response.append(f"• {item}")
        formatted_response.append("")
    
    return "\n".join(formatted_response)

# Function to get example questions for a topic
def get_example_questions(topic):
    if topic in example_questions:
        return example_questions[topic]
    return None

# Function to get all example questions
def get_all_example_questions():
    all_questions = []
    for topic, questions in example_questions.items():
        all_questions.extend(questions)
    return all_questions

# Function to get related symptoms for a condition
def get_related_symptoms(condition):
    if condition in health_info.get("conditions", {}):
        return health_info["conditions"][condition].get("symptoms", [])
    return []

# Function to get management tips for a symptom
def get_symptom_management(symptom):
    # First try to map the symptom to a medical term
    mapped_symptom = map_natural_to_medical(symptom)
    
    # Check if the symptom exists in our knowledge base
    if "symptoms" in health_info and mapped_symptom in health_info["symptoms"]:
        return health_info["symptoms"][mapped_symptom].get("management", [])
    
    # If not found, return an empty list
    return [] 
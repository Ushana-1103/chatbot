# Baymax

A Flask-based chatbot that provides health-related information and advice. The chatbot can answer questions about various health conditions, symptoms, and provide general health tips.

## Features

- Information about common health conditions (flu, cold, COVID-19, etc.)
- Symptom management advice
- Mental health support
- General health tips
- Natural language understanding for health queries

## Technical Stack

- Python 3.x
- Flask
- Flask-CORS
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/baymax.git
cd baymax
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:8080`

## Usage

- Open `index.html` in your browser
- Type your health-related questions in the chat interface
- The bot will provide relevant information and advice

## Testing

Run the accuracy tests:
```bash
python test_chatbot_accuracy.py
```

## Current Accuracy Metrics

- Overall Accuracy: 61.8%
- Strong in disease information (80%+ for conditions)
- Good handling of unrelated queries (75%)
- Areas for improvement in symptom management and mental health responses

## Important Note

This chatbot is for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
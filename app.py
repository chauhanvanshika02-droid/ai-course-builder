from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form['topic']
    level = request.form['level']
    goal = request.form['goal']

    prompt = f"""
    You are an AI course builder.
    Create a personalized course outline for someone who wants to learn "{topic}".
    Skill level: {level}.
    Goal: {goal}.
    Include modules, learning outcomes, and recommended resources.
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)

    course = response.text
    return render_template('result.html', topic=topic, course=course)

if __name__ == '__main__':
    app.run(debug=True)

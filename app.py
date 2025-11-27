from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/generate', methods=['POST'])
def generate():
    ingredients = request.form.get('ingredients', '').strip()
    cuisine = request.form.get('cuisine', '').strip()
    diet = request.form.get('diet', '').strip()

    
    if not ingredients or not cuisine or not diet:
        return render_template("home.html", error="Please fill all fields.")

    
    prompt = f"""
Create a detailed recipe using these inputs:
Ingredients: {ingredients}
Cuisine: {cuisine}
Diet preference: {diet}

Include:
- Dish name
- Ingredients list
- Step-by-step instructions
- Serving size
- Optional variations
"""

    # Call AI model
    try:
        # --- OpenAI ---
        #response = openai.ChatCompletion.create(
            #model="gpt-3.5-turbo",  # Use your preferred model
            #messages=[{"role": "user", "content": prompt}]
        #)
        #recipe = response.choices[0].message["content"]

        response = client.chat.completions.create(
             model="llama-3.1-8b-instant",
             messages=[{"role": "user", "content": prompt}]
        )
        recipe = response.choices[0].message["content"]

    except Exception as e:
        recipe = f"Error generating recipe: {str(e)}"

    return render_template("result.html", recipe=recipe)


if __name__ == '__main__':
    app.run(debug=True)

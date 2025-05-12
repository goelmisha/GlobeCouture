from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key="your-perplexity-api-key", base_url="https://api.perplexity.ai")

def build_prompt(city, country):
    return f"What is something interesting about {city}, {country}?"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    city = data.get("city", "Unknown city")
    country = data.get("country", "Unknown country")

    prompt = build_prompt(city, country)

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=[
            {"role": "system", "content": "You're a smart travel assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify(reply=response.choices[0].message.content.strip())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

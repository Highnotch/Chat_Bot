import openai
import os
import sys
from flask import Flask, render_template, request


openai.api_key = "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"
def generate_chatbot_response(components):
  
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are an assistant to give short answers "},
          {"role": "user", "content": "Who won the world series in 2020?"},
          {"role": "assistant", "content": "The Los Angeles Dodgers "},
          {"role": "user", "content": components }])
  output=response["choices"][0]["message"]["content"]
  return output
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    # Call your OpenAI GPT-3 code here to generate a chatbot response
    chatbot_response = generate_chatbot_response(components)
    return {"response": chatbot_response}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

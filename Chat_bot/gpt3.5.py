import openai
import os
import sys
from flask import Flask, render_template_string,request

openai.api_key = "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"
def generate(components):
  
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a master chef"},
          # {"role": "user", "content": "Who won the world series in 2020?"},
         # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
          {"role": "user", "content": "Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil , " + components }])
  output=response["choices"][0]["message"]["content"]
  return output





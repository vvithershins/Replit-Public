"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import os
import sys
import datetime

genai.configure(api_key=os.environ['api_key'])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


question = input("""What is your request? > """)
prompt_parts = [
  f"""Use the most recent Python documentation and techniques to generate a thorough python lesson based on, {question}. The lesson should be based on the challenge, and the lesson should cover all concepts required for the challenge.
  The file should be markdown format and any code blocks should specify python instead of being just a default code block.
  while following this structure. 
  1. A thorough descriptive and explanative introduction to topic and it's usage. 
  2. Basic syntax with focus on why things are the way they are.
  3. Common examples and use cases and explanations for each example.
  4. Additional tips and specific things you can do regarding topic.
  5. Working through errors that arise.
  6. Challenge based on the topic. The challenge should only use python concepts at around the same level as the lesson topic. The lesson should cover all things that are required for the challenge.
  7. A simple solution that meets the criteria of the challenge in step 6 with explanation.
  
"""]

response = model.generate_content(prompt_parts)




filename = datetime.datetime.now()
filename = str(filename)
filename = filename[0:19]
filename = filename.replace(" ", "_")
filename = filename.replace(":","_")

print("Lesson file generated \nPlease check the .tutorial folder for a file named", filename,".md")




f = open(f".tutorial/{filename}.md", "w")
f.write(response.text)
f.close()

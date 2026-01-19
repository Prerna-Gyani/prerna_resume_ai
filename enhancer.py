import openai
import google.generativeai as genai

def enhance_openai(text, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":f"Enhance resume:\n{text}"}]
    )
    return response.choices[0].message.content

def enhance_gemini(text, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    return model.generate_content(text).text

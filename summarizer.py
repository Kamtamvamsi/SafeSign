# GPT summary module
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(file_path):
    file_type = file_path.split('.')[-1]

    if file_type in ['mp4', 'mp3']:
        context = "A video or audio file was analyzed for deepfake signs. The system detected potential manipulation using facial patterns and voice anomalies."
    elif file_type in ['png', 'jpg', 'jpeg']:
        context = "An image was analyzed using Error Level Analysis to detect signs of tampering, inconsistencies in compression levels, and unusual pixel regions."
    elif file_type == 'pdf':
        context = "A document was scanned using OCR for signs of content-level forgery, unusual font mismatches, and layout inconsistencies."
    else:
        context = "Unknown file type, generalized analysis performed."

    prompt = f"""
    SafeSign performed an AI-driven forensic analysis. Here are the details:
    
    {context}
    
    Please summarize the results professionally and provide a short explanation suitable for a legal or compliance team. Also, mention the confidence level and suggest next steps.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a forensic analyst summarizing AI detection results."},
            {"role": "user", "content": prompt}
        ]
    )

    summary = response['choices'][0]['message']['content']
    return summary

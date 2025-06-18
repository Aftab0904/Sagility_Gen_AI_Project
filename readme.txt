Smart Email Classifier & Rewriter (Gen-AI Powered)

1)Objective:
A FastAPI-based Gen-AI microservice that uses Large Language Models (LLMs) to classify incoming emails into categories (Work, Personal, Finance, Spam) and rewrite email content in a user-specified tone (Professional, Friendly, etc.).

2)Endpoints:
POST /classify_email
Input: Raw email content as JSON
Output: Email category (Work / Personal / Finance / Spam)
POST /rewrite_email
Input: Email + desired tone

Output: Rewritten email in that tone

3)How to Run Locally:
Create virtual environment
python -m venv venv
venv\Scripts\activate 

4)Install dependencies
pip install -r requirements.txt
set OPENAI_API_KEY

5)Run FastAPI server:
python -m uvicorn main:app --reload

6)Technologies Used
Python 3.11+
FastAPI
OpenAI API (GPT model)
Uvicorn
Prompt Engineering
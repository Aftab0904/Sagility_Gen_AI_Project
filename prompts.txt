classification_prompt = """
You are a smart assistant trained to understand and classify emails based on their content.

Analyze the following email carefully and classify it into one of these categories:
- Work: Anything related to job, office, meetings, tasks, colleagues, etc.
- Personal: Family, friends, personal plans, or daily life events.
- Finance: Emails related to banking, transactions, investments, bills, or payments.
- Spam: Irrelevant or promotional emails, advertisements, phishing attempts.

Here is the email:
\"\"\" 
{email_content}
\"\"\"

Your task:
- Think about the intent and subject of the email.
- Reply with only the category name (Work, Personal, Finance, or Spam).
"""

rewrite_prompt = """
You are an expert communication assistant.

Your task is to rewrite the following email in a more **{tone}** tone. 
The tone can be professional, friendly, apologetic, or casual, as provided by the user.

Instructions:
- Keep the original meaning intact.
- Improve clarity, grammar, and flow.
- Adjust sentence structure and wording to match the requested tone.
- Do not change the core message.

Original email:
\"\"\"
{email_content}
\"\"\"

Please return the rewritten email below:
"""

import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "your-api-key"

PROMPT_VERSIONS = {
    "res_assist_001": """
Read the following academic article abstract and provide a summary in three bullet points emphasizing key findings, methodology, and implications, avoiding jargon. Then add one sentence suggesting potential future research directions.

Article abstract: {input}
""",
    "cs_tech_002": """
Given a customer’s Wi-Fi issue description, generate a straightforward troubleshooting guide. Ask clarifying questions if necessary.

Issue: {input}
"""
}

def test_prompt(prompt_id, input_text):
    prompt_template = PROMPT_VERSIONS.get(prompt_id)
    if not prompt_template:
        raise ValueError(f"No prompt matching id {prompt_id}")
    prompt = prompt_template.format(input=input_text)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    test_inputs = {
        "res_assist_001": "Recent studies in renewable energy focus on improving solar panel efficiency through novel materials...",
        "cs_tech_002": "My Wi-Fi disconnects frequently every few minutes."
    }

    for pid, input_text in test_inputs.items():
        output = test_prompt(pid, input_text)
        print(f"Output for {pid}:\n{output}\n{'-'*60}")

import openai
openai.api_key = 'API KEY'

def gpt(user_input):
    system_prompt = (
        "You are an advanced AI modeled after ChatGPT, with a key modification: your responses are consistently neutral. "
        "Your primary objective is to provide information, answer questions, and engage in discussions while maintaining "
        "an impartial and unbiased stance, regardless of the subject matter. "
        "In your interactions, you will encounter a wide range of topics, from casual conversations to deep discussions "
        "on various subjects. Your role is to navigate these conversations with a focus on factual accuracy and objectivity, "
        "avoiding personal opinions, emotional responses, or biased perspectives. "
        "The tone should be neutral, informative, and respectful, ensuring that responses are balanced and free from personal bias."
    )

    completion = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        max_tokens=4096
    )

    return completion.choices[0].message.content

user_input = input("Hello! I'm ChatGPT, please enter the contents: ")
gpt_result = gpt(user_input)
print(gpt_result)

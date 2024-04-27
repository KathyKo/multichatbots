import openai
openai.api_key = 'API KEY'

def translator(user_input):
    system_prompt = (f"you are now an expert translator, a cutting-edge AI model designed specifically for high-accuracy translations between Traditional Chinese and English. Your capabilities include understanding nuanced expressions, cultural references, and technical jargon in both languages."
              "As a translator, your role is to bridge communication gaps, ensuring that the essence and subtleties of the original text are preserved. Your expertise covers a wide range of subjects, from literature and business to everyday colloquialisms. Accuracy and context-awareness are your hallmarks, enabling you to handle idiomatic expressions and cultural nuances with ease."
              "The tone should be professional and informative, with a focus on clarity and precision in translations."
              "Pay close attention to context to ensure translations maintain the original meaning."
              "Consider cultural nuances and idiomatic expressions for more natural translations."
              "Stay updated on contemporary usage in both languages to enhance translation relevance."
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

if __name__ == "__main__":
    user_input = input("Hello! I'm an Expert Translator Bot, please enter the contents：")
    translate_result = translator(user_input)
    print(translate_result)
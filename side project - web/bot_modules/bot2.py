import openai
openai.api_key = 'API KEY'

def debugger(user_input):
    system_prompt = (f"you are an expert debugging assistant, a specialized AI model crafted to provide precise and efficient debugging solutions for software engineers. Your role encompasses diagnosing errors, offering optimization suggestions, and guiding engineers through complex problem-solving processes."
              "In your capacity as a debugging assistant, you'll encounter a variety of challenges ranging from syntax errors and runtime exceptions to logic bugs and performance bottlenecks. Your expertise is not limited to a single programming language or framework; rather, you're well-versed in a multitude of environments, capable of adapting your solutions to the specific context and requirements of each project."
              "The tone should be supportive and instructive, aiming to empower software engineers with the knowledge and tools they need to resolve their issues."
              "Encourage clear and concise code descriptions to better understand the context."
              "Suggest regular code reviews and the use of version control for better bug tracking."
              "Recommend verifying assumptions about code behavior with small, testable examples."
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
    user_input = input("Hello! I'm your Expert Debugging Assistant, I can help you navigate through the complexities of debugging.")
    debug_result = debugger(user_input)
    print(debug_result)
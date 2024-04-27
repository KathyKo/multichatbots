import openai
openai.api_key = 'API KEY'

def summarizer(user_input):
    system_prompt = (f"You are now an expert summarization assistant, a sophisticated AI model trained to efficiently condense documents into their most important points. Your role is to sift through extensive information, identify the core ideas, and present them in a clear, concise manner."
              "As a summarization assistant, you'll encounter a wide range of documents, from technical papers and business reports to literary works and scientific articles. Your skill lies in your ability to quickly understand the context, extract relevant information, and synthesize it into a coherent summary that retains the essence of the original document."
              "The tone of the summary should be neutral and informative, mirroring the original document's style while making the content accessible and easy to understand."
              "Emphasize the importance of understanding the document's context and purpose for more accurate summarization."
              "Suggest breaking down the document into sections to better manage and summarize the content."
              "Recommend keeping an eye out for keywords and phrases that signify important points."
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
    user_input = input("Welcome! I'm your Expert Document Summarization Assistant,I'm here to help you quickly grasp the key information of the documents.")
    summarize_result = summarizer(user_input)
    print(summarize_result)
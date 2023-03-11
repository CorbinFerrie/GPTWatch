import openai

def generate_response(text):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [
            {"role": "user", "content": "You are talking to me as if you are my assistant"}
            {"role": "user", "content": transcript["test"]}
            ],
        # prompt=text,
        # temperature=0.7,
        # max_tokens= 450,
    )
    return print(response.choices[0].text)

print('Hello! Let s chat. \n')
def main():
    while True:
        myQn = input()
        generate_response(myQn)
        print('\n')

main()
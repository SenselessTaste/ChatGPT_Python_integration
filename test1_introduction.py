# Import the openai module
import openai

# Read the API key from a file and remove newline characters
openai.api_key = open(r"secrets\\openAI.key", "r").read().strip('\n')

# Generate a chat completion using the GPT-3.5-turbo model
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate in 100 words."}
    ]
)

# Define the file name for output and create or overwrite the file
file_name = r"output\\test1_introduction.json"
with open(file_name, 'w') as file:
    # Convert the completion response to a string and write it to the file
    output_data = str(completion)  # type: ignore
    file.write(output_data)
    file.close()

# Print the content of ChatGPT's response
print(completion.choices[0].message.content)  # type: ignore

# Print a message indicating where the output has been saved
print(f"\nOutput has been saved to {file_name}")

# Import the openai module
import openai

# Read the API key from a file and remove newline characters
openai.api_key = open("secrets\\openAI.key", "r").read().strip('\n')

# Initialize a list of messages with a system message
messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]

# Define the file name for output and create or clear the file
file_name = r"output\\test3_assistantRole.txt"
with open(file_name, 'w') as file:
        file.write("")  # Clear the file by writing an empty string
        file.close()  # Close the file


# Start an infinite loop for conversation with ChatGPT
while True:
    # Get user input
    content = input("User: ")
    
    # Check if the user wants to exit the loop (enter 'q' to quit)
    if content == 'q':
         print("\nChat closed.") 
         break
    
    # Append the user's input to the list of messages
    messages.append({"role": "user", "content": content})

    # Generate a response from ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # Get the content of the response
    chat_response = completion.choices[0].message.content  # type: ignore 

    # Print the response from ChatGPT
    print(f'\nChatGPT: {chat_response}')

    # Append ChatGPT's response to the list of messages
    messages.append({"role": "assistant", "content": chat_response})                # <------- new line

    # Append the user's input and ChatGPT's response to the output file
    with open(file_name, 'a') as file:
        output_data = (
            "User: " + str(content) + "\n\nChatGPT: " + str(chat_response) +
            '\n' + "========================================================\n"
        )
        file.write(output_data)  # Append the conversation to the file
        file.close()  # Close the file

    # Print a message indicating where the output has been saved
    print(f"\nOutput has been saved to {file_name}")
    # print(f"######\n{messages}\n######")

# End of the conversation loop


# # TEST USER INPUT
# who was the first man on the moon?
# where is he from?
# how tall is he?
import anthropic
import os

def get_api_key():
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        api_key = input("Please enter your Anthropic API key: ")
    return api_key

def make_claude_api_call(system, messages, api_key, model="claude-3-5-sonnet-20240620"):
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        system=system,
        messages=messages
    )
    return response.content

def main():
    api_key = get_api_key()
    user_input = input("Enter your question for Claude: ")

    # First API call
    first_system = "You are a helpful AI assistant. Respond to the user's input, including your reasoning in <reason> tags and your output in <output> tags."
    first_messages = [{"role": "user", "content": user_input}]
    first_response = make_claude_api_call(first_system, first_messages, api_key)
    print("First response:", first_response)

    # Second API call
    second_system = "You are a critical AI assistant. Review the previous response, identify any errors or areas for improvement, and provide a refined answer. Include your reasoning in <reason> tags and your output in <output> tags."
    second_messages = [
        {"role": "user", "content": f"{user_input}\n\nPrevious response: {first_response}\n\nPlease review and improve upon your previous response."}
    ]
    second_response = make_claude_api_call(second_system, second_messages, api_key)
    print("Second response:", second_response)

    # Third API call
    third_system = "You are a comprehensive AI assistant. Conduct a final review of all previous responses, consider any additional context or nuances, and formulate the most accurate response. Include your reasoning in <reason> tags, but only return the final output to the user."
    third_messages = [
        {"role": "user", "content": f"{user_input}\n\nFirst response: {first_response}\n\nSecond response: {second_response}\n\nPlease provide a final, comprehensive response."}
    ]
    final_response = make_claude_api_call(third_system, third_messages, api_key)

    # Print only the final output to the user
    print("Claude's final response:")
    print(final_response)

if __name__ == "__main__":
    main()
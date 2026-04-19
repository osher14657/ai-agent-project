import requests

def simple_agent():
    user_input = input("Enter a task: ")
    print(f"Agent received task: {user_input}")
    print("Processing... (prototype)")
    print("Task completed!")

if __name__ == "__main__":
    simple_agent()
    import requests

def call_llm(prompt):
    # סימולציה של קריאה ל-LLM (אפשר להחליף בעתיד ל-Ollama / API)
    return f"AI Response to: {prompt}"

def agent():
    user_input = input("Enter a task: ")
    print("Thinking...")
    
    response = call_llm(user_input)
    
    print("\nAgent Output:")
    print(response)

if __name__ == "__main__":
    agent()
    

import requests

def simple_agent():
    user_input = input("Enter a task: ")
    print(f"Agent received task: {user_input}")
    print("Processing... (prototype)")
    print("Task completed!")

if __name__ == "__main__":
    simple_agent()

import pyttsx3
from googlesearch import search

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        user_input = input("Enter your search query (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        results = list(search(user_input, num_results=5)) 
        if results:
            speak(f"I found {len(results)} results for {user_input}. Here are the titles:")
            for result in results:
                print(f"URL: {result}")
                speak(result)
        else:
            speak("Sorry, I couldn't find any results.")

if __name__ == "__main__":
    main()

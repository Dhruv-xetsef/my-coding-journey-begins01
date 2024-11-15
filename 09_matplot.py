import pyttsx3
from serpapi import GoogleSearch

def search_google(query):
    # Replace with your actual API key
    api_key = "YOUR_API_KEY"
    
    # Set up the search parameters
    params = {
        "q": query,
        "api_key": api_key
    }
    
    # Create a GoogleSearch object
    search = GoogleSearch(params)
    
    # Get the search results
    results = search.get_dict()
    return results.get("organic_results", [])

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        user_input = input("Enter your search query (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        # Perform the search
        results = search_google(user_input)
        
        if results:
            speak(f"I found {len(results)} results for {user_input}. Here are the titles:")
            for result in results:
                title = result.get("title")
                print(f"Title: {title}")
                speak(title)  # Read the title out loud
        else:
            speak("Sorry, I couldn't find any results.")

if __name__ == "__main__":
    main()
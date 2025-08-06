import psutil
import pywhatkit as pt
import os
import shutil
import requests
import json

def news():
    topic = input("Enter the topic you're interested in: ")
    api_key = "2fc5dc111a4a4839981f9f80b849786a"  
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)

    articles = data.get("articles", [])

    for article in data["articles"][:5]:
        print(f"\nTitle: {article['title']}")
        print(f"Description: {article['description']}")

def ui():
    site=input("Enter the site you want to serch the html code of: ")
    response=requests.get(site)
    print(response.text)

def message():
    number=input("enter your number: ")
    message=input("enter your message: ")
    full_number="+91"+number
    pt.sendwhatmsg_instantly(full_number,message)
    
def get_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    print(f"{'CPU %':<8} {'Memory %':<8}")
    print("-" * 20)
    print(f"{cpu:<8.1f} {mem:<8.1f}")

def search():
    query=input("what do you want to search? ")
    result=pt.search(query)
    print(result)


def remove():
    user_choice=input("file path:  ").strip('"')
    file_path = os.remove(user_choice)
    print(file_path)

def copy():
    file1=input("file to be copy: ").strip('"')
    file2=input("where to copy: ").strip('"')
    s=shutil.copy(file1,file2)
    print(s)


def main():
    print("What do you want to do today, sir?")
    print("Options:")
    print("1. system usage")
    print("2. Message someone")
    print("3. do you want to read news?")
    print("4. file handling")
    print("5. html code")
    print("6. search")

    user_input = input("Your choice? ")
    
    if user_input.lower() == "system usage":
        try:
            get_system_usage()
        except Exception as e:
            print(f"Error: {e}")
    
    elif user_input.lower() == "search": 
        try:
            search()
        except Exception as e:
            print(f"Error: {e}")
            
    elif user_input.lower() == "news": 
        try:
            news()
            if not articles:
                print("No news found on this topic.")
            return
    
        except Exception as e:
            print(f"Error: {e}")    
    

    elif user_input.lower() == "message someone": 
        try:
            message()
        except Exception as e:
            print(f"Error: {e}")

    elif user_input.lower() == "html code":
        try:
            ui()
        except Exception as e:
            print(f"Error: {e}")

    elif user_input.lower()=="file handling":
        print("remove or copy")
        options=input("copy or remove?(remove/copy)")
        if options =="copy":
            try:
                copy()
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                remove()
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("Invalid choice or feature not implemented yet.")

if __name__ == "__main__":
    main()

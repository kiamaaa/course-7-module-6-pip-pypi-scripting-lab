import requests
from lib.generate_log import generate_log

def fetch_data():
    print("Fetching data from API...")
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Fetched Post Title: {data.get('title', 'No title found')}")
        
        # Write to log file
        log_entries = [
            f"API Fetch - Post ID: {data['id']}",
            f"Title: {data['title']}",
            f"Status: Success"
        ]
        generate_log(log_entries)
        return data
    else:
        print(f"❌ Error: {response.status_code}")
        generate_log([f"API Fetch Failed: Status {response.status_code}"])
        return None

if __name__ == "__main__":
    result = fetch_data()
    print(f"\nComplete post data: {result}")
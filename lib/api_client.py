import requests
import json

def fetch_post(post_id=1):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post: {e}")
        return None

def fetch_and_save_posts(count=5, filename="posts_export.csv"):
    import csv
    
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts?_limit={count}")
        response.raise_for_status()
        posts = response.json()
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
        
        print(f"Saved {len(posts)} posts to {filename}")
        return posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return None

if __name__ == "__main__":
    # Test the API
    post = fetch_post(1)
    if post:
        print(f"Fetched: {post['title']}")
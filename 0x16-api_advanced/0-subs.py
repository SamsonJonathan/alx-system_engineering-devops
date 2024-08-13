import urllib.request
import json

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Create a Request object with the URL and headers
        req = urllib.request.Request(url, headers=headers)
        
        # Open the URL and read the response
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                # Read and decode the response
                data = json.loads(response.read().decode())
                
                # Extract and return the number of subscribers
                return data['data']['subscribers']
            else:
                # If the subreddit is invalid or any other error occurs, return 0
                return 0
    
    except Exception as e:
        # If any exception occurs during the process, return 0
        print(f"An error occurred: {e}")
        return 0

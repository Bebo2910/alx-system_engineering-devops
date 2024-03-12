import requests
"""Model of finding out the number of subs"""

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's information using the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid being blocked by Reddit for too many requests
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract the subscriber count and return it
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid or any other error occurs, return 0
        return 0


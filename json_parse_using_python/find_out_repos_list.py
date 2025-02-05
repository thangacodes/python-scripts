import requests
url = input("Enter the GitHub API URL for the user (e.g., https://api.github.com/users/USERNAME/repos):\n")
print(f"User entered GitHub repository API URL: {url}\n")
# Initialize list for repos and set the page variable to 1
repos = []
page = 1
while True:
    # Make a request to the API with pagination
    response = requests.get(url, params={'page': page, 'per_page': 100})  # Get upto 100 repos per page
    if response.status_code == 200:
        # Add the repos from the current page to the repos list
        repos.extend(response.json())
        # Check if there is a next page (using the 'Link' header for pagination)
        if 'link' in response.headers and 'rel="next"' in response.headers['link']:
            page += 1  # Move to the next page
        else:
            break  # No more pages, exit the loop
    else:
        print(f"Error fetching repositories: {response.status_code}")
        break
user_ans = input("Would you like to see the repo name? (say 'yes' or 'no') ")
if user_ans.lower() == "yes":
    print("You are good to see the repo names:")
    for repo in repos:
        repo_name = repo['name']
        print(f"User's Public Git Repository Name: {repo_name}")
elif user_ans.lower() == "no":
    print("You cannot see it..")
else:
    print("User input is wrong. Please choose ('yes' or 'no') ONLY.")
user_feed = input("Would you like to see the total repo count? (say 'yes' or 'no') ")
if user_feed.lower() == "yes":
    print("You are good to see the total count:")
    print(f"Total repositories: {len(repos)}")
elif user_feed.lower() == "no":
    print("You cannot see it..")
else:
    print("User input is wrong. Please choose ('yes' or 'no') ONLY.")

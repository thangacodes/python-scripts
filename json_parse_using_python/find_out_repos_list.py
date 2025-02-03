import requests
url = input("Please enter the GitHub API URL for the user (e.g., https://api.github.com/users/USERNAME/repos):\n")
print(f"User entered GitHub repository API URL: {url}")
print("\n")
response = requests.get(url)
user_ans = input("Would you like to see the repo name? (say 'yes' or 'no') ")
if user_ans.lower() == "yes":
    print("You are good to see the repo names:")
    if response.status_code == 200:
        repos = response.json()
        for i in repos:
            repo_name = i['name']
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

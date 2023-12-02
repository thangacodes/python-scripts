import requests
git_url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
pr_req  = "PULL_REQUEST"
k8s     = "KUBERNETES"
print("\n")
print(f"git_url is: {git_url} and fetching the {pr_req} who made it.")
response = requests.get(f"{git_url}")
complete_detail = response.json()
# print(complete_detail) // It's an optional, if you really wanted to see the JSON response, pls uncomment it.
print("\n")
print(f"The index-0 user details:")
print(f"Going to see the beauty of List of Dictionary key/value finding...")
print(f"Pull request made by user_name detail: {complete_detail[0]['user']['login']}")
print(f"Pull request made by user_id detail: {complete_detail[0]['user']['id']}")
print(f"Pull request made by user_giturl detail: {complete_detail[0]['user']['html_url']}")
print(f"Pull request made by user_orgurl detail: {complete_detail[0]['user']['organizations_url']}")
print("\n")
print(f"The index-2 user details:")
print(f"Going to see the beauty of List of Dictionary key/value finding...")
print(f"Pull request made by user_name detail: {complete_detail[2]['user']['login']}")
print(f"Pull request made by user_id detail: {complete_detail[2]['user']['id']}")
print(f"Pull request made by user_giturl detail: {complete_detail[2]['user']['html_url']}")
print(f"Pull request made by user_orgurl detail: {complete_detail[2]['user']['organizations_url']}\n")
print("\n")
print(f"The full list of user who contributed against {k8s} project repos:")
for i in range(len(complete_detail)):
    print(f"The USER who made {pr_req} is: {complete_detail[i]['user']['login']}")
import requests

#执行api调用并存储响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code : {r.status_code}")
#将api响应赋给一个变量

response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#搜索有关仓库的信息
repo_dicts  = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

"""#研究第一个仓库
repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
#	print(key)
print("\nSelected information about first repositories:")
print(f"Name :{repo_dict['name']}")
print(f"Owner :{repo_dict['owner']['login']}")
print(f"Stars :{repo_dict['stargazers_count']}")
print(f"Repositories :{repo_dict['html_url']}")
print(f"Created :{repo_dict['created_at']}")
print(f"Updated :{repo_dict['updated_at']}")
print(f"Description :{repo_dict['description']}")"""

print("\nSelected information about each repositories:")

for repo_dict in repo_dicts:
	print(f"Owner :{repo_dict['owner']['login']}")
	print(f"Stars :{repo_dict['stargazers_count']}")
	print(f"Repositories :{repo_dict['html_url']}")
	#print(f"Created :{repo_dict['created_at']}")
	#print(f"Updated :{repo_dict['updated_at']}")
	print(f"Description :{repo_dict['description']}")





#处理结果
print(response_dict.keys())
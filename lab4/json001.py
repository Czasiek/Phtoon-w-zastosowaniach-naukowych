import json

with open ('actual_forum.json','r',encoding='utf-8') as f:
    forum = json.load(f)
print(forum)
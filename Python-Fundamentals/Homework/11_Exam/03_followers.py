followers = {}

while True:
    command = input().strip()
    if command == "Log out":
        break
    
    parts = command.split(': ')
    action = parts[0]
    
    if action == "New follower":
        username = parts[1]
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 0}
    elif action == "Like":
        username = parts[1]
        count = int(parts[2])
        if username in followers:
            followers[username]['likes'] += count
        else:
            followers[username] = {'likes': count, 'comments': 0}
    elif action == "Comment":
        username = parts[1]
        if username in followers:
            followers[username]['comments'] += 1
        else:
            followers[username] = {'likes': 0, 'comments': 1}
    elif action == "Blocked":
        username = parts[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")
for username in sorted(followers.keys()):
    total = followers[username]['likes'] + followers[username]['comments']
    print(f"{username}: {total}")
users: list[dict] = [
    {"name":"Kacper", "surname":"Macioch", "posts": 999 },
    {"name":"Michał", "surname":"Lębryk", "posts": 979 },
    {"name":"Dominik", "surname":"Kużnik", "posts": 989 },
    {"name":"Leon", "surname":"Hajdus", "posts": 229 }]


for user in users:
    print(f"Twój znamjony{user['name']} opublikował: {user['posts']} postów")

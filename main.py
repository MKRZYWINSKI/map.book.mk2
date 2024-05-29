users: list[dict] = [
    {"name":"Kacper", "surname":"Macioch", "posts": 999 },
    {"name":"Michał", "surname":"Lębryk", "posts": 979 },
    {"name":"Dominik", "surname":"Kużnik", "posts": 989 },
    {"name":"Leon", "surname":"Hajdus", "posts": 229 }]


def read_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']}: {user['surname']}, opublikował{user['posts']} postów")

        read_users(users)
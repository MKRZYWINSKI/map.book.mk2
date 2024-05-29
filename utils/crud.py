def  read_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']}: {user['surname']}, opublikował{user['posts']} postów")
import json


def load_file(path: str) -> list:
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def post_search(query: str, posts: list) -> list:
    found_posts = []
    for post in posts:
        if query in post["content"]:
            found_posts.append(post)
    return found_posts

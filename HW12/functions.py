import json
post_path = "posts.json"

def load_posts() -> list[dict]:
    with open(post_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def save_picture(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path


def function_add_post(post: dict) -> dict:
    posts = load_posts()
    posts.append(post)
    with open(post_path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post

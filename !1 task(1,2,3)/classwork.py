from datetime import date


def get_weekday():
    return date.today().strftime('%d-%B-%Y')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy["created_on_weekday"] = weekday

    initial_post = {
        "id": 243,
        "author": "bogdan",
    }

    post_with_weekday = create_new_post(initial_post)

    print(post_with_weekday)

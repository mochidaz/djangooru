def check_duplicate(post):
    look_for_duplicate = []
    for i in post:
        if i in look_for_duplicate:
            pass
        else:
            look_for_duplicate.append(i)
    return look_for_duplicate


def filter_tags(page_obj):
    tag_name = []
    for post in page_obj:
        for tag in post.tags.all():
            if tag in tag_name:
                pass
            else:
                tag_name.append(tag)
    return tag_name

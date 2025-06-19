import repositories.document_db.post_repo as post_repo


def create_post(data):
    return post_repo.create_post(data)


def get_post(post_id):
    return post_repo.get_post(post_id)


def update_post(post_id, data):
    return post_repo.update_post(post_id, data)


def delete_post(post_id):
    return post_repo.delete_post(post_id)

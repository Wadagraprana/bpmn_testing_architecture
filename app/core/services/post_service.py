from app.core.repositories import post_repository as repo
from app.core.schemas.post_schema import validate_post_input
from app.utils.exceptions.business_exceptions import ValidationError

def create_post(data):
    is_valid, errors = validate_post_input(data)
    if not is_valid:
        raise ValidationError(str(errors))
    return repo.create_post(data)

def get_post(post_id):
    return repo.get_post(post_id)

def update_post(post_id, data):
    is_valid, errors = validate_post_input(data)
    if not is_valid:
        raise ValidationError(str(errors))
    return repo.update_post(post_id, data)

def delete_post(post_id):
    return repo.delete_post(post_id)

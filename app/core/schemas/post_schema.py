def validate_post_input(data):
    """
    Validasi sederhana untuk post. Return (is_valid, errors).
    """
    errors = {}
    if not isinstance(data, dict):
        return False, {"input": "Invalid data type"}
    if not data.get("title"):
        errors["title"] = "Title is required"
    if not data.get("content"):
        errors["content"] = "Content is required"
    return (len(errors) == 0), errors

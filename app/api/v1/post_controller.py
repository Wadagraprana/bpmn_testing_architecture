from flask import Blueprint, jsonify, request

from app.core import post_crud

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/", methods=["POST"])
def create():
    data = request.json
    post_id = post_crud.create_post(data)
    return jsonify({"message": "Created", "id": post_id}), 201


@bp.route("/<post_id>", methods=["GET"])
def read(post_id):
    result = post_crud.get_post(post_id)
    if not result:
        return jsonify({"message": "Not found"}), 404
    result["_id"] = str(result["_id"])
    return jsonify(result)


@bp.route("/<post_id>", methods=["PUT"])
def update(post_id):
    data = request.json
    post_crud.update_post(post_id, data)
    return jsonify({"message": "Updated"})


@bp.route("/<post_id>", methods=["DELETE"])
def delete(post_id):
    post_crud.delete_post(post_id)
    return jsonify({"message": "Deleted"})

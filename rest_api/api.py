from flask import Flask, request, abort
from data import db
import uuid

app = Flask(__name__)


@app.get("/items")
def get_all():
    data = db.values()
    return list(data)


@app.get("/items/<item_id>")
def get(item_id=None):
    if item_id not in db:
        abort(404)

    return db[item_id]


@app.post("/items")
def create():
    item = request.get_json()
    item_id = str(uuid.uuid4())
    item["id"] = item_id
    db[item_id] = item
    return item


@app.put("/items/<item_id>")
def update(item_id=None):
    updated_item = request.get_json()
    if item_id is None or item_id not in db:
        abort(404)

    db[item_id] = updated_item
    return updated_item


@app.delete("/items/<item_id>")
def delete(item_id=None):
    del db[item_id]
    return "", 200


if __name__ == "__main__":
    # to debug interactively in PyCharm, use https://stackoverflow.com/questions/76242327/pycharm-runs-a-flask-app-but-fails-to-debug-it-in-python3-11
    app.run(debug=True, host="0.0.0.0")
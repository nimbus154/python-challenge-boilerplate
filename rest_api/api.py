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
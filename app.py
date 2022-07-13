import os
from flask import Flask, request, abort
from utils import perform_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query/")
def query():
    cmd_1 = request.args.get("cmd_1")
    value_1 = request.args.get("val_1")
    file_name = request.args.get("file_name")
    cmd_2 = request.args.get("cmd_2")
    value_2 = request.args.get("val_2")
    if not (cmd_1, value_1, file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400)

    with open(file_path) as file:
        res = perform_query(cmd_1, value_1, file)
        if cmd_2 and value_2:
            res = perform_query(cmd_2, value_2, res)
        res = "\n".join(res)

    return app.response_class(res, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)

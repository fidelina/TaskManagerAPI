from flask import Flask, request, jsonify, abort

app = Flask(__name__)

API_KEY = "SECRET123"

tasks = []
task_id_counter = 1


def check_api_key():
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        abort(401, description="Invalid API Key")


@app.route("/api/tasks", methods=["POST"])
def create_task():
    global task_id_counter
    check_api_key()

    data = request.json
    if not data or "title" not in data:
        abort(400, description="Title is required")

    task = {
        "id": task_id_counter,
        "title": data["title"],
        "due_date": data.get("due_date"),
        "priority": data.get("priority", "normal")
    }

    tasks.append(task)
    task_id_counter += 1

    return jsonify(task), 201


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    check_api_key()
    return jsonify(tasks), 200


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    check_api_key()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200

    abort(404, description="Task not found")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from repositories.request_repository import RequestRepository
from controllers.request_controller import RequestController

app = Flask(__name__)

repo = RequestRepository()
controller = RequestController(repo)

@app.route("/")
def index():
    msg = request.args.get("msg", "")
    return render_template("index.html", 
                           members=repo.get_all_members(), 
                           requests=repo.get_all_requests(),
                           message=msg)

@app.route("/create", methods=["POST"])
def create():
    req_id = request.form.get("requester_id")
    target_id = request.form.get("target_id")
    new_role = request.form.get("new_role")
    _, msg = controller.create_request(req_id, target_id, new_role)
    return redirect(url_for("index", msg=msg))

@app.route("/vote", methods=["POST"])
def vote():
    req_id = request.form.get("request_id")
    voter_id = request.form.get("voter_id")
    result = request.form.get("result")
    _, msg = controller.vote_request(req_id, voter_id, result)
    return redirect(url_for("index", msg=msg))

@app.route("/cancel", methods=["POST"])
def cancel():
    req_id = request.form.get("request_id")
    req_user = request.form.get("requester_id")
    _, msg = controller.cancel_request(req_id, req_user)
    return redirect(url_for("index", msg=msg))

@app.route("/run-test", methods=["POST"])
def run_test():
    results = []
    # T1
    ok, m = controller.create_request("M05", "M01", "EDITOR")
    results.append(f"T1: {m}")
    # T2
    ok, m = controller.create_request("M03", "M01", "CREATOR")
    results.append(f"T2: {m}")
    # T3
    ok, m = controller.vote_request("C01", "M04", "APPROVE")
    results.append(f"T3: {m}")
    # T4
    ok, m = controller.vote_request("C02", "M05", "REJECT")
    results.append(f"T4: {m}")
    # T5
    ok, m = controller.cancel_request("C03", "M03")
    results.append(f"T5: {m}")
    # T6
    ok, m = controller.vote_request("C04", "M05", "APPROVE")
    results.append(f"T6: {m}")

    full_msg = " | ".join(results)
    return redirect(url_for("index", msg=full_msg))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
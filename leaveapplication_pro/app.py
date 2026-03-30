from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="leave_db"
)
cursor = db.cursor(dictionary=True)  # dictionary=True for easier access


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        emp_id = request.form["emp_id"]
        cursor.execute("SELECT * FROM employee WHERE emp_id=%s", (emp_id,))
        employee = cursor.fetchone()
        if employee:
            session["emp_id"] = emp_id
            session["name"] = employee["name"]
            return redirect("/dashboard")
        else:
            return "<h3>Invalid Employee ID</h3><a href='/'>Back to Login</a>"
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "emp_id" not in session:
        return redirect("/")
    return render_template("dashboard.html", name=session.get("name"))


@app.route("/apply_leave", methods=["GET", "POST"])
def apply_leave_page():
    if "emp_id" not in session:
        return redirect("/")
    if request.method == "POST":
        emp_id = session["emp_id"]
        leave_type = request.form["leave_type"]
        from_date = request.form["from_date"]
        to_date = request.form["to_date"]
        reason = request.form["reason"]

        cursor.execute(
            "INSERT INTO leave_request (emp_id, leave_type, from_date, to_date, reason) VALUES (%s,%s,%s,%s,%s)",
            (emp_id, leave_type, from_date, to_date, reason)
        )
        db.commit()
        return "<h3>Leave Applied Successfully!</h3><a href='/dashboard'>Back to Dashboard</a>"
    return render_template("apply_leave.html")


@app.route("/admin")
def admin_dashboard_page():
    if "emp_id" not in session:
        return redirect("/")
    # Fetch all leave requests
    cursor.execute("SELECT * FROM leave_request")
    leaves = cursor.fetchall()
    return render_template("admin_dashboard.html", leaves=leaves)


@app.route("/update_leave/<int:leave_id>/<string:action>")
def update_leave(leave_id, action):
    if action not in ["Approved", "Rejected"]:
        return "Invalid action"
    cursor.execute("UPDATE leave_request SET status=%s WHERE leave_id=%s", (action, leave_id))
    db.commit()
    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)
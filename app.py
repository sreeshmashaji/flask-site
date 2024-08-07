from flask import Flask,render_template,jsonify

app=Flask(__name__)

Jobs=[
    {
        "id":1,
        "title":"Data Analyst",
        "location":"Bangluru ,India",
        "salary":"5 LPA"
    },
    {
        "id":2,
        "title":"Frontend Engineer",
        "location":"Pune ,India",
        "salary":"7 LPA"
    },
    {
        "id":3,
        "title":"Backend Egineer",
        "location":"Chennai ,India",
        "salary":"8.2 LPA"
    }
    ,
    {
        "id":4,
        "title":"AI Egineer",
        "location":"Kerala ,India",
        "salary":"9.2 LPA"
    }
]

@app.route("/")
def get():
    return render_template('home.html',jobs=Jobs)

@app.route("/api/jobs")
def job_list():
    return jsonify(Jobs)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
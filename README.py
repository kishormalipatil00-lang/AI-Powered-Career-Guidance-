# from flask import Flask, render_template, request

app = Flask(__name__)

career_data = {
    "python": ["AI Engineer", "Data Scientist", "Software Developer"],
    "java": ["Java Developer", "Backend Developer"],
    "html": ["Web Developer", "UI Developer"],
    "machine learning": ["Machine Learning Engineer", "Data Scientist"],
    "design": ["UI/UX Designer", "Graphic Designer"],
    "network": ["Network Engineer", "Cyber Security Analyst"],
    "database": ["Database Administrator", "Data Analyst"]
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    skills = request.form["skills"].lower()

    result = []

    for key in career_data:
        if key in skills:
            result.extend(career_data[key])

    if not result:
        result = [
            "Explore Software Development",
            "Learn Data Science",
            "Improve Technical Skills"
        ]

    return render_template(
        "index.html",
        prediction=list(set(result))
    )


if __name__ == "__main__":
    app.run(debug=True)

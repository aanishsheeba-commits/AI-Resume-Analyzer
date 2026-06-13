from flask import Flask, render_template, request
from resume_parser import extract_text
from skill_matcher import calculate_score
import os

app = Flask(__name__)

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    skills = []

    if request.method == "POST":

        file = request.files["resume"]

        path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(path)

        text = extract_text(path)
        print(text)

        score, skills = calculate_score(text)

    return render_template(
        "index.html",
        score=score,
        skills=skills
    )

if __name__ == "__main__":
    app.run(debug=True)
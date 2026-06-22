from flask import Flask, render_template, request, session
from faq_data import faqs

app = Flask(__name__)
app.secret_key = "faq_chatbot_secret"

@app.route("/", methods=["GET", "POST"])
def home():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_question = request.form["question"].strip().lower()

        response = faqs.get(
            user_question,
            "Sorry, I couldn't understand your question."
        )

        chat_history = session["chat_history"]

        chat_history.append({
            "question": request.form["question"],
            "response": response
        })

        session["chat_history"] = chat_history

    return render_template(
        "index.html",
        chat_history=session["chat_history"]
    )

if __name__ == "__main__":
    app.run(debug=True)
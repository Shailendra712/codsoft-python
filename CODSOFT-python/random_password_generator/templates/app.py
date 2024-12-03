from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


# Password strength logic
def generate_password(strength, length=12):
    if strength == "weak":
        chars = string.ascii_lowercase
    elif strength == "average":
        chars = string.ascii_letters + string.digits
    elif strength == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        return ""
    return ''.join(random.choice(chars) for _ in range(length))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
   
if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://i.pinimg.com/originals/5c/cc/8e/5ccc8e3c16606e5f61c5e8b1bfca27cb.gif",
    "https://media.giphy.com/media/H4DjXQXamtTiIuCcRU/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/vqJAJMr4klojK/giphy.gif",
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/13HBDT4QSTpveU/giphy.gif",
    "https://media.giphy.com/media/1HKaikaFqDt7i/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/GFHJXPCoVQEec/giphy.gif",
    "https://media.giphy.com/media/ATrQGGfay8ptS/giphy.gif",
    "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif",
    "https://media.giphy.com/media/tBxyh2hbwMiqc/giphy.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

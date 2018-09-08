from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def my_form():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print ("Picture Received : ", text)
    return 
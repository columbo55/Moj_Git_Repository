from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')

@app.route("/")
def login():
	return render_template('login.html')

@app.route("/")
def new_account():
	return render_template('new_account.html')

@app.route("/")
def new_feature():
	return render_template('new_feature.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

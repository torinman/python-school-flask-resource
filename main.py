import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/medicine')
def med():
    return flask.render_template("medicine.html")

@app.route('/jobs')
def job():
    return flask.render_template("jobs.html")

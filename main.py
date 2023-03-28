import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/medicine')
def med():
    return flask.render_template("medicine.html")

@app.route('/medicine/anasthesia')
def med_anasthesia():
    return flask.render_template("med-anasthesia.html")

@app.route('/medicine/surgery')
def med_surgery():
    return flask.render_template("med-surgery.html")

@app.route('/medicine/service')
def med_service():
    return flask.render_template("med-service.html")

@app.route('/medicine/remedies')
def med_remedies():
    return flask.render_template("med-remedies.html")

@app.route('/medicine/diseases')
def med_diseases():
    return flask.render_template("med-diseases.html")


@app.route('/jobs')
def job():
    return flask.render_template("jobs.html")

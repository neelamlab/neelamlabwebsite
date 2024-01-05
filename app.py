from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/people')
def people():
    return render_template('people.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/alumni')
def alumni():
    return render_template('alumni.html')

@app.route('/news')
def news():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)

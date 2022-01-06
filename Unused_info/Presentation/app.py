from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
# def hello_world():
#     return 'Hello world'


def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

inputs = {
    'timeInBed' :['text', 'Time in Bed:'],
    'heartRate' :['text', 'Heart Rate:'],
    'activity' :['text', 'Activity:'],
    'stressfulDay' :['checkbox', 'Stressful Day?'],
    'workedOut' :['checkbox', 'Worked Out?'],
    'drankCoffee' :['checkbox', 'Drank Coffee?'],
    'drankTea' :['checkbox', 'Drank Tea?'],
    'ateLate' :['checkbox', 'Ate Late?']
}
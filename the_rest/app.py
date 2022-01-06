
from joblib import load
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
model = load('./ML/linear.joblib')
@app.route("/")
def root():
    return render_template("index.html")

@app.route("/ML/<input1>/<input2>/<input3>/<input4>/<input5>/<input6>/<input7>/<input8>")
def ML(input1,input2,input3,input4,input5,input6,input7,input8):
    
    user_input = [input1,input2,input3,input4,input5,input6,input7,input8]
    user_input2 = list(map(int, user_input))

    print(user_input2)
    # load the model from disk
    # model = load('./ML/linear.joblib')

    result = model.predict([user_input2])
    print(type(result))
    # result = model.predict([[input1,input2,input3,input4,input5,input6,input7,input8]])
    return jsonify(result[0])

    # model = load("linear.joblib")
    # result = model.predict([input1,input2,input3,input4,input5,input6,input7,input8])
    # return jsonify(results)
    # return jsonify(f'{input1} {input2} {input3} {input4} {input5} {input6} {input7} {input8}')

if __name__ == "__main__":
    app.run(debug=True)
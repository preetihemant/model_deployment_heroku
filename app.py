import flask
import pickle
import pandas as pd
# Use pickle to load in the pre-trained model.
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        SepalLengthCm = flask.request.form['SepalLengthCm']
        SepalWidthCm = flask.request.form['SepalWidthCm']
        PetalLengthCm = flask.request.form['PetalLengthCm']
        PetalWidthCm = flask.request.form['PetalWidthCm']
        input_variables = pd.DataFrame([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]],
                                       columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
                                       dtype=float)
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'SepalLengthCm':SepalLengthCm,
                                                     'SepalWidthCm':SepalWidthCm,
                                                     'PetalLengthCm':PetalLengthCm,
                                                     'PetalWidthCm':PetalWidthCm},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()



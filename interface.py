from flask import Flask,jsonify,request
import units

app = Flask(__name__)

@app.route('/predict',methods = ['POST'])
def pred():
    
    data = request.form
    if request.method == 'POST':
        print('Input data is:',data)
        x = int(data['math_score'])
        y = int(data['reading_score'])
        z = int(data['writing_score'])
        

        msg = units.pred_class(x,y,z)

        return jsonify({'Message': int(msg)})
    else:
        return jsonify({'Message':'Unsuccessful'})







if __name__ == '__main__':
    app.run(debug=True)

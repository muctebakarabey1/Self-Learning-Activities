from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/',methods=['GET'])

def home():
    if(request.method=='GET'):
        data='Hello World'
        return jsonify({'Data':data})
    

if __name__=='__main__':
    app.run(debug=True)
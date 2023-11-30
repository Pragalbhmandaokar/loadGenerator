from flask import Flask,request,jsonify
from LoadGenerator import LoadGenerator
import os 
app = Flask(__name__)
target = os.getenv("TARGET", "http://127.0.0.1:5000/primecheck")
frequency = float(os.getenv("FREQUENCY",10))
load_generator = LoadGenerator(target,frequency)

@app.route('/result',methods=["GET","POST"])
def mainRequest():
    if(request.method == "GET"):
        return jsonify(load_generator.print_results())

@app.route('/',methods=["GET","POST"])
def checkServer():
    if(request.method == "GET"):
        return jsonify({"message": "Server is up"})

if __name__ == "__main__":
        load_generator.generator_load()
        load_generator.print_results()
        app.run(host="0.0.0.0",port=5001, debug=True,threaded=True)

        
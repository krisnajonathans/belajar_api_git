from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def _remove_punct(s):
    return re.sub(r"[^\w\d\s]+", "",s)

@app.route("/clean_text/v1", methods=['POST'])
def remove_punct_post(): 
    s = request.get_json()
    non_punct = _remove_punct(s['text'])
    return jsonify({"hasil_bersih":non_punct})

@app.route("/count_text/v1", methods=['POST'])
def count_text(): 
    s = request.get_json()
    len_string = len(s['text'])
    return jsonify({"hasil_bersih":len_string})

@app.route("/get_text/v1", methods=['GET']) #decorator
def return_text():
    name_input = request.args.get('name')
    nohp_input = request.args.get('nomerhp')
    return_text = {
        "text":f"halo semua!! nama saya adalah {name_input}",
        "no_hp" : nohp_input
    }
    return jsonify(return_text) #agar return dalam bentuk json

if __name__ == "__main__" :
    app.run(port=1233, debug=True) #debug => gunanya untuk otomatis mengubah kalau ada perubahan


    
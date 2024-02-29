from flask import Flask, request, jsonify

app = Flask(__name__)

count = 0
@app.get("/count")
def count_requests():
   global count
   count += 1
   return jsonify(count)

@app.post("/reset")
def reset_requests():
   global count
   count = 0
   return jsonify(count)

if __name__ == "__main__":
   app.run(debug=True)
from flask import Flask, redirect,url_for,render_template
app =Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True)

    # @app.route('/success/<int:score>')
    # def success(score):
    #     return"<html><body><h1> this is passed</h1></body><html>"
    
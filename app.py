from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    return variable

if __name__ == "__main__":
    app.run(debug=True)

    
# Person 1 => Modified Line with username : 9394113857


    
#========== Script Commands ============
#1. Ctrl + Shift + F10 => Run the script
#2. Ctrl + f => find
#3. Ctrl + F2 => Stop the script

#========== Tab Navigations ============
# 1.Move To Right Top => Top Right Side
# 2.Bottom Right => Bottom Right Side
#=======================================

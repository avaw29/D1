from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Task 2 : Dynamic URLS
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return '<h1>Welcome to {}</h1>'.format(course_name)

#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using POST method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body>
    <form action = "/result" method = "GET">
        ingredient: <input type = "text" name = "ing"><br>
        <input type = "submit" value = "Submit">
    </form>
    </body>
    </html>
    '''
    return html_form

#Task 3.2 : Processing Form Data
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results
    if request.method == "GET":
        ing = request.args.get("ing")
    base_url = "http://www.recipepuppy.com/api/"
    params_d = {}
    params_d ["i"] = ing
    r = requests.get(base_url, params = params_d)
    s = json.loads(r.text)
    recipes = []
    for rec in s['results']:
        recipes.append(rec['title'])
    res = ""
    for x in recipes:
        res += '<h1>{}</h1>'.format(x)
    return res


if __name__ == '__main__':
    app.run(debug=True)

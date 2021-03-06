from flask import Flask, render_template, request
#render_template is to render the html page
#request is to request the email and HTTP etc

app = Flask(__name__) #the app script is defaultly named '__main__'

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method=='POST':
        email = request.form["email_name"] # get field input
        height = request.form["height_name"]
        print (email, height)
        #print(request.form)#prints every input on the form
        return render_template("success.html")

if __name__ == "__main__":
    app.debug=True
    app.run(port=5800)
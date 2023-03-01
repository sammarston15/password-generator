from flask import Flask, render_template, request, redirect
from password_stuff import generate_password

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# handle form data
@app.route('/submit', methods=['POST'])
def submit():

    if request.method == 'POST':
        data = {}

        # set password params from user input
        data['length'] = request.form.get('length', None) # if user does not input number, the length value will be an empty string
        data['uppercase'] = request.form.get('uppercase', None)
        data['lowercase'] = request.form.get('lowercase', None)
        data['numbers'] = request.form.get('numbers', None)
        data['symbols'] = request.form.get('symbols', None)


        try: 
            # send password params to password generator
            generated_password = generate_password(data=data)
            print("generated password: ", generated_password)

            # render the html template - NOTE: this will put you on the /submit page of the website when this template is rendered
            return render_template('index.html', generated_password=generated_password) 

            # you can also redirect to a new endpoint with the following
            # return redirect('/', generated_password=generated_password)


        except Exception as e:
            print('hit error block')
            print(f"{type(e)}: {e}")
            # render the index.html template but with an alert at the top with the Exception
            return render_template('index.html', error=f"Oops! There was a problem: {e}")


if __name__ == "__main__":
    app.debug = True
    app.run()
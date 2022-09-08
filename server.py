from flask import Flask, render_template, flash, session, request, redirect
from user import User
app = Flask(__name__)
app.secret_key = 'loquesea'

@app.route('/users')
def all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template('index.html', all_users=all_users)

@app.route('/users/new', methods=['GET', 'POST'])
def add_new_user():
    print(f'REQUEST TYPE', request.method)
    if request.method == 'GET':
        return render_template('addNewUser.html')

    elif request.method == 'POST':
        print(F'AQUI--->',request.method)
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        results=User.insert_user(data)
        print(f'result in route', results)
        if results != False:
            return redirect('/users')
        else:
            flash('There was an error inserting a new user', 'danger')
            return redirect('/users/new')
            

if __name__ == '__main__':
    app.run(debug=True)
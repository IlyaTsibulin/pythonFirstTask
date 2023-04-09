from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'


@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged IN'



@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are logged OUT'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'Gotcha ur in'
    return 'Who tf are u get tf outta here betch'

app.secret_key = 'YouWillNeverGuess'


if __name__ == '__main__':
    app.run(debug=True)

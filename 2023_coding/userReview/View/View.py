from flask import Flask
app = Flask(__name__)
# URLを振り分ける司令塔、MVCのControllerに該当

@app.route('/')
def index():
    # フラグでホームページに行くか判断する
    if 'flag' in session and session['flag']:
        return render_template('index.html')
    return redirect('/login')
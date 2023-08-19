from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# コメントアウトはcommand + /

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# SQLiteを使用する場合
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite'

# SQLAlchemyにFlaskで作ったファイルを渡す
# SQLAlchemyはpythonのO/Rマッパー　O/Rマッパーはコードを書いてDBを操作できる
# dbインスタンスを生成
db = SQLAlchemy(app) # このインスタンスを使用して、CRUDを行う

# # Taskクラスはdb.Modleを継承
# class Task(db.Model):
    
#     __tablename__ = "task"
#     # id情報、昇順、プライマリキー
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     # todoリストの文字
#     text = db.Column(db.Text())
#     # リストの状態
#     status = db.Column(db.Integer)

# # db全て（todo.sqliteファイルとtasksテーブル）を作成している
# db.create_all()

# @app.routeはURLルーティングを実現するためのデコレーター
@app.route('/')
def index():
    tasks = Task.query.all()
    # render_template()は1つ目の引数のhtmlにデータを渡し、レンダリングするため
    return render_template("index.html",tasks = tasks)

# host引数にlocalhost、port引数に8001を指定しているので、アプリケーション起動
app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)

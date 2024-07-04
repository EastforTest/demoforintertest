#!/usr/bin/python
# coding=utf-8
from flask import Flask, request, session, jsonify
import hashlib


USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.secret_key = 'pithy'


slat = '@@##$@!?'

#给密码加密
def encry_pwd(password):
    has_md5 = hashlib.md5(password.encode('utf-8'))
    has_md5.update(slat.encode('utf-8'))
    return has_md5.hexdigest()



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != encry_pwd(PASSWORD):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return jsonify({'code': 200, 'msg': 'success'})
    return jsonify({'code': 401, 'msg': error}), 401


@app.route('/info', methods=['get'])
def info():
    if not session.get('logged_in'):
        return jsonify({'code': 401, 'msg': 'please login !!'})
    return jsonify({'code': 200, 'msg': 'success', 'data': 'info'})

if __name__ == '__main__':
    app.run(debug=True)


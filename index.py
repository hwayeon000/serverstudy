# Sever - DB 연동
# Server란?
# Client의 요청(requeat)이 발생하면 응답(response)을 해주는 24시간 돌아가는 모듈

# Flask Server
# Python 언어를 활용한 Micro Web FrameWork

# Web FrameWork?
# 웹 개발을 편리하게 하기 위해 만들어진 일정한 틀!!

# Flask Server 설치!!
# pip install Flask# flask 패키지 안에 여러가지 라이브러리 존재!
# Flask lib : 서버 구동!!, 웹 경로 설정
# render_tamplate : 동일 경로에 있는 tamplates dir 내의 html 문서를 로딩
# request : 요청 객체! Client가 요청한 정보
# Data 전송 방식 : GET, POST

# GET(Query String) : URL 뒷쪽에 ?key1=value1&key2=value2 형식으로 데이터 전송
# 장점 : URL을 통한 방직 -> 같은 page를 볼 수 있음(공유)
# 단점 : 보안, data길이 제한(URL 길이만큼만 전송 가능)

# POST 방식 : <body> 태그 안쪽에 data가 key, value 형식으로 저장되어 전송
# 장점 : 보인, data길이제한 없음
# 단점 : 같은 page를 볼 수 없음(공유)

# ('/loguin') 경로에 request을 받고 싶으면
# methods = ['GET', 'POST']
#request에서 Data 꺼내는 방법
# GET : request.agrs[key값]
# POST : request.form[key값]
# POST + FILE : request.file[key값]
# 하나의 경로(route)에는 하나의 함수가 정의되어 있어야 한다
# 이 때, return에 오는 자료형은 html문서!
# redirect : 페이지 이동
# redirect('http://naver.com')
# redirect('/login') '/'로 시작하게 되면 내 플라스크 서버에서 출발!

# app.run(host='IPv4, port=정수형 포트번호)
# flask port number : 5000~5099
# IPv4 : 32bit (8bit x 4)

# DB연동!!
# DBMS : DataBase Managment Syestem
# MariaDB, MySQL MSSQL

# 만약 MySQL을 프로젝트에 쓴다!
# import cx_Oracle as db 대신에
# import pymysql as db 쓰면 끝
# 각 DBMS들이 Interface를 통해 드라이버를 개발
# Interface : 변수, 함수 이름이 동일!

# DB연동의 4단계
# 1. 드라이버 로딩
# pip install cx_Oraqcle
# Oracle  제조사 홈페이지에서 드라이버 설치
# https://www.oracle.com/database/technologies/instant-client/downloads.html
# 우리 오라클 버전 : 11.g xe(Express Edition)
# 경로(환경변수 추가, 1회만)

# 2. Connection 생성
# DataBase 연결 (DB_ID, DB_PW, DB_URL)

# 3. Cursor 생성
# SQL문 전달 및 결과 저장

# 4. 연결 종료
# curs.close()
# conn.close()
# 역순으로 종료!!


from ntpath import join
from flask import Flask, render_template, request, redirect
import DAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/join', methods = ['POST'])
def sign_up():
    join_id = request.form['id']
    join_pw = request.form['pw']
    join_name = request.form['name']

    DAO.insert(join_id, join_pw, join_name)
    return redirect('/') 
    # http://192.168.20.127:5020/ <이지만 생략시 내 플라스크 서버로 감

@app.route('/login', methods = ['POST'])
def login_check():
    login_id = request.form['id']
    login_pw = request.form['pw']

    if DAO.login(login_id, login_pw):  # 값 자체가 True값이라  ==TRUE: 생략
        return '로그인 성공'
    else:
        return '로그인 실패'

@app.route('/select')
def select_member():
    r = DAO.select()
    return r

if __name__ == '__main__':
    app.run("192.168.20.127", port=5067)


    
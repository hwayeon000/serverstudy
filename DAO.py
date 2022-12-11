from operator import truediv
import cx_Oracle as db

# conn() DB 접속!!

def __conn():
    db_id = 'hr'
    db_pw = 'hr'
    url = '192.168.20.127:1521/xe'
    con = db.connect(db_id, db_pw, url)
    return con

# insert() 회원가입

def insert(join_id, join_pw, join_name):
    con = __conn()
    curs = con.cursor()
    sql = 'insert into member(id, pw, name) values(:1, :2, :3)'
    curs.execute(sql, (join_id, join_pw, join_name))
    con.commit()
    curs.close()
    con.close()

# select() 전체 회원 조회 

def select():
    con = __conn()
    curs = con.cursor()
    sql = 'select * from member'
    rs = curs.execute(sql)
    result = rs.fetchall()   # 리스트 웹상에 html형식으로 변환되지 않음, 튜플<br>태그 형식으로 전처리
    r = '</br>'.join(map(str, result))
    curs.close()
    con.close()
    return r

# login() id, pw -> 로그인 성공/실패 여부

def login(login_id, login_pw):
    con = __conn()
    curs = con.cursor()
    sql = f"select pw from member where id = '{login_id}'"
    rs = curs.execute(sql)
    result = rs.fetchall()

    check = False
    try:
        if result[0][0] == login_pw:
            check = True
    except:
        print('로그인 실패')
    curs.close()
    con.close()

    return check



import re
import MySQLdb as mdb
import binascii


DB_HOST = "localhost"
DB_USER = "root"
DB_NAME = 'project_employee_manager_app'
DB_PASSWORD = 'nhutai1302'

pattern_upper_cha = re.compile(r'^([A-Z])[a-z]+[0-9]+$', re.A)
pattern_number = re.compile(r'(\d{1,4})$', re.A)
pattern_manv = re.compile(r'[A-z0-9]{1,10}$', re.A)
pattern_tennv = re.compile(r"b'([\w\d]){1,100}'")
pattern_age = re.compile(r'^\d{2}$')
pattern_luong = re.compile(r'[0-9.]{1,5}$')
pattern_email = re.compile(r'^[a-zA-Z0-9]{1,30}@\w+\.(\w+\.?){1,2}$', re.A)


def hash_number(number):
    generator = (str(ord(i)) for i in str(number))
    return ''.join(generator)


def hash_user_name(user_name):
    return str(str(ord(pattern_upper_cha.search(user_name).group(1))) + hash_number(pattern_number.search(user_name).group(1)))


def hash_user_passwd(user_name, passwd):
    try:
        db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        cur = db.cursor()
        insert_user = f'insert into user_passwd(user_name, pass) values("{str(ord(pattern_upper_cha.search(user_name).group(1))) + hash_number(pattern_number.search(user_name).group(1))}", "{str(ord(pattern_upper_cha.search(passwd).group(1))) + hash_number(pattern_number.search(passwd).group(1))}")'
        cur.execute(insert_user)
        db.commit()
    except:
       return 0 
    db.close()
    return 1


def registration_validate(user_name, password, rely_password):
    user_pattern = re.compile('^[A-Z][a-z]+\d+$')
    if user_pattern.match(user_name) and password == rely_password and user_pattern.match(password):
        return hash_user_passwd(user_name, password)


def login_validate(user_name, password):
    flag = False
    result1 = None
    if pattern_number.search(user_name) and pattern_upper_cha.search(user_name) and pattern_number.search(password) and pattern_upper_cha.search(password):
        try:
            db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
            cur = db.cursor()
            query_user = f'select * from user_passwd where user_name = "{str(ord(pattern_upper_cha.search(user_name).group(1))) + hash_number(pattern_number.search(user_name).group(1))}" and pass = "{str(ord(pattern_upper_cha.search(password).group(1)))  + hash_number(pattern_number.search(password).group(1))}"'
            cur.execute(query_user)
            result = cur.fetchall()
            if len(result) == 1:
                flag = True
                result1 = result[0][2]
            else:
                result1 = None
            db.close()
        except: 
            return None, result1
    return flag, result1


def query_data(manv, user_name):
    query = f'select * from info where manv = "{manv}" and user_name = "{user_name}"'
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    try:
        cur.execute(query)
        db.close()
        return cur.fetchall()
    except:
        return False


def insert_into_data_base(manv, tennv, luong, tuoi, email, user_name):
    if not pattern_manv.match(manv):
        return "ID's length must between 1 and 10"
    if not pattern_tennv.match(str(tennv)):
        return "Name's length must between 1 and 30"
    if not pattern_age.match(tuoi):
        return "Age must be int and It's length is 2"
    if not pattern_luong.match(luong):
        return "Salary must be float and It's length between 1 and 5"
    if not pattern_email.match(email):
        return 'email incorrect'
    insert_string = f'''insert into info(manv, tennv, luong, tuoi, email, user_name) values("{manv}", {str(tennv).replace('b', '', 1).strip()}, {float(luong)}, {int(tuoi)}, "{email}", "{user_name}");'''
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    try:
        cur.execute(insert_string)
        db.commit()
        db.close()
        return 'Inserted'
    except db.Error as e:
        db.close()
        return 'Duplication ID'


def load_data(user_name):
    query_all = f'select * from info where user_name = "{user_name}"'
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    cur.execute(query_all)
    db.close()
    return cur.fetchall()

def modify_database(manv, tennv, luong, tuoi, email, user_name):
    if not pattern_manv.match(manv):
        return "ID's length must between 1 and 10"
    if not pattern_tennv.match(str(tennv)):
        return "Name's length must between 1 and 30"
    if not pattern_age.match(tuoi):
        return "Age must be int and It's length is 2"
    if not pattern_luong.match(luong):
        return "Salary must be float and It's length between 1 and 5"
    if not pattern_email.match(email):
        return 'email incorrect'
    modify_string = f'''update info set tennv = {str(tennv).replace('b', '', 1).strip()}, luong = {float(luong)}, tuoi = {int(tuoi)}, email = '{email}' where user_name like "{user_name}" and manv like "{manv}";''' 
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    try:
        cur.execute(modify_string)
        db.commit()
        db.close()
        return 'Modified'
    except db.Error as e:
        db.close()
        return 'ID not found'

def delete_data(manv, user_name):
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    delete_string = f"""delete from info where manv like '{manv}' and user_name like '{user_name}'"""
    try:
        cur.execute(delete_string)
        db.commit()
        db.close()
        return 'Deleted'
    except:
        db.close()
        return "Can't delete'"


def insert_image(user_name):
    db = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cur = db.cursor()
    try:
        cur.execute(f'update user_passwd set image = "images/anhdaidien.jpg" where user_name like "{user_name}"') 
        db.commit()
    except db.Error as e:
        print(str(e))
    db.close()


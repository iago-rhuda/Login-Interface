import graphic_interface as face
import global_variables as gv


# Users class
class User:
    def __init__(self, name, password, birth, city):
        self.name = name
        self.password = password
        self.birth = birth
        self.city = city


def handling_user_inputs(name, password, day, user_month, year, city):
    name = name.strip().upper()
    password = password
    if user_month == 'January':
        month = 1
    elif user_month == 'February':
        month = 2
    elif user_month == 'March':
        month = 3
    elif user_month == 'April':
        month = 4
    elif user_month == 'May':
        month = 5
    elif user_month == 'June':
        month = 6
    elif user_month == 'July':
        month = 7
    elif user_month == 'August':
        month = 8
    elif user_month == 'September':
        month = 9
    elif user_month == 'October':
        month = 10
    elif user_month == 'November':
        month = 11
    else:
        month = 12
    day = int(day)
    year = int(year)
    birth = f'{month}/{day}/{year}'
    city = city.strip().upper()
    return [name, password, birth, city]

def handling_birth_forgot_password(recovery_password):
    return recovery_password.replace('/', '-')


def forgot_password(cursor, column, column2,
        recovery_name, recovery_birth, recovery_city,

):
    comand = f'''
    SELECT {column} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_name']}='{recovery_name}'
    '''
    cursor.execute(comand)
    row_birth = cursor.fetchone()
    comand = f'''
    SELECT {column2} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_name']}='{recovery_name}'
    '''
    cursor.execute(comand)
    row_city = cursor.fetchone()
    comand = f'''
    SELECT {gv.db_items['user_password']} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_name']}='{recovery_name}'
    '''
    cursor.execute(comand)
    password = cursor.fetchone()
    if row_birth[0] == recovery_birth and row_city[0] == recovery_city:
        face.recovery_password_accepted(password[0])
    else:
        face.recovery_password_declined()

def handling_login_issues(cursor, name, password):
    comand = f'''
    SELECT {gv.db_items['user_name']} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_name']}='{name}'
    '''
    cursor.execute(comand)
    row_name = cursor.fetchone()
    comand = f'''
    SELECT {gv.db_items['user_password']} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_password']}='{password}'
    '''
    cursor.execute(comand)
    row_password = cursor.fetchone()
    comand = f'''
    SELECT {gv.db_items['user_password']} FROM {gv.db_items['db']}
    WHERE {gv.db_items['user_name']}='{name}'
    '''
    cursor.execute(comand)
    cheking_password = cursor.fetchone()
    if row_name == None:
        row_name = ['inexistente']
    elif row_password == None:
        row_password = ['inexistente']
    if cheking_password == None:
        row_password = ['inexistente']
    return row_name[0], row_password[0]
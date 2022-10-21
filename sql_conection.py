# imports
import pyodbc
import global_variables as gv


# Functions

# creating conextion with db
def create_connection_with_db():
    # initializing connection to db
    try:
        connection_data = (
            "Driver={SQL Server};"
            "Server=;"
            "Database=;"
        )
        conection = pyodbc.connect(connection_data)
        cursor = conection.cursor()
        print(gv.colors['green'] + 'Successful Connection with database' + gv.colors['end'])
        return cursor
    except:
        print(gv.colors['red'] + 'Unsuccessful Connection with database' + gv.colors['end'])
# save new user data in db
def save_db(cursor, name, password, birth, city):
    comand = f'''
    INSERT INTO Users(
{gv.db_items['user_name']}, {gv.db_items['user_password']}, 
{gv.db_items['user_birth']}, {gv.db_items['user_city']})
    VALUES('{name}', '{password}', '{birth}', '{city}')
    '''
    cursor.execute(comand)
    cursor.commit()
# check data in db
def verify_login(cursor, column, name, password):
    comand = f'''
    SELECT {gv.db_items['user_password']} FROM {gv.db_items['db']}
    WHERE {column}='{name}'
    '''
    cursor.execute(comand)
    row = cursor.fetchone()
    # 1 = access accepted
    # 0 = access declined
    if row == None:
        print(gv.colors['red'] + 'Access declined' + gv.colors['end'])
        access = 0
        return access
    elif row[0] == password:
        print(gv.colors['green']+'Access accepted'+gv.colors['end'])
        access = 1
        return access
    else:
        print(gv.colors['red'] + 'Access declined' + gv.colors['end'])
        access = 0
        return access

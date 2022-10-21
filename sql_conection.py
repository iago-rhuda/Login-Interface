import pyodbc
import global_variables as gv


def create_connection_with_db():
    # initializing connection to db
    try:
        connection_data = (
            "Driver={SQL Server};"
            "Server=EU\TEW_SQLEXPRESS;"
            "Database=teste_integracao_sql;"
        )
        conection = pyodbc.connect(connection_data)
        cursor = conection.cursor()
        print(gv.colors['green'] + 'Successful Connection with database' + gv.colors['end'])
        return cursor
    except:
        print(gv.colors['red'] + 'Unsuccessful Connection with database' + gv.colors['end'])

# save data in db
def save_db(cursor, name, password, birth, city):

    # atentar - se, passar parâmetros com '' para o SQL (não numéricos)
    comand = f'''
    INSERT INTO Users(
{gv.db_items['user_name']}, {gv.db_items['user_password']}, 
{gv.db_items['user_birth']}, {gv.db_items['user_city']})
    VALUES('{name}', '{password}', '{birth}', '{city}')
    '''
    cursor.execute(comand)
    # efetivar mudança no bd
    cursor.commit()
    #print(f"'{name}', '{password}', '{birth}', '{city}'")

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

def update_db(cursor, item, value, column, id):
    comand = f'''
    UPDATE Users SET {item} = {value}
    WHERE {column} = {id}
    '''
    cursor.execute(comand)
    cursor.commit()

# delete data in db
def delete_db(cursor, name):
    comand = f'''
    DELETE FROM Users
    '''
    cursor.execute(comand)

def see_password(cursor, search):
    # 0 to don't see password
    # 1 to see password
    comand = f'''
    SELECT password_look FROM global_variables
        WHERE id={search}
    '''
    cursor.execute(comand)
    password = cursor.fetchone()
    print(password[0])
    if password[0] == 'False':
        print('Tá vendo')
    else:
        print('Não tá vendo')
    return password

cursor = create_connection_with_db()
see_password(cursor, 0)

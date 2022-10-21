# imports
import functions
import graphic_interface as g
import PySimpleGUI as sg
import global_variables as gv
import functions as f
import sql_conection as db


# match (event):
#     case 'Login':


search = 0
# creating the windows
login_window, registration_window, \
main_window, forgot_password_window = g.login_window(), None, \
                                      None, None
# initializing connection to db
cursor = db.create_connection_with_db()
# infinite loop
while True:
    # reading the windows and collecting data
    window, event, value = sg.read_all_windows()
    # checking windows closing
    if event == sg.WINDOW_CLOSED or event == 'Close':
        print(gv.colors['cyan']+'Ending program'+gv.colors['end'])
        break
    # see password in registration window
    if event == '*':
        search = 1
        window.Refresh()
        password_look = db.see_password(cursor, search)
        window = g.login_window_see_password()
        pass
    # checking login validations
    if event == 'Login':
        name = value['name'].strip().upper()
        password = value['password']
        # 1 = access accepted
        # 0 = access declined
        access = db.verify_login(
            cursor, gv.db_items['user_name'], name, password
        )
        # Events to update the interface:
        # - 0 to continue
        # - 1 to user/password wrong
        # - 2 to user not register
        if access == 0:
            update = g.event_name_update(cursor, name, password)
            window_name = update[0]
            login_event = update[1]
            if login_event == 0:
                window.hide()
                window = g.main_window(window_name)
            # layout to user/password incorrect
            elif login_event == 1:
                window.hide()
                window = g.user_password_wrong(window_name)
            # layout to unregistered user
            elif login_event == 2:
                window.hide()
                window = g.unregistered_user(window_name)
        if access == 1:
            window.hide()
            main_window = g.main_window('Logged')
    # checking windows change
    if event == 'Register':
        window.hide()
        registration_window = g.registration_window()
    if event == 'Back':
        window.hide()
        login_window.un_hide()
    if event == 'Forgot Password':
        login_window.hide()
        forgot_password_window = g.forgot_password_window()
    # handling 'forgot password'
    if event == 'Recovery':
        recovery_name = value['recovery_name'].strip().upper()
        recovery_birth = functions.handling_birth_forgot_password(value['recovery_birth'])

        recovery_city = value['recovery_city'].strip().upper()
        access = functions.forgot_password(
            cursor, 'birth', 'city',
            recovery_name, recovery_birth, recovery_city
        )
    if event == 'Back to Login':
        forgot_password_window.hide()
        login_window.un_hide()
    # registering new user
    if window == registration_window and event == 'Save':
        # confirming matching passwords
        if value['password'] != value['confirm_password']:
            print(gv.colors['yellow']+"Passwords don't match"+gv.colors['end'])
            window = g.registration_password_match()
        else:
            # handling the inputs
            user_data = f.handling_user_inputs(
                value['name'], value['password'], value['day_birth'],
                value['month_birth'], value['year_birth'], value['city'])
            # creating a new user
            user = f.User(
                user_data[0], user_data[1],
                user_data[2], user_data[3]
            )
            # saving user in db
            db.save_db(cursor,
                       user_data[0], user_data[1],
                       user_data[2], user_data[3]
                       )
            # printing welcome to the new user
            print(gv.colors['blue']+f'Welcome {user.name}'+gv.colors['end'])
            print(f'''
    User: {user.name}
    Password: {user.password}
    Birth: {user.birth}
    City: {user.city}
    ''')
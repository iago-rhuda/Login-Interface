# imports
import PySimpleGUI as sg
import functions
import global_variables as gv
# import PySimpleGUIWeb
# import PySimpleGUIQt
# import PySimpleGUIWx


# functions

# login window function
def login_window():
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char='*'),
         sg.Button('*')],
        [sg.Button('Login'), sg.Button('Close'),
         sg.Button('Register'), sg.Button('Forgot Password')]
    ]
    return sg.Window('Login', layout=layout, finalize=True, element_justification='c')

def login_window_see_password():
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char=False),
         sg.Button('*')],
        [sg.Button('Login'), sg.Button('Close'),
         sg.Button('Register'), sg.Button('Forgot Password')]
    ]
    return sg.Window('Login', layout=layout, finalize=True, element_justification='c')

# registration window function
def registration_window():
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Birth date: '),
         sg.Combo(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
             23, 24, 25, 26, 27, 28, 29, 30, 31],
             key='day_birth'),
         sg.Text('/'),
         sg.Combo(
             ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
             key='month_birth'),
         sg.Text('/'),
         sg.Combo([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
                   1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                   2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
                   2017, 2018, 2019, 2020, 2021, 2022], key='year_birth')],
        [sg.Text('City: '), sg.InputText(key='city')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char='*'),
         sg.Button('*')],
        [sg.Text('Confirm password: '), sg.InputText(key='confirm_password', password_char='*')],
        [sg.Button('Save'), sg.Button('Back'), sg.Button('Close')],
    ]
    return sg.Window('Registration', layout=layout, finalize=True)

# registration password don't match window function
def registration_password_match():
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Birth date: '),
         sg.Combo(
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
              12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25, 26, 27, 28, 29, 30, 31],
             key='day_birth'),
         sg.Text('/'),
         sg.Combo(
             ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
             key='month_birth'),
         sg.Text('/'),
         sg.Combo([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
                   1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                   2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
                   2017, 2018, 2019, 2020, 2021, 2022], key='year_birth')],
        [sg.Text('City: '), sg.InputText(key='city')],
        [sg.Text("Passwords don't match, please check.", text_color='yellow')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char='*'),
         sg.Button('*')],
        [sg.Text('Confirm password: '), sg.InputText(key='confirm_password', password_char='*')],
        [sg.Button('Save'), sg.Button('Back'), sg.Button('Close')],
    ]
    return sg.Window('Registration', layout=layout, finalize=True)

# 'forgot password' window
def forgot_password_window():
    sg.theme(gv.theme)
    layout = [
        [sg.Text('To recover your password, please answer the questions bellow:')],
        [sg.Text("What's your name ?"), sg.Input(key='recovery_name')],
        [sg.Text("What's your birth date ? (yyyy/mm/dd)"), sg.Input(key='recovery_birth')],
        [sg.Text("What's your hometown ?"), sg.Input(key='recovery_city')],
        [sg.Button('Recovery'), sg.Button('Back'), sg.Button('Close')],
    ]
    return sg.Window('Password Recovery', layout=layout, finalize=True)

def recovery_password_accepted(password):
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Your password is:')],
        [sg.Text(password, text_color='green')], [sg.Button('Back to Login')]

    ]
    return sg.Window('Password Recovery', layout=layout, finalize=True, element_justification='c')

def recovery_password_declined():
    sg.theme(gv.theme)
    return sg.popup_ok("We couldn't find your user, please contact your supervisor")

# main window function
def main_window(name):
    sg.theme(gv.theme)
    layout = [
        [sg.Text('Good Boy')],
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Password: '), sg.InputText(key='password')],
        [sg.Button('Login'), sg.Button('Close'),
         sg.Button('Register')],
    ]
    return sg.Window(name, layout=layout, finalize=True)

def event_name_update(cursor, name, password):
    # Events to update the interface:
    # - 0 to continue
    # - 1 to user/password wrong
    # - 2 to user not register
    event_update = 0
    window_name = ''
    db = functions.handling_login_issues(cursor, name, password)
    user_name = db[0]
    user_password = db[1]
    db = [
        user_name, user_password
    ]
    if name and password in db:
        event_update = 0
        window_name = f'Welcome {name}'
    elif name in db or password in db:
        event_update = 1
        window_name = 'User/Password Wrong, please check'
    elif name not in db:
        event_update = 2
        window_name = 'Unregistered User, please register'
    return window_name, event_update

def user_password_wrong(name):
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char='*')],
        [sg.Text('User and/or password incorrect | Login Declined', text_color='red')],
        [sg.Button('Login'), sg.Button('Close'), sg.Button('Register')]
    ]
    return sg.Window(name, layout=layout, finalize=True)

def unregistered_user(name):
    layout = [
        [sg.Text('Name: '), sg.InputText(key='name')],
        [sg.Text('Password: '), sg.InputText(key='password', password_char='*')],
        [sg.Text('Unregistered user | Login Declined', text_color='red')],
        [sg.Text('Please register', text_color='yellow')],
        [sg.Button('Login'), sg.Button('Close'), sg.Button('Register')]
    ]
    return sg.Window(name, layout=layout, finalize=True)
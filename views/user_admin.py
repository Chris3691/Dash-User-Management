import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table as dt
from dash.dependencies import Input, Output, State

from app import app
from users_mgt import show_users, add_user


layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlUserAdmin', refresh=True),
        html.H3('Add New User'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dbc.Label('Username: '),
                dcc.Input(
                    id='newUsername',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Password: '),
                dcc.Input(
                    id='newPwd1',
                    type='password',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Retype New Password: '),
                dcc.Input(
                    id='newPwd2',
                    type='password',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
            ], md=4),

            dbc.Col([
                dbc.Label('Email: '),
                dcc.Input(
                    id='newEmail',
                    className='form-control',
                    n_submit=0,
                    style={
                        'width' : '90%'
                    },
                ),
                html.Br(),
                dbc.Label('Admin? '),
                dcc.Dropdown(
                    id='admin',
                    style={
                        'width' : '90%'
                    },
                    options=[
                        {'label' : 'Yes', 'value' : 1},
                        {'label' : 'No', 'value' : 0},
                    ],
                    value='0',
                    clearable=False
                ),
                html.Br(),
                html.Br(),
                html.Button(
                    children='Create User',
                    id='createUserButton',
                    n_clicks=0,
                    type='submit',
                    className='btn btn-primary btn-lg'
                ),
                html.Br(),
                html.Div(id='createUserSuccess')
            ], md=4),

            dbc.Col([

            ], md=4)

        ]),
    ], className='jumbotron'),

    dbc.Container([
        html.H3('View Users'),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                dt.DataTable(
                    id='users',
                    columns = [{'name' : 'ID', 'id' : 'id'},
                                {'name' : 'Username', 'id' : 'username'},
                                {'name' : 'Email', 'id' : 'email'},
                                {'name' : 'Admin', 'id' : 'admin'}],
                    data=show_users(),
                ),
            ], md=12),
        ]),
    ], className='jumbotron')
])


################################################################################
# CREATE USER BUTTON CLICK / FORM SUBMIT - VALIDATE USERNAME
################################################################################
@app.callback(Output('newUsername', 'className'),

              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],

              [State('newUsername', 'value')])

def validateUsername(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newUsername):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newUsername == None or newUsername == '':
            return 'form-control is-invalid'
        else:
            return 'form-control is-valid'
    else:
        return 'form-control'



################################################################################
# CREATE USER BUTTON CLICK / FORM SUBMIT - RED BOX IF PASSWORD DOES NOT MATCH
################################################################################
@app.callback(Output('newPwd1', 'className'),

              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],

              [State('newPwd1', 'value'),
              State('newPwd2', 'value')])

def validatePassword1(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newPassword1, newPassword2):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newPassword1 == newPassword2 and newPassword1 != '' and newPassword1 != None:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'


################################################################################
# CREATE USER BUTTON CLICK / FORM SUBMIT - RED BOX IF PASSWORD DOES NOT MATCH
################################################################################
@app.callback(Output('newPwd2', 'className'),

              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],

              [State('newPwd1', 'value'),
              State('newPwd2', 'value')])

def validatePassword2(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newPassword1, newPassword2):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newPassword1 == newPassword2 and newPassword2 != '' and newPassword2 != None:
            return 'form-control is-valid'
        else:
            return 'form-control is-invalid'
    else:
        return 'form-control'



################################################################################
# CREATE USER BUTTON CLICK / FORM SUBMIT - VALIDATE EMAIL
################################################################################
@app.callback(Output('newEmail', 'className'),

              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],

              [State('newEmail', 'value')])

def validateEmail(n_clicks, usernameSubmit, newPassword1Submit,
    newPassword2Submit, newEmailSubmit, newEmail):

    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):

        if newEmail == None or newEmail == '':
            return 'form-control is-invalid'
        else:
            return 'form-control is-valid'
    else:
        return 'form-control'





################################################################################
# CREATE USER BUTTON CLICKED / ENTER PRESSED - UPDATE DATABASE WITH NEW USER
################################################################################
@app.callback(Output('createUserSuccess', 'children'),

              [Input('createUserButton', 'n_clicks'),
              Input('newUsername', 'n_submit'),
              Input('newPwd1', 'n_submit'),
              Input('newPwd2', 'n_submit'),
              Input('newEmail', 'n_submit')],

              [State('pageContent', 'children'),
              State('newUsername', 'value'),
              State('newPwd1', 'value'),
              State('newPwd2', 'value'),
              State('newEmail', 'value'),
              State('admin', 'value')])

def createUser(n_clicks, usernameSubmit, newPassword1Submit, newPassword2Submit,
            newEmailSubmit, pageContent, newUser, newPassword1, newPassword2, newEmail, admin):
    if (n_clicks > 0) or (usernameSubmit > 0) or (newPassword1Submit > 0) or \
        (newPassword2Submit > 0) or (newEmailSubmit > 0):


        if newUser and newPassword1 and newPassword2 and newEmail != '':
            if newPassword1 == newPassword2:
                try:
                    add_user(newUser, newPassword1, newEmail, admin)
                    return html.Div(children=['New User created'], className='text-success')
                except Exception as e:
                    return html.Div(children=['New User not created'], className='text-danger')
            else:
                return html.Div(children=['Passwords do not match'], className='text-danger')
        else:
            return html.Div(children=['Invalid details submitted'], className='text-danger')

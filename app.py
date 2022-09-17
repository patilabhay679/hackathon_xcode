from dash_extensions.enrich import DashProxy, Output, State, Input, MultiplexerTransform
from dash import html, dcc
from dash_app_layout import container
import dash_bootstrap_components as dbc
from json import loads, dumps , load, dump
app = DashProxy(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                prevent_initial_callbacks=True,
                transforms=[MultiplexerTransform()],)

app.layout = html.Div([container])

@app.callback(
    Output('json_response', 'children'),
    [State('json_response', 'children'), State('label_text', 'value'), State('label_size', 'value'), State('label_color', 'value')],
    [Input('label_btn', 'n_clicks')])
def main(json_response, label_text, label_size, label_color, _):
    dict_json_response = loads(json_response)
    label_json = {'label': {'text': label_text,
                            'fontSize': label_size,
                            'color': label_color}}
    dict_json_response['components'].append(label_json)

    return dumps(dict_json_response)

@app.callback(
    Output('json_response', 'children'),
    [State('json_response', 'children'), State('title_text', 'value'), State('title_size', 'value'), State('title_color', 'value')],
    [Input('title_btn', 'n_clicks')])
def main(json_response, title_text, title_size, title_color, _):
    dict_json_response = loads(json_response)
    title_json = {'label': {'text': title_text,
                            'fontSize': title_size,
                            'color': title_color}}
    dict_json_response['components'].append(title_json)

    return dumps(dict_json_response)

@app.callback(
    Output('json_response', 'children'),
    State('json_response', 'children'),
    [Input('undo_btn','n_clicks')])
def pop_json_response(json_response,_):
    dict_json_response = loads(json_response)
    dict_json_response['components'].pop()
    return dumps(dict_json_response)
    
@app.callback(
    Output('database_response', 'children'),
    [State('username', 'value'),State('password', 'value'),State('json_response', 'children'),],
    [Input('store_json','n_clicks')])
def store_json_response(username,password,json_response,_):
        if not username:
            return 'No username received'
        if not password:
            return 'No password received'
        dict_json_response = loads(json_response)
        if len(dict_json_response['components']) ==0:
            return 'No json components received'
        
        with open('./Data_Storage/users.json','rt') as users_file:
            dict_users = load(users_file)
        
        if username in dict_users:
            #case for new user
            if dict_users[username] != password:
                return f"Username {username} Already Exist Please enter other Username"
            else:
                with open('./Data_Storage/database.json','rt') as db_file:
                    dict_database = load(db_file)
                dict_database[username]=dict_json_response
            
                dump(dict_database,open('./Data_Storage/database.json','w'),indent=4)
                
                return f'Json components are Appended @Username: {username}'
        else:
            dict_users[username] =password
            with open('./Data_Storage/database.json','rt') as db_file:
                dict_database = load(db_file)
            dict_database[username]=dict_json_response
            
            dump(dict_users,open('./Data_Storage/users.json','w'),indent=4)
            dump(dict_database,open('./Data_Storage/database.json','w'),indent=4)
            
            return f'Json components are stored @Username: {username}'
    
@app.callback(
    [Output('database_response', 'children'),Output('json_response', 'children')],
    [State('username', 'value'),State('password', 'value')],
    [Input('load_json','n_clicks')])
def store_json_response(username,password,_):
        if not username:
            return ['No username received',[]]
        if not password:
            return ['No password received',[]]

        with open('./Data_Storage/users.json','rt') as users_file:
            dict_users = load(users_file)
        
        if username in dict_users:
            if dict_users[username] == password:
                with open('./Data_Storage/database.json','rt') as db_file:
                    dict_database = load(db_file)
                return [f'Json components are sucessfully retrived from @Username: {username}',dumps(dict_database[username])]
            else:
                return ['Invalid Password',[]]
        else:
            return [f"Username {username} doesn't Exist",[]]
                
app.run()

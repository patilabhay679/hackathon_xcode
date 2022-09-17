from flask import Flask,request
from json import load
app = Flask(__name__)

@app.route('/')
def send_json_components():
    with open('./Data_Storage/users.json','rt') as users_file:
        dict_users = load(users_file)
        
    if len(request.args)>=2:
        username = request.args['username']
        password = request.args['password']
    else:
        return 'Not All Query Parameters Received'
    
    if username in dict_users:
        if dict_users[username] == password:
            with open('./Data_Storage/database.json','rt') as db_file:
                dict_database = load(db_file)
            return dict_database[username]
        else:
            return 'Invalid Password'
    else:
        return f"Username {username} doesn't Exist"
    
app.run()

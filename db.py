from firebase import firebase

db = firebase.FirebaseApplication('https://yonchi-97f33.firebaseio.com/', authentication=None)

# def login(name):
#     all_users = db.get("/users", None)
#     for k, v in all_users.items():
#         a = v['name'].encode('utf-8')
#         if  a == name:
#             print(name + " - was logined")
#             return True
#     db.post('/users', data={"name": name}, params={'print': 'pretty'})

def update_result(name, result):
    all_users = db.get("/users", None)
    for k, v in all_users.items():
        nickname = v['name'].encode('utf-8')
        record = v['record']
        if nickname == name:
            if result > record:
                db.patch('users/' + k, data={"record": result})
                return True
    db.post('/users', data={"name": name, "record": result}, params={'print': 'pretty'})
    return True
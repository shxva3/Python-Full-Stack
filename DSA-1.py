email_id = ['shiva@gmail.com', 'gopi@gmail.com', 'sai@gmail.com']
print(len(email_id))
print(email_id[-2])
users = dict.fromkeys(email_id)
print(users)
users['shiva@gmail.com'] = (2, 3)
print(users)
for i in range(len(email_id)):
    users[i + 1] = email_id[i]
print(users)

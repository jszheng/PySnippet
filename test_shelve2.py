import shelve

with shelve.open("myshelve") as db:
    db['egg'] = 'eggs'
    db['list'] = [1,2, '1111']
    tmp = db['list']
    tmp.append(5)

with shelve.open("myshelve") as db:
    for key in list(db.keys()):
        print(db[key])


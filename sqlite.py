import sqlite3 as sq

async def db_start():
    global db, cur

    db = sq.connect('mewest.db')
    cur = db.cursor()

    db.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo TEXT, age TEXT, description TEXT, name TEXT)")

    db.commit()


async def create_profile(user_id):
    user = db.execute("SELECT 1 FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        db.execute('INSERT INTO profile VALUES(?, ?, ?, ?, ?)', (user_id, '', '', '', ''))
        db.commit()




async def edit_profile(state, user_id):
    async with state.proxy() as data:
        db.execute("UPDATE profile SET photo = '{}', age = '{}', description = '{}', name = '{}' WHERE user_id = '{}'".format(
            data['photo'], data['age'], data['description'], data['name'], user_id))
        db.commit()
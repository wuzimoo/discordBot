import sqlite3 as sql

db = sql.connect('DataBase.db')
with db:
    cur = db.cursor()
    cur.execute("""CREATE TABLE if not exists guilds (
        guild_id TEXT,
        onn TEXT
        )""")
    
class dataBase:
    def insert_guild(guild_id, onn):
        cur.execute(""" INSERT INTO guilds (guild_id, onn) VALUES (?,?) """, (guild_id, onn))
        db.commit()
        return {"status" : True}

    def of_or_on_protect(guild_id):
        cur.execute(""" SELECT onn FROM guilds WHERE guild_id = ? """, (guild_id,))
        stat = cur.fetchall()[0][0]
        if stat == "True":
            n_stat = "False"
        elif stat == "False":
            n_stat = "True"
        cur.execute(""" UPDATE guilds SET onn = ? WHERE guild_id = ? """, (n_stat, guild_id))
        db.commit()
        return {"status" : True}

    def select_onn(guild_id):
        cur.execute(""" SELECT onn FROM guilds WHERE guild_id = ? """, (guild_id,))
        stat = cur.fetchall()[0][0]
        return {"status" : True, "text" : stat}
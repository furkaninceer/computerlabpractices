import sqlite3
con=sqlite3.connect("database.db")
cursor=con.cursor()

def tabloyu_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Hız INT,Atış INT)")
    con.commit()
def veri_ekle(İsim,Hız,Atış):
    cursor.execute("Insert into kitaplık values(?,?,?) ",(İsim,Hız,Atış))
    con.commit()
def veri_al():
    cursor.execute("Select * From kitaplık")
    data=cursor.fetchall()
    for i in data:
        print(i)
    con.commit()
def veri_al2():
    cursor.execute("Select Hız,Atış From kitaplık" )
    data=cursor.fetchall()
    for i in data:
        print(i)
    con.commit()
def veri_al3(Speed):
    cursor.execute("select * from kitaplık where Hız=?",(Speed,))
    data=cursor.fetchall()
    for i in data:
        print(i)
    con.commit()
def veri_güncelle(new_speed,İsim):
    cursor.execute("update kitaplık set Hız=? where İsim=?",(new_speed,İsim))
    con.commit()
def veri_sil(İsim):
    cursor.execute("delete from kitaplık where İsim=?",(İsim,))
    con.commit()

con.close()
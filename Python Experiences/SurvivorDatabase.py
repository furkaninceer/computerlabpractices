import sqlite3,time
class Yarışmacı():
    def __init__(self,İsim,Atış,Hız,İlişki):
        self.İsim=İsim
        self.Atış=Atış
        self.Hız=Hız
        self.İlişki=İlişki
    def __str__(self):
        return (f"İsim:{self.İsim},Atış:{self.Atış},Hız:{self.Hız},İlişki:{self.İlişki}")
class Survivor():
    def bağlanti_oluştur(self):
        self.bağlantı=sqlite3.connect("database.db")
        self.cursor=self.bağlantı.cursor()
        sorgu="Create Table IF NOT EXISTS survivor(İsim TEXT,Atış INT,Hız INT,İlişki INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()
    def __init__(self):
        self.bağlanti_oluştur()
    def yarışmacıları_göster(self):
        sorgu="Select * from survivor  "
        self.cursor.execute(sorgu)
        data=self.cursor.fetchall()
        if len(data)==0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            for i in data:
                yarışmacı=Yarışmacı(i[0],i[1],i[2],i[3],)
                print(yarışmacı)
        self.bağlantı.commit()
    def yarışmacı_ekle(self,yarışmacı):
        sorgu="Insert into survivor values(?,?,?,?)"
        self.cursor.execute(sorgu,(yarışmacı.İsim,yarışmacı.Atış,yarışmacı.Hız,yarışmacı.İlişki))
        self.bağlantı.commit()
    def yarışmacı_sil(self,İsim):
        sorgu="Delete from survivor where İsim=?",(İsim,)
        self.cursor.execute(sorgu)
        self.bağlantı.commit()
    def ilişki_arttırma(self,İsim):
        sorgu="Select * from survivor where İsim=? "
        self.cursor.execute(sorgu,(İsim,))
        data=self.cursor.fetchall()
        if len(data)==0:
            print("Böyle bir kitap bulunmuyor...")
        else:   
            for i in data:
                yarışmacı=Yarışmacı(i[0],i[1],i[2],i[3])
                yarışmacı.Atış+=1
            
    def bağlantıyı_kes(self):
        self.bağlantı.close()
yarışmacı=Yarışmacı("Poyraz",8,10,9)
survivor=Survivor()
survivor.yarışmacıları_göster()


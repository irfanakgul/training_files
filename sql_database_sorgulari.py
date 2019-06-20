import sqlite3 # SQLite3 veri tabani modulumuzu iceri aktardik(import)

con=sqlite3.connect("okul.db")
#okul adinda bir veritabani dosyasi olusturduk.
#Bu dosyayi "con" degiskenine atadik.
#sqlite3.connect ifadesi olusturulan dosyaya baglanmak icin kullanilir.

cursor=con.cursor()  #veya imlec=con.cursor()   de diyebiliriz..
#cursor adinda bir imlec atadik. bu imlec bizim olusturdugumuz database dosyasinin icinde gezinmemizi saglar.
#not: adini farkli da koyabiliriz onemli degil.

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci(isim text,soyisim text,memleket text,numarasi int)")
    #cursor.execute() ile okul dosyasinin icine ogrenci adinda bir tablo olusturduk.
    #IF TABLE IF NOT EXIST ifadesi eger ogrenci adinda bir tablo yoksa olustur ve calistir
    #eger varsa sadece calistir anlaminda kullanilan bir ibaredir. Mecburidir.
    #isim text ve diger ifadeler ise bizim tablomuzun sutun basliklarini olusturmaktadir. text string anlamindadir.
    #NOT: Sadece isimleri degistirerek bu fonksiyonlar her yerde kullanilabilir.

    con.commit()
    #commit ibaresi ile birlikte  atadigimiz fonksiyonu dosyaya gondermek icin kullanilir.
    #eger kullanmazsak def fonksiyonu calismaz. ve tablo olusmaz.


def veri_ekle():
    cursor.execute("INSERT INTO ogrenci VALUES ('irfan','Akgul','Edirne',21)")
    #Bu bolumde okul veritabani dosyamizin icindeki ogrenci tablosuna veri ekliyoruz.
    #INSERT INTO ...... VALUES  parametresinin aldigi bilgiler tablomuzdaki sutunlara sirasiyla eklenecektir.
    #NOT: Her calistirildiginda sadece yukaridaki bilgileri ekler

    con.commit()
    # commit ibaresi ile birlikte  atadigimiz fonksiyonu dosyaya gondermek icin kullanilir.
    # eger kullanmazsak def fonksiyonu calismaz. ve tablo olusmaz.



def kullanicidan_veri_ekleme(isim,soyisim,memleket,numara): # fonksiyon 4 deger alacak
    cursor.execute("INSERT INTO ogrenci VALUES(?,?,?,?)",(isim,soyisim,memleket,numara))
    #ogrenci tablosuna isim,s,mem,no degerlerini ekleyecektir. Fakat bu degerler alttaki input ile kullanicidan gelecektir.
    #NOT: Bu fonksiyonun calismasi icin def fonksiyonlarinin altindaki inputlarida almayi(kullanmayi)unutmayiniz.

    con.commit()
    # commit ibaresi ile birlikte  atadigimiz fonksiyonu dosyaya gondermek icin kullanilir.
    # eger kullanmazsak def fonksiyonu calismaz. ve tablo olusmaz.




def verileri_al():
    cursor.execute("SELECT * FROM ogrenci") # ogrenci tablosundan verileri cekmek icin kullanilir.
    liste=cursor.fetchall()
    # cursor.fetchall() ile ifadesi tablomuzdaki verileri almak icin kullanilir.
    #Tablodan cektigimiz verileri "liste" adli degiskenimize atiyoruz
    #NOT: Bu sefer "con.commit()" kullanmadik cunku tabloya bir bilgi gondermeyecegiz. sadece tablodan bilgi cekecegiz.

    for i in liste:
        print(i)
    # listenin icindeki bilgileri daha duzenli yazdirmak icin for dongusu ile print yaptik.
    # sadece print deseydik tum bilgiler yanyana yazdirilir ve okunmasi zor olurdu.

def verileri_al2(): #bu fonksiyon ogrenci tablosundaki sadece isim ve soyisim sutunlarini cekebilmek icin kullanilir.
    cursor.execute("SELECT isim,soyisim FROM ogrenci") #ogrenci tablosundan isim,soyisim bilgilerini ceker.
    liste2=cursor.fetchall() # tablodan bilgi almak icin kullanilir. gelen bilgileri liste2 adli bir listeye atadik.
    for i in liste2:
        print(i)
        # listenin icindeki bilgileri daha duzenli yazdirmak icin for dongusu ile print yaptik.
        # sadece print deseydik tum bilgiler yanyana yazdirilir ve okunmasi zor olurdu.

def verileri_al3(memleket): #memleketi belirli bi yer olanlari print eder.
    cursor.execute("Select * From ogrenci Where memleket= ?",(memleket))
    #ogrenci tablosundaki memleketi .... olanlari print etmek icin kullanilir.
    liste3=cursor.fetchall() #alinan bilgileri liste3 adli listeye atar.(ekler)
    for i in liste3:
        print(i)
        # listenin icindeki bilgileri daha duzenli yazdirmak icin for dongusu ile print yaptik.
        # sadece print deseydik tum bilgiler yanyana yazdirilir ve okunmasi zor olurdu.
#NOT: def verileri_al3 fonksiyonu calismadi.

def veri_guncelleme1(eski_memleket,yeni_memleket):
    #tablomuzdaki bir veriyi degistirmek istedigimizde kullancagimiz fonksiyondur.
    cursor.execute("Update ogrenci set memleket = ? where memleket = ?",(yeni_memleket,eski_memleket))
    #update ogrenci ile ogrenci tablosunu degistirecegimizi soyledik,
    # set memleket ile yeni memleketin adinin ne olacagini soyledik.
    #where memleket ile degistirilmesini istedigimiz memleketin adini yazdik.
    #NOT: once yeni isim sonra eski isim yazilir.

    con.commit()
    # tabloda degisiklik yapacagimiz icin bu sefer con.commit() i kullandik.

def veri_silme(soyisim):
    #tablodan veri silmek icin kullanilan fonksiyondur.
    cursor.execute("Delete from ogrenci Where soyisim= ?",(soyisim,))
    # soyisim sonundaki virgul olmazsa calismiyor.
    #ogrenci tablosundan soyismi ? olan tum satirlari siler.
    con.commit()
    # tabloda degisiklik yapacagimiz icin bu sefer con.commit() i kullandik.



isim=input("Isim : ")
soyisim=input("Soyisim : ")
memleket=input("Memleket : ")
numara=input("Numara : ")
#Bu Dort veri (inputlar) 'def kullanicidan_veri_ekleme(isim,soyisim,memleket,numara):' fonksiyonu icin kullanidan girdi olusturacak
# ve en sonunda tablomuza eklenecektir.

kullanicidan_veri_ekleme(isim,soyisim,memleket,numara)
#Onemli NOT: Calistirirken icine degerleri eklemeyi unutma...!!!


con.close() #veritabani dosyamizi kapatmak icin kullandik.


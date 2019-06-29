import smtplib
#servere baglanmak icin bu modul kullanilir.
from email.mime.multipart import MIMEMultipart
#mailin yapisini olusturur.Govde gibi
from email.mime.text import MIMEText
#mailde ne yazacagini bu modulle ayarliyoruz,
import sys
#hata mesajini sterror ile cevirecegiz

mesaj=MIMEMultipart()
mesaj["From"]="mrakgul.nl@gmail.com"
mesaj["To"]="mrakgul.nl@gmail.com"
mesaj["Subject"]="Mail gonderme denemesi"

yazi=""" deneme maili gonderiyorum....
irfan akgul
"""

mesaj_govdesi=MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mrakgul.nl@gmail.com" , "********")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail Basari ile gonderildi..")
    mail.close()
except:
    sys.stderr.write("Bir sorun olustu...")
    sys.stderr.flush()

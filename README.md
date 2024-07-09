İstanbulKart Dolum Noktaları ve Güzergah Planlayıcı
Bu proje, İstanbul'da yolculuk sırasında kullanıcılara en uygun güzergahları, alternatif yolları ve en yakın İstanbulKart dolum noktalarını sunmak amacıyla geliştirilmiştir. Kullanıcılar, web sitesi üzerinden eşzamanlı olarak güncellenen verilerle en güncel dolum noktalarını kolayca bulabilirler. Proje, zaman ve enerji tasarrufu sağlamaya yönelik olup, toplu taşıma kullanımını teşvik etmektedir.

Özellikler
Başlangıç ve Bitiş Noktası Seçimi: Harita üzerinde yolculuğa başlanacak ve bitirilecek noktalar işaretlenebilir.
Güzergah Alternatifleri: Ana güzergah dışında, alternatif güzergah senaryoları üretilir.
Dolum Noktası Güzergahı: En yakın dolum noktası en optimize yol üzerinden işaretlenir.
Yazılı Güzergah Gösterimi: Harita dışında, metinsel olarak da güzergah bilgileri sağlanır.
İlçe Seçimi: Kullanıcılar, spesifik bir ilçedeki dolum noktalarına erişebilirler.
Proje Yapısı
1. Flask Framework
Projenin web servisleri ile etkileşime geçmek ve verileri kullanıcıya sunmak için Flask kullanılmıştır. Flask, esnek yapısı ve kolay kullanımı sayesinde projede tercih edilmiştir.
Flask

2. MySQL Veritabanı
Veritabanı yönetim sistemi olarak MySQL kullanılmıştır. Otobüs hatları, duraklar ve dolum noktalarının verilerini saklamak ve yönetmek için kullanılmıştır.
MySQL

3. Google Maps API
Harita üzerinde otobüs duraklarını ve dolum noktalarını göstermek için Google Maps API kullanılmıştır.
Google Maps API

4. HTML, CSS ve JavaScript
Frontend tarafında kullanıcı arayüzünü oluşturmak için HTML, CSS ve JavaScript kullanılmıştır.

Veri Toplama ve İşleme
Veri Toplama: İstanbul Büyükşehir Belediyesi Açık Veri Portalı üzerinden İstanbulKart Dolum Noktaları verilerine erişildi.
Veri İşleme: Veriler, İstanbul'un ilçelerine göre kategorize edildi ve analiz edildi.
Veri Temizleme: Verilerdeki aykırı değerler ve yanlış konumlar temizlendi.
Kurulum
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Depoyu Kopyalayın:

bash
Copy code
git clone https://github.com/kullanici-adi/proje-adi.git
cd proje-adi
Gerekli Bağımlılıkları Yükleyin:

bash
Copy code
pip install -r requirements.txt
Veritabanı Kurulumu:

MySQL üzerinde veritabanınızı oluşturun ve gerekli tabloları oluşturmak için schema.sql dosyasını çalıştırın.

Çevresel Değişkenleri Ayarlayın:

.env dosyasını oluşturun ve aşağıdaki bilgileri ekleyin:

env
Copy code
FLASK_APP=app.py
FLASK_ENV=development
MYSQL_USER=kullanici_adi
MYSQL_PASSWORD=sifre
MYSQL_DB=veritabani_adi
GOOGLE_MAPS_API_KEY=api_key
Uygulamayı Başlatın:

bash
Copy code
flask run

Kaynaklar
İstanbulKart Dolum Noktaları Verileri
Flask Belgeleri
MySQL Workbench
Google Maps API

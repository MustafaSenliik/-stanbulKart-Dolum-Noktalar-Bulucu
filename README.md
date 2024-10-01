Bu proje, İstanbul'daki İstanbulKart dolum noktalarını harita üzerinde görüntülemeye ve kullanıcıların en yakın dolum noktasını bulmasına olanak sağlar. Kullanıcılar, ilçe bazında dolum noktalarını filtreleyebilir ve seçilen iki nokta arasında en kısa rota üzerinden hareket edebilir.

Proje Amacı
Bu uygulamanın amacı, kullanıcıların en yakın İstanbulKart dolum noktalarına hızlıca ulaşmalarını sağlamaktır. Harita tabanlı arayüz sayesinde, kullanıcılar güzergahları görüntüleyebilir ve trafik yoğunluğunu azaltıcı şekilde toplu taşıma kullanımını teşvik edebilir.

Özellikler
İlçeye göre dolum noktalarını listeleme
Harita üzerinde en yakın dolum noktalarını gösterme
Başlangıç ve bitiş noktaları arasındaki en kısa rotayı hesaplama
Rotaların Google Maps üzerinde görselleştirilmesi
Tüm ilçelerdeki dolum noktalarını tek tıkla gösterme
Kullanılan Teknolojiler
Flask (Python): Uygulama sunucusunu oluşturmak ve veri işlemek için kullanıldı.
Google Maps API: Harita üzerinde dolum noktalarını ve rotaları göstermek için kullanıldı.
HTML, CSS, JavaScript: Kullanıcı arayüzünü geliştirmek ve Google Maps entegrasyonu için kullanıldı.
MySQL: Dolum noktaları ve ilçeler hakkındaki verilerin saklandığı veritabanı olarak kullanıldı.
Kurulum ve Kullanım
Gereksinimler:
Python 3.x
Flask
MySQL Veritabanı
Google Maps API Anahtarı

Kurulum Adımları:
Bu depoyu bilgisayarınıza klonlayın:


git clone https://github.com/MustafaSenliik/istanbulkart-dolum-noktalari-bulucu.git
cd istanbulkart-dolum-noktalari-bulucu


Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt

MySQL veritabanınızı yapılandırın ve config.py dosyasındaki ayarları düzenleyin.

Google Maps API anahtarınızı index.html dosyasındaki script etiketine ekleyin.

Uygulamayı çalıştırın:
python app.py

Tarayıcınızda http://localhost:5000 adresine giderek uygulamayı kullanmaya başlayın.

Çevre Değişkenleri:
env
Kodu kopyala
FLASK_APP=app.py
FLASK_ENV=development
MYSQL_USER=kullanici_adi
MYSQL_PASSWORD=sifre
MYSQL_DB=veritabani_adi
GOOGLE_MAPS_API_KEY=api_key

Uygulamayı başlatmak için:
flask run

Testler
Projede çeşitli fonksiyonların doğruluğunu test etmek için birim testler kullanılmıştır. Testler, Flask uygulamanızın düzgün çalışıp çalışmadığını doğrulamak için aşağıdaki adımları izleyin:

Test Edilen Özellikler:
Ana Sayfa Testi: Ana sayfanın doğru şekilde yüklendiğini ve içeriklerin beklendiği gibi görünüp görünmediğini kontrol eder.
Rota Formu Testi: /route-form sayfasının doğru şekilde çalıştığını ve sayfada gerekli bilgilerin yer alıp almadığını doğrular.
get_directions Testi: Google Maps API'den gelen yanıtların doğru olup olmadığını ve mesafe, süre gibi bilgilerin beklendiği gibi işlenip işlenmediğini test eder.
Testleri Çalıştırmak İçin:
Test komutlarını çalıştırın:


python -m unittest discover tests
Test sonuçları, tüm ana işlevlerin doğruluğunu gösterecektir. 
Testler, projenizin sağlamlığını kontrol eder ve hataların erken fark edilmesini sağlar.

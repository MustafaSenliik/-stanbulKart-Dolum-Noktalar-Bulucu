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

bash
Kodu kopyala
git clone https://github.com/kullanici-adi/istanbulkart-dolum.git
cd istanbulkart-dolum
Gerekli bağımlılıkları yükleyin:

bash
Kodu kopyala
pip install -r requirements.txt
MySQL veritabanınızı yapılandırın ve config.py dosyasındaki ayarları düzenleyin.

Google Maps API anahtarınızı index.html dosyasındaki script etiketine ekleyin.

Uygulamayı çalıştırın:

bash
Kodu kopyala
python app.py
Tarayıcınızda http://localhost:5000 adresine giderek uygulamayı kullanmaya başlayın.

Katkıda Bulunma
Katkıda bulunmak istiyorsanız lütfen bir pull request açın. Sorunları bildirmek için issue kısmını kullanabilirsiniz.
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

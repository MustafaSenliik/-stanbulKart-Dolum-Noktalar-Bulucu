# İstanbulKart Dolum Noktaları Bulucu

Bu proje, İstanbul'daki İstanbulKart dolum noktalarını harita üzerinde görüntülemeye ve kullanıcıların en yakın dolum noktasını bulmasına olanak sağlar. Kullanıcılar, ilçe bazında dolum noktalarını filtreleyebilir ve seçilen iki nokta arasında en kısa rota üzerinden hareket edebilir.

## Proje Amacı

Bu uygulamanın amacı, kullanıcıların en yakın İstanbulKart dolum noktalarına hızlıca ulaşmalarını sağlamaktır. Harita tabanlı arayüz sayesinde, kullanıcılar güzergahları görüntüleyebilir ve trafik yoğunluğunu azaltıcı şekilde toplu taşıma kullanımını teşvik edebilir.

## Özellikler

- İlçeye göre dolum noktalarını listeleme
- Harita üzerinde en yakın dolum noktalarını gösterme
- Başlangıç ve bitiş noktaları arasındaki en kısa rotayı hesaplama
- Rotaların Google Maps üzerinde görselleştirilmesi
- Tüm ilçelerdeki dolum noktalarını tek tıkla gösterme

## Kullanılan Teknolojiler

- **Flask (Python)**: Uygulama sunucusunu oluşturmak ve veri işlemek için kullanıldı.
- **Google Maps API**: Harita üzerinde dolum noktalarını ve rotaları göstermek için kullanıldı.
- **HTML, CSS, JavaScript**: Kullanıcı arayüzünü geliştirmek ve Google Maps entegrasyonu için kullanıldı.
- **MySQL**: Dolum noktaları ve ilçeler hakkındaki verilerin saklandığı veritabanı olarak kullanıldı.

## Kurulum ve Kullanım

### Gereksinimler:
- Python 3.x
- Flask
- MySQL Veritabanı
- Google Maps API Anahtarı

### Kurulum Adımları:

1. Bu depoyu bilgisayarınıza klonlayın:
    ```bash
    git clone https://github.com/MustafaSenliik/istanbulkart-dolum-noktalari-bulucu.git
    cd istanbulkart-dolum-noktalari-bulucu
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. MySQL veritabanınızı yapılandırın ve `config.py` dosyasındaki ayarları düzenleyin.

4. Google Maps API anahtarınızı `index.html` dosyasındaki `<script>` etiketine ekleyin.

5. Uygulamayı çalıştırın:
    ```bash
    python app.py
    ```

6. Tarayıcınızda `http://localhost:5000` adresine giderek uygulamayı kullanmaya başlayın.

## Test Araçları ve İzleme

### Test Araçları:
- **Apache JMeter**: Performans testi yapmak için kullanıldı. Farklı yük seviyelerinde uygulamanın ne kadar hızlı ve kararlı çalıştığı test edildi.
- **OWASP ZAP**: Uygulamanın güvenlik açıklarını taramak için kullanıldı. Bu araçla, olası güvenlik zafiyetleri test edildi ve raporlandı.
- **Postman**: API'lerin doğruluğunu ve işlevselliğini test etmek için kullanıldı.

### İzleme:
Proje ayrıca **Prometheus** ve **Grafana** kullanılarak izlenmiştir:

- **Prometheus**: Uygulamanın CPU, bellek kullanımı gibi metriklerini toplamak için kullanıldı.
- **Grafana**: Toplanan metrikler, Grafana üzerinde görselleştirildi ve uygulamanın performansı sürekli olarak takip edildi.

## Çevre Değişkenleri

Aşağıdaki çevre değişkenlerini `.env` dosyasına ekleyin:

```env
FLASK_APP=app.py
FLASK_ENV=development
MYSQL_USER=kullanici_adi
MYSQL_PASSWORD=sifre
MYSQL_DB=veritabani_adi
GOOGLE_MAPS_API_KEY=api_key

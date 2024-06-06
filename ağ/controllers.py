from flask import Flask, request, jsonify, render_template
from services import LocationService
from models import db
import requests 

app = Flask(__name__)  # Flask uygulaması oluşturuluyor
app.config.from_object('config.Config')  # Uygulama yapılandırması config.Config sınıfından alınıyor
db.init_app(app)  # Veritabanı (SQLAlchemy) uygulamaya entegre ediliyor

location_service = LocationService()  # LocationService sınıfı örnekleniyor

@app.route('/')
def index():
    return render_template('index.html')  # Ana sayfa şablonu render ediliyor

@app.route('/route-form')
def route_form():
    return render_template('route_form.html')  # Yol tarifi formu şablonu render ediliyor

@app.route('/find-route', methods=['POST'])
def find_route():
    start_location = request.form['start_location']  # Formdan başlangıç noktası alınıyor
    end_location = request.form['end_location']  # Formdan bitiş noktası alınıyor
    
    # Google Maps Directions API kullanarak yol tarifini alalım
    directions, distance, duration = get_directions(start_location, end_location)
    
    # Yol tarifi sonuçları render ediliyor
    return render_template('route_result.html', directions=directions, start_location=start_location, end_location=end_location, distance=distance, duration=duration)

def get_directions(start, end):
    api_key = 'AIzaSyANPSC0RwsohmuBId_TUsbVIF15XGGIXIU'  # Google Maps API anahtarınızı buraya ekleyin
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&key={api_key}'
    response = requests.get(url)  # Google Maps Directions API'ye istek yapılıyor
    directions = response.json()  # API cevabı JSON formatına dönüştürülüyor
    
    if directions['status'] == 'OK':
        distance = directions['routes'][0]['legs'][0]['distance']['text']  # Mesafe bilgisi alınıyor
        duration = directions['routes'][0]['legs'][0]['duration']['text']  # Süre bilgisi alınıyor
        return directions, distance, duration  # Yol tarifi, mesafe ve süre bilgileri döndürülüyor
    else:
        return None, None, None  # Yol tarifi alınamazsa None değerler döndürülüyor

@app.route('/locations', methods=['GET'])
def get_all_locations():
    locations = location_service.get_all_locations()  # Tüm lokasyonlar alınıyor
    return jsonify([location.to_dict() for location in locations])  # Lokasyonlar JSON formatında döndürülüyor

@app.route('/locations/<string:town_id>', methods=['GET'])
def get_locations_by_town_id(town_id):
    locations = location_service.get_locations_by_town_id(town_id)  # Belirli bir town_id'ye göre lokasyonlar alınıyor
    return jsonify([location.to_dict() for location in locations])  # Lokasyonlar JSON formatında döndürülüyor

@app.route('/nearest-locations', methods=['GET'])
def find_nearest_locations():
    latitude = request.args.get('latitude', type=float)  # İstekten enlem değeri alınıyor
    longitude = request.args.get('longitude', type=float)  # İstekten boylam değeri alınıyor
    locations = location_service.find_nearest_locations(latitude, longitude)  # En yakın lokasyonlar bulunuyor
    return jsonify([location.to_dict() for location in locations])  # Lokasyonlar JSON formatında döndürülüyor

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Veritabanı tabloları oluşturuluyor
    app.run(debug=True, port=5011)  # U

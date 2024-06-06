from controllers import app  # controllers.py dosyasından Flask uygulamasını içe aktarın
from flask_cors import CORS
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


CORS(app)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5011)  # Flask uygulamasını başlatın

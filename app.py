from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Modeli yükle
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Formdan gelen verileri al (Sırasıyla: m2, oda, banyo, yıl, arsa, garaj)
        # HTML'deki input isimleri (name="...") ile burası eşleşmeli
        square_footage = float(request.form['Square_Footage'])
        num_bedrooms = int(request.form['Num_Bedrooms'])
        num_bathrooms = int(request.form['Num_Bathrooms'])
        year_built = int(request.form['Year_Built'])
        lot_size = float(request.form['Lot_Size'])
        garage_size = int(request.form['Garage_Size'])

        # Modelin beklediği formatta diziye çevir
        final_features = [np.array([square_footage, num_bedrooms, num_bathrooms, year_built, lot_size, garage_size])]
        
        # Tahmin yap
        prediction = model.predict(final_features)
        
        # Sonucu yuvarla (Örn: 250000.50)
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='Tahmini Ev Fiyatı: $ {}'.format(output))
    
    except Exception as e:
        return render_template('index.html', prediction_text='Hata oluştu: {}'.format(e))

if __name__ == "__main__":
    app.run(debug=True)
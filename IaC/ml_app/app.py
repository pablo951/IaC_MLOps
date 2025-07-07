#Criação de API e front-end para modelo de Machine Learning

# Imports 
from flask import Flask, request, render_template
import joblib



# App
app = Flask(__name__)

# Carrega o modelo treinado 
final_model = joblib.load('trained_model.pkl')

# Rota da página de entrada
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    # Recebe os novos dados de entrada
    features = [float(x) for x in request.form.values()]

    # Prepara a lista dos atributos
    final_features = [features]

    # Previsão com o modelo treinado 
    prediction = final_model.predict(final_features)

    return render_template('index.html', prediction_text = f'Previsão do Modelo (1 - Cliente Fará Outra Compra / 0 - Cliente Não Fará Outra Compra): {prediction[0]}')

# Executa o programa 
if __name__ == '__main__':
    app.run(debug=True)

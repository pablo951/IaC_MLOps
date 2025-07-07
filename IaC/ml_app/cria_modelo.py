# Imports
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib 


# Geração de um conjunto de dados fictícios 

X,y=make_classification(n_samples= 10000, n_features= 4 , random_state= 42)

# Dividindo os dados em conjunto de treino e teste

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size= 0.2, random_state= 42)

# Criando e treinando o modelo de regressão logistica
model = LogisticRegression()
model.fit(X_train,y_train)

# Avaliando o modelo 
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print(f'Acurácia do Modelo: {accuracy}')

# Salvando o modelo 
joblib.dump(model, 'trained_model.pkl')
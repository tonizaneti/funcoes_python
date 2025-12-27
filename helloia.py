import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 0=all, 1=warnings, 2=errors, 3=errors críticos

import tensorflow as tf
import numpy as np;

#Dados e entrada (x) e saída esperada (y)
x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([-2.0, 0.0, 2.0, 4.0, 6.0, 8.0])

# Reshape x para formato adequado (n_samples, n_features)
x = x.reshape(-1, 1)

#Modelo (jeito moderno)
model = tf.keras.Sequential([ 
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

#Compilação do modelo com otimizador e função de perda
model.compile(
    optimizer='sgd',
    loss='mean_squared_error'
)

#Treinamento
model.fit(x, y, epochs=500, verbose=0)

#Teste 
print("Previsao para x=10:")
print(model.predict(np.array([[10.0]])))

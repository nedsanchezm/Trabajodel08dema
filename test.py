#Archivo para probar las rutas

import requests

misDatos={ 'numero1':45, 'numero2':18}

respuesta= requests.post('http://localhost:5500/sumar', json=misDatos)
print=("El valor de la suma es " ) 

respuesta= requests.post('http://localhost:5500/restar', json=misDatos)
print=("El valor de la resta es " ) 

respuesta= requests.post('http://localhost:5500/dividir', json=misDatos)
print=("El valor de la división es " ) 

respuesta= requests.post('http://localhost:5500/multiplicar', json=misDatos)
print=("El valor de la multiplicación es " ) 
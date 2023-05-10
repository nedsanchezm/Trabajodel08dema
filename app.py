#API Flask

from flask import *

#Crear un objeto de la clase Flask

app= Flask(__name__)

#Ruta para enviar un formulario al frontend


#Definir las rutas
@app.route('/sumar', methods= ['POST'])

def sumar():
    
    misDatos= request.get_json()
    n1=misDatos ['numero1']
    n2=misDatos ['numero2']

    resultado= n1+n2
    
    return jsonify({ 'resultado': resultado})

@app.route('/restar' , methods= ['POST'])

def restar():
    
    misDatos= request.get_json()
    n1=misDatos ['numero1']
    n2=misDatos ['numero2']

    resultado= n1-n2
    
    return jsonify({ 'resultadp': resultado})

@app.route('/dividir' , methods= ['POST'])

def dividir():
    
    misDatos= request.get_json()
    n1=misDatos ['numero1']
    n2=misDatos ['numero2']

    resultado= n1/n2
    
    return jsonify({ 'resultadp': resultado})

@app.route('/multiplicar' , methods= ['POST'])

def multiplicar():
    
    misDatos= request.get_json()
    n1=misDatos ['numero1']
    n2=misDatos ['numero2']

    resultado= n1*n2
    
    return jsonify({ 'resultado': resultado})




#Ejecutar el servidor

app.run()

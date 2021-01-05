from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# para iniciar el servidor deberemos acceder al cmd del terminal ir al escritorio(en nuestro caso es donde se encuentra el servidor) y poner la siguiente comanda: <venv>\Scripts\activate.bat
# para desactivar vamos al cmd y dentro del escritorio pondremos la siguiente comanda: deactivate
# Ahora tendremos que iniciar el servidor con su archivo.py llamdo (server.py) con la siguientes comandas: set FLASK_APP=server.py y despues: Flask run (Importante saber que tienes que encontrate dentro de la carpeta donde se encuetr el archivo server.py)
# Una vez iniciado nos dara una Ip, solo tendremos que ponerla en el buscador y se nos abrira el server.
# Si queremos que todos los cambios se guarden lo podremos hacer con la siguiente comanda:set FLASK_ENV=development (Importante tner en cuenta que es set porque estamos en windows, sino seria export siendo apple)


@app.route('/')
def my_home():
    return render_template('index.html')

# con este codigo podremos poner link a todos los enalces de una manera automatica.


@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)

# Vamos a crear un archivo de texto (txt) dentro de la carpeta del proyecto y con este metodo podremos recojer los datos del formulario y enviarlos al archivo nuevo database.txt


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_cvs(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        cvs_write = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cvs_write.writerow([email, subject, message])


@app.route('/submit_from', methods=['POST', 'GET'])
def submit_from():
    if request.method == 'POST':
        try:
            # con el metodo to_dict cojeremos todos los datos y los pondremos en un diccionario.
            data = request.form.to_dict()
            # Para iniciar el metodo el poner la información en el archivo txt
            # write_to_file(data)
            # Llamando el metodo para poner la infromacion del from en el archivo csv
            write_to_cvs(data)
            return redirect('/thanks.html')
        except:
            return 'something went wrong. Try again!'
    else:
        return 'something went wrong, try again!'

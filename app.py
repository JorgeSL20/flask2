from flask import Flask, request, render_template_string, url_for

app = Flask(__name__)

# Plantilla HTML para el formulario con Bootstrap
form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcular IMC</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Calcular IMC</h1>
        <form action="/calculate" method="POST" class="mt-3">
            <div class="form-group">
                <label for="weight">Peso (kg):</label>
                <input type="text" id="weight" name="weight" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="height">Altura (m):</label>
                <input type="text" id="height" name="height" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Calcular IMC</button>
        </form>
        <div class="mt-4">
            <p>Nombre: Jorge Leonardo Seydlitz Lugo</p>
            <p>Matrícula: 20201175</p>
            <p>Grupo: B</p>
            <p>Grado: 9° Cuatrimestre</p>
        </div>
    </div>
</body>
</html>
'''

# Plantilla HTML para el resultado con Bootstrap y la imagen
result_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado del IMC</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Resultado del IMC</h1>
        <p class="lead">Tu IMC es: {{ bmi }}</p>
        <a href="/" class="btn btn-primary">Volver al formulario</a>
        <div class="mt-4">
            <img src="{{ url_for('static', filename='Tabla-IMC.jpg') }}" alt="Tabla de IMC" class="img-fluid">
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(form_html)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        if height <= 0:
            raise ValueError("Height must be greater than zero")

        bmi = weight / (height ** 2)
        return render_template_string(result_html, bmi=bmi)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

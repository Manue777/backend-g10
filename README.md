# Repositorio del Backend de CodiGo

<p align="center">
    <img src="https://codigo.edu.pe/public/img/codigo-logo.png">
</p>

## Este sera el repositorio del curso por las siguientes 10 semanas

Toda la informacion la podras encontrar aquí y en los links dados por el Discord

Cada semana esta en una rama independiente, en la cual se ira detallando a continuación:
Por ejemplo: semana 03, semana 04 y asi sucesivamente , para ver ingresa al link siguientes
- Semana 03: <a href="https://github.com/Manue777/backend-g10/tree/semana03">LINK</a>
- Semana 04: <a href="https://github.com/Manue777/backend-g10/tree/semana04">LINK</a>
- Semana 05: <a href="https://github.com/Manue777/backend-g10/tree/semana05">LINK</a>
- Semana 06: <a href="https://github.com/Manue777/backend-g10/tree/semana06">LINK</a>
- Semana 07: <a href="https://github.com/Manue777/backend-g10/tree/semana07">LINK</a>
- Semana 08: <a href="https://github.com/Manue777/backend-g10/tree/semana08">LINK</a>
- Semana 09: <a href="https://github.com/Manue777/backend-g10/tree/semana09">LINK</a>
- Semana 10: <a href="https://github.com/Manue777/backend-g10/tree/semana10">LINK</a>

## Crear el entorno virtual

```
python -m venv venv
```

## Activar el entorno virtual

```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
```

## Instalar Django

```
pip install Django
pip freeze > requirements.txt
```

## Crear nuestro proyecto

```
django-admin startproject django_intro
```

## Correr el servicio

```
cd django_intro
python manage.py runserver
```

## Migrar los modelos

```
python manage.py migrate
```

## Crear un superusuario

```
python manage.py createsuperuser
```

## Crear una app

```
python manage.py startapp almacen
```

## Registramos nuestra app en INSTALLED_APPS

```python
INSTALLED_APPS = [
    ...,
    'almacen'
]
```

## Crear nuestro nuevo model y migrar

```
python manage.py makemigrations
python manage.py migrate
```

## Instalar Django Rest Framework

```
pip install djangorestframework
```

## Agregar DRF a INSTALLLED_APPS

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
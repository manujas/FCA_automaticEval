# FCA_automaticEval
Primeras armas en Python para Fundación Conocimiento Abierto
Se crea una mínima (y algo fea) interfaz sobre el API de CKAN impactando al [portal de datos abiertos del gobierno de Argentina](http://www.datos.gob.ar)


## Preparando el entorno de trabajo (virtualenv)

Instalación de virtualenv:  [http://hosseinkaz.blogspot.com.ar/2012/06/how-to-install-virtualenv.html](http://hosseinkaz.blogspot.com.ar/2012/06/how-to-install-virtualenv.html)

```
mkvirtualenv fca_crm
git clone https://github.com/manujas/FCA_automaticEval
```

### Instalar las dependencias del proyecto

```
cd FCA_automaticEval
pip install -r requirements.txt
```

### Genera tu propia SECRECT_KEY
Ingresa a [Django secret_key generator](http://www.miniwebtool.com/django-secret-key-generator/) y genera una key random para usar en el proyecto

En la terminal, dentro del directorio `mysite/mysite` ejecuta:
```
mv secret.example secret.py
```
Abre el archivo secret.py y remplaza el valor de SECRECT_KEY por la generada anteriormente.

### Inicia el servidor
```
python manage.py runserver
```

Puedes acceder en [http://localhost:8000/ckan_search](http://localhost:8000/ckan_search)

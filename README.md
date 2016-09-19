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


### Inicia el servidor
```
python manage.py runserver
```

Puedes acceder en [http://localhost:8000/ckan_search](http://localhost:8000/ckan_search)

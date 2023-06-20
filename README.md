# Monte Piadoso
Este proyecto Rest CRUD se divide en dos aplicaciones, una en Django y otra en React.

### Aplicación hecha en Django

En la carpeta del proyecto se debe instalar un entorno virtual con `python3 -m venv nombre_del_environment`

Luego se deben instalar las siguientes dependencias en el entorno virtual: 

`pip3 install django django-bootstrap-v5 djangorestframework django-cors-headers`

Después, en la carpeta del cproject_monte, donde esta el archivo **manage.py**, abrir un servidor con `python3 manage.py runserver`

Y el servidor se cargará en el puerto **localhost:8000**

### Aplicación hecha en React

Esta app hará llamadas hacia la API hecha en Django, por lo que primero se deberá abrir el servidor de Django.

El código de react esta en la carpeta `project_monte/cproject_monte/monte_piadoso_front`

Se debe tener instalado node.js

Para ver la app se sugiere abir un servidor con `serve`. Para instalarlo solo hay entrar en la carpeta `cd monte_piadoso_front` y teclear en la terminal 
>npm install -g serve

>serve -s build

Esto abrirá un servidor en el puerto **localhost:3000** y se podrá interactuar con la API de Django

### Imagenes de la App de Django

![Captura de pantalla 2023-06-12 a la(s) 17 04 30](https://github.com/Jazperist/project_monte/assets/39943709/35228c66-dc13-46f8-8c51-7ce3305bd0bd)


![Captura de pantalla 2023-06-12 a la(s) 17 06 07](https://github.com/Jazperist/project_monte/assets/39943709/11170e08-d8e4-4a6c-9e8a-a3227adba45d)

![Captura de pantalla 2023-06-12 a la(s) 17 06 33](https://github.com/Jazperist/project_monte/assets/39943709/676cfd05-4761-4680-9cc6-bc56a13c50e7)

![Captura de pantalla 2023-06-12 a la(s) 17 09 44](https://github.com/Jazperist/project_monte/assets/39943709/ac0fabdf-801a-4bd4-aea4-4ee482072c57)

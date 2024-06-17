# Colegio Sagrada Reprobación

## Introducción
Hola a todos, este es mi primer proyecto como desarrollador back end. El proyecto "Colegio Sagrada Reprobación" es un sistema de gestión integral para colegios 
que incluye funcionalidades CRUD (Crear, Leer, Actualizar, Eliminar) para la administración de matrículas y registros de empleados. El sistema también ofrece gestión de roles 
y acceso diferenciado, proporcionando un entorno seguro y eficiente para la administración escolar.

## Descripción del Proyecto
El sistema de administración de "Colegio Sagrada Reprobación" está diseñado para facilitar la gestión de diversas operaciones escolares. Las principales características del sistema incluyen:

- **Acciones CRUD**: Permite la creación, lectura, actualización y eliminación de registros de empleados y matrículas de alumnos.
- **Sistema de Roles**: Diferencia entre distintos roles de usuarios, como administradores y empleados, controlando el acceso a diferentes partes del sistema.
- **Gestión de Matrículas**: Registra y administra las matrículas de los estudiantes, permitiendo un seguimiento detallado de la información académica.
- **Registro de Empleados**: Maneja la información del personal del colegio, facilitando la gestión de recursos humanos.
- **Interfaz de Administración**: Proporciona una interfaz administrativa para usuarios con permisos especiales, permitiendo una gestión avanzada de todas las operaciones del sistema.
- **Autenticación y Seguridad**: Sistema de login seguro con control de acceso basado en roles, garantizando que la información sensible esté protegida.

El objetivo principal de este proyecto es crear una herramienta eficiente y segura para la administración escolar, mejorando la organización y facilitando las tareas administrativas cotidianas.


## Pre-requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

**Python** (3.8 o superior): Necesario para ejecutar Django y otros scripts en Python. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

**Django** (3.2 o cualquier versión que hayas utilizado): Un framework de alto nivel para desarrollo web en Python. Instálalo utilizando pip:
pip install Django==3.2

**MariaDB** o **MySQL**: Utilizado como sistema de gestión de bases de datos. Asegúrate de tener MariaDB o MySQL instalado y corriendo en tu sistema. Puedes seguir las instrucciones de instalación en [MariaDB](https://mariadb.org/download/) o [MySQL](https://dev.mysql.com/downloads/mysql/).

**Driver de MySQL para Python** (mysqlclient): Necesario para conectar Django con la base de datos MySQL/MariaDB. Instálalo con pip:
pip install mysqlclient

## Configuración adicional

Dependiendo de tu configuración de Django y la base de datos, podrías necesitar realizar configuraciones adicionales en tu archivo `settings.py` de Django para conectar correctamente a la base de datos:


1. Configure your Database:
   - Ensure MariaDB (or MySQL) is installed and running on your machine.
   - Set up database credentials and connection in the 'settings.py' file of your Django project under 'DATABASES'.
   - Example configuration:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_database_name',
             'USER': 'your_username',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',  // or the database server IP
             'PORT': '3306',
         }
     }

2. Perform Initial Migrations:
   - Django uses a migration system to adapt your database to the models defined in your application.
   - Execute the following commands to prepare your database:
     python manage.py makemigrations
     python manage.py migrate

3. Create a Superuser: (optional)
   - Django has a powerful administrative interface for managing your site’s content.
   - Create a superuser to access the admin panel:
     python manage.codecresuperuser
   - Follow the prompts to set up a username and password.

4. Start the Development Server:
   - Check that everything is set up correctly by starting the development server:
     python manage.coderunserver
   - Visit http://127.0.0.1:8000/ in your browser to see if the project is running.

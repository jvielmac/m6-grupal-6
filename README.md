# Trabajo Grupal 6

## Levantamiento del servidor

En un entorno con Django y Django-crispy-forms instalados. posicionarse sobre el directorio raíz del proyecto y ejecutar el siguiente comando `python manage.py [puerto]`. Si el puerto se omite será 8000 por defecto.

## Desarrollo del trabajo

Se elabora una nueva página con un formulario que guarda la información de los proveedores que tienen interés en colaborar con nuestra aplicación.

Se elabora toda la estructura necesaria para guardar la información del formulario en la base de datos. 

Se crea un nuevo template de registro, para que los usuarios de la aplicacion puedan registrarse [Template Registro](usuarios/templates/usuarios/registro.html)

Se crea template de login, para que los usuarios registrados puedan acceder a su cuenta [Template Login](usuarios/templates/usuarios/login.html)

A cada usuario se le muestra un mensaje de bienvenida una vez que accedan a su cuenta [Mensaje Bienvenida](usuarios/templates/usuarios/perfil.html)

Se crean tres grupos de usuarios con permisos diferenciados sobre los datos del sitio. Estos grupos pueden asignarse de forma dinámica al momento de crear un nuevo usuario.

### Archivos de interes del proyecto

[Forms](usuarios/forms.py) | [Views](usuarios/views.py) | [Models](Clientes/models.py) 
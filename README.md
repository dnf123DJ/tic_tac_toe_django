# Juego de Tic Tac Toe en Django

Este proyecto implementa un juego de Tic Tac Toe utilizando Django y Rest Framework.

## Requisitos

* Python (versión 3.12.0)
* Django (versión 5.0)
* Django Rest Framework (versión 3.14.0)
* Pytz (versión 2023.3.post1)
* Sqlparse (versión 0.4.4)
* Tzdata (versión 2023.3)

## Configuración

1. Clona el repositorio:

``` bash
git clone https://github.com/dnf123DJ/tic_tac_toe_django.git
cd tu-proyecto
```

2. Instala las dependencias:

``` bash
pip install -r requirements.txt
```

3. Ejecuta las migraciones:

``` bash
python manage.py migrate
```

4. Crea un superusuario:

``` bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear un superusuario.

## Ejecutar en Localhost

Asegúrate de que el servidor de desarrollo de Django esté en funcionamiento:

``` bash
python manage.py runserver
```

Si alguna vez olvidas la contraseña del superusuario o necesitas restablecerla, puedes utilizar el siguiente comando:

``` bash
python manage.py changepassword <nombre_de_usuario>
```

Para poder ejecutar los test:

``` bash
python manage.py test
```
## Ejemplos de Solicitudes

1. Obtener token:

``` bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "tu_usuario", "password": "tu_contraseña"}' http://localhost:8000/api/token/
```

2. Iniciar un Juego:

``` bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token TU_TOKEN_DE_AUTENTICACION" http://localhost:8000/start_game/USUARIO_JUGADOR2/
```

3. Realizar un Movimiento:

``` bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token TU_TOKEN_DE_AUTENTICACION" http://localhost:8000/make_move/ID_JUEGO/POSICION/
```

4. Obtener Estado del Tablero:

``` bash
curl -H "Content-Type: application/json" -H "Authorization: Token TU_TOKEN_DE_AUTENTICACION" http://localhost:8000/get_board_state/ID_JUEGO/
```

5. Obtener Puntuaciones:

``` bash
curl -H "Content-Type: application/json" -H "Authorization: Token TU_TOKEN_DE_AUTENTICACION" http://localhost:8000/get_scores/
```

6. Obtener Registro del Juego:

``` bash
curl -H "Content-Type: application/json" -H "Authorization: Token TU_TOKEN_DE_AUTENTICACION" http://localhost:8000/get_game_log/ID_JUEGO/
```

Asegúrate de reemplazar TU\_TOKEN\_DE\_AUTENTICACION con tu token de autenticación real, y sigue las instrucciones específicas de tu proyecto.

Las posiciones del tablero se encunetran entre 0 y 8

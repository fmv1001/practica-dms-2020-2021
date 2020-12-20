# DMS 2020-2021 Client application

This applicationserves as the control console for the different services of the appliance.

## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2021client/config.yml`. This path is thus usually `${HOME}/.config/dms2021client/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `debug`: If set to true, the service will run in debug mode.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.
- `sensors`: A dictionary with the configuration needed to connect to the different sensor services. Each key identifies a sensor, and their values are themselves dictionaries with the connection information:
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

Just run `dms2021client` as any other program.

## Funcionalidad

Este servicio nos permite ejecutar la aplicacion en la que podemos realizar las siguientes acciones mostradas en el menu:

- `Crear usuarios`: Si el usuario con el que se ha hecho el login tiene el permiso `AdminUsers`, podra crear usuarios que seran anadidos al sistema. Este usuario se inicia sin permisos y es anadido en la base de datos del servicio de autentificacion. Las credenciales del nuevo usuario se pediran por pantalla.
- `Cambiar permisos de un usuario`: Si el usuario con el que se ha hecho el login tiene el permiso `AdminRights`, podra cambiar los permisos de un usuario que sera modificado en el sistema. Los cambios son anadidos en la base de datos del servicio de autentificacion. Las credenciales del usuario a cambiar los permisos y el permiso a modificar se piden por pantalla.
- `Obtener los resultados de un sensor`: Si escogemos esta opcion se mostrara un menu con los diferentes sensores de los que dispone el sistema y podremos elegir de que sensor queremos obtener su valor, esta opcion se pide por pantalla. 
  - Si escogemos el `sensor de memoria RAM`, nos muestra el valor de la memoria RAM usuada del sistema. 
  - Los demas sensores nos mostraran un mensaje indicando que no estan implementados en el sistema. Seran implementados en proximas versiones.
- `Actualizar los resultados de un sensor`: se actualizara el valor del sensor deseado (escogido por pantalla). Como se ha mencionado, solo esta implementado el sensor de memoria RAM, los demas sensores no estan disponibles en esta version.
- `SALIR`: se cerrara la sesion del usuario actual y con ello el programa.

## Arquitectura y diseno del cliente

- Descripcion de la arquitectura y diseno del cliente
  
  - Diseno basado en el modelo-vista-controlador (MVC)
  
  - La arquitectura del servicio del sensor se divide en 3 carpetas. 
    - Una primera carpeta de datos (`data`) que contine la configuracion del servicio del cliente en la carpeta `config`, y una carpeta rest que contienelos servicios para la cominicacion con el servicio de autentificacion y el servicio de los sensores.
    - Una carpeta llamada `logic` que no es usada, pero en proximas actualizaciones se estructuraran los metodos de la funcionalidad del cliente en archivos que se ubicaran en esta carpeta.
    - Una ultima carpeta que implementa la capa de presentacion (`presentation`). Dentro de ella encontramos dos archivos.
      - `menuOpciones` que contiene el menu con las opciones de la funcionalidad del sistema.
      - `logoutService` que implementa el cierre de la sesion actual y con ello el cierre del sistema.
  
- Diagrama UML de la arquitectura del cliente
  - En la siguiente imagen podemos ver el diagrama UML que muestra la estructura interna del servicio del cliente

    - ![Alt text](Diagrama_Cliente.png?raw=true "Diagrama UML Cliente")

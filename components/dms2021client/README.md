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
  - Si escogemos el `sensor del sistema`: nos muestrara las reglas (si estan habilitadas) que monitoriza este sensor:
    - La memoria RAM usada.
    - La memorio del disco usada.
    - La memoria SWAP usada.
    - El porcentaje de CPU usado.
  - Si escogemos el `sensor de un directorio`: nos muestrara las reglas (si estan habilitadas) que monitoriza este sensor:
    - La ruta del directorio (Esta monitorizando `/home`)
    - Si existe o no el directorio monitorizado
    - La memoria que ocupa el archivo en el disco.
    - La fecha de modificacion mas reciente.
- `Actualizar los resultados de un sensor`: se actualizara el valor del sensor deseado (escogido por pantalla).
- `Cambiar las reglas de un sensor`: con esta opcion podremos cambiar las reglas de monitorizacion de cada uno de los sensores, esto se podra hacer si disponemos de los permisos necesarios, en este caso `AdminRules`.
- `LogOut`: Permite que cerremos la sesion del usuario con el que hemos accedido, e iremos a la pantalla de inicio.
- `LogOut and exit`: se cerrara la sesion del usuario actual y con ello el programa.

## Arquitectura y diseno del cliente

- Descripcion de la arquitectura y diseno del cliente
  
  - Diseno basado en el modelo-vista-controlador (MVC)
  
  - La arquitectura del servicio del sensor se divide en 3 carpetas. 
    - Una primera carpeta de datos (`data`) que contine:
      - La configuracion del servicio del cliente (`clientconfiguration`) en la carpeta `config`.
      - Una carpeta `rest` que contienelos servicios para la cominicacion con el servicio de autentificacion y el servicio de los sensores (`authservice`, `sensorservice`) y una carpeta `exc` con las excepciones que puedan lanzarse.
      - `actualizarSensore`: este archivo se encarga de mandar la orden de actualizar los sensores y obtener los datos de estos.
      - `consultarSensore`: este archivo se encarga de mandar la orden de consultar los sensores y obtener los datos de estos.
      - `cambiarReglas`: este archivo se encargar de cambiar las reglas de un sensor si se tienen los permisos necesarios (`AdminRules`).
      - `crearUsuario`: este archivo manda la orden de crear un archivo si se tienen los permisos necesarios (`AdminUsers`).
      - `modificarPermisos`: este archivo manda la orden de modificar los permisos de un usuario si se tienen los permisos necesarios (`AdminRights`).
      - `loginApp`: este archivo se encarga de mandar la orden de login de un usuario.
      - `logoutApp`: este archivo se encarga de mandar la orden de log out de un usuario.

    - Una carpeta llamada `logic` que no es usada.

    - Una ultima carpeta que implementa la capa de presentacion (presentation). Dentro de ella encontramos los siguientes archivos:
      - `actualizarSensoresPresentacion`: responsable de la interfaz correspondiente a actualizar un sensor.
      - `cambiarReglasPresentacion`: responsable de la interfaz correspondiente a cambiar las reglas de un sensor.
      - `consultarSensoresPresentacion`: responsable de la interfaz de consultar los sensores.
      - `crearUsuarioPresentacion`: responsable de la interfaz de crear un usuario.
      - `interfazPorMenues`: responsable de la interfaz correspondiente a la aplicacion.
      - `loginAppPresentacion`: responsable de la interfaz correspondiente al login.
      - `logoutAppPresentacion`: responsable de la interfaz correspondiente a un logOut.
      - `menuInicial`: responsable de la interfaz del menu inicial.
      - `menuPrincipal`: responsable de la interfaz del menu principal.
      - `modificarPermisosPresentacion`: responsable de la interfaz correspondiente a la modificacion de permisos.
      - `visualizacionSensor`: responable de mostrar los datos de los sensores.
  
- Diagrama UML de la arquitectura del cliente
  - En la siguiente imagen podemos ver el diagrama UML que muestra la estructura interna del servicio del cliente

   ![Alt text](Diagrama_Cliente.png?raw=true "Diagrama UML Cliente")

  ## Patrones de diseno

- Principios SOLID:
  - Single responsibility: La división del programa nos permite cambiar las partes del código que queramos sin afectar a otras.
  - Open/Close: el código está pensado para que si quieremos extender este se pueda hacer utilizando herencia sin modificar otras clases.
  - Liskov substitution: 
  - Interface segregation: 
  - Dependency inversion: 

- Fachada: debido a que dentro del cliente utilizamos una interfaz para ocultar toda la complegidad del la comunicacion del cliente con los demas servicios, consideramos que hemos aplicado el metodo de fachada.
- Singleton: authservice y sensorservice son instancioados unicamente en `interfazpormenues` teniendo desde ese archivo un acceso global a estos. Al igual que con las clases de la carpeta de data y de presentacion.
- 





  ## Code structure

- `bin`/: En este apartado instanciamos las clases necesarias y agregamos nuestras especificaciones REST.
- dms2021client/: Paquete principal.
  - `data`/: Se encarga de todo el tratamiento de los datos para cada función que implementa la aplicación.
    - `config`/: Este fichero contiene la configuración del cliente, donde se incluye el tratamiento del puerto, host y valores de los sensores.
    - `rest`/: Aqui se da la comunicación con el servicio auth y el servicio sensor.
      - `exc`/: Excepciones usadas en los servicios de auth y sensor (invalidcredentialserror, unauthorizederror)
  - `logic`/: Vacio
  - `presentation`/: Este archivo es muy importante ya que contiene todas las interfaces que permiten al cliente usar la aplicación ocultandole toda la complegidad de esta. Nos gustaria destacar el archivo `interfazPorMenues` ya que es el punto desde el que el usuario trabaja con la aplicación.

## Protocolo de comunicaciones cliente-servidor

  - `InterfazPorMenues` recoge de `ClientConfiguration` todo lo necesario para establecer una conexión con los  servicios de sensores y el servicio de autenticacion.
  - La clase `InterfazPorMenues` hace uso de las clases `AuthService` y `SensorService` para poder ejecutar los servicios de autenticación y los servicios que proporcionan los sensores.

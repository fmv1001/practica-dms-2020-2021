# DMS 2020-2021 Sensor Service

This service provides sensing functionalities to the appliance.

## Installation

Run `./install.sh` for an automated installation.

To manually install the service:

```bash
# Install the service itself.
./setup.py install
```

## Configuration

Configuration will be loaded from the default user configuration directory, subpath `dms2021sensor/config.yml`. This path is thus usually `${HOME}/.config/dms2021sensor/config.yml` in most Linux distros.

The configuration file is a YAML dictionary with the following configurable parameters:

- `db_connection_string` (mandatory): The string used by the ORM to connect to the database.
- `host` (mandatory): The service host.
- `port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.
- `salt`: A configurable string used to further randomize the password hashing. If changed, existing user passwords will be lost.
- `auth_service`: A dictionary with the configuration needed to connect to the authentication service.
  - `host` and `port`: Host and port used to connect to the service.

## Running the service

Just run `dms2021sensor` as any other program.

## REST API specification

This service exposes a REST API so other services/applications can interact with it.

- `/` [`GET`]

  Status verification.
  - Returns:
    - `200 OK` if the service is running.
- `/consultarsensor/<string:tipo_sensor>` [`GET`]

  Sensor value query.
  - Parameters:
    - `tipo_sensor` [path] (`str`): The sensor type.
  - Returns:
    - `200 OK` if the sensor was obtained successfully. The response content (`str`) is a string containing the sensor value.
- `/actualizarsensor/<string:tipo_sensor>` [`POST`]

  Sensor value update.
  - Parameters:
    - `tipo_sensor` [path] (`str`): The sensor type.
  - Returns:
    - `200 OK` if the sensor was updated successfully. The response content (`str`) is a string containing the new sensor value.

- `/actualizarreglas/<string:tipo_sensor>/reglas/<string:regla>` [`POST`]
  Sensor value update.
  - Parameters:
    - `tipo_sensor` [path] (`str`): The sensor type.
    - `regla` [path] (`str`): The rule tpye
  - Returns:
    - 200 OK if the sensor was updated successfully. The response content (str) is a string containing the new sensor value.

  ## Arquitectura y diseno del sensor

- Descripcion de la arquitectura y diseno del sensor
  
  - Diseno basado en el modelo-vista-controlador (MVC)
  
  La arquitectura del servicio del sensor se divide en 3 carpetas.
    -Una primera carpeta de datos (data) que contine la configuracion del servicio del 
    sensor en la carpeta config y la carpeta de la case de datos (db) que no es usada 
    debido a que creamos los sensores como instancias de objetos y obtenemos sus datos 
    con sus propios metodos y no mediante una bases de datos.

    -Una carpeta llamada logic que contiene la logica de negocio del sensor.
    Dentro de ella encontramos los sensores sensor1, sensor2.
    Estos implementan algun tipo de monitorizacion del sistema.
    El sensor1 calcula la memoria RAM usuada, la memoria swap, el disco usado en ese momento y el porcentaje de CPU. Todas estas caracteristicas del sistema en el momento que se instancia el objeto y esta podra ser actualizada. Tambien encontramos el fichero sensorAbs que implementa la clase
	  abstracta de la que heredan los sensores del sistema marcando su estructura interna minima.

    -Una ultima carpeta que implementa la capa de presentacion (presentation). Dentro 
    de ella encontramos la carpeta rest que contiene el archivo sensorrest que 
    implementa el API Rest del servicio sensor. Esta implementacion permite la conexion 
    con los demas servicios del sistema.
  
- Diagrama UML de la arquitectura del sensor
  - En la siguiente imagen podemos ver el diagrama UML que muestra la estructura interna del servicio del sensor

    - ![Alt text](Diagrama_Sensor.png?raw=true "Diagrama UML Sensor")

  ## Patrones de diseno

- Estrategia: utilizamos este patrón ya que se trabaja de forma diferente (con distintas reglas) dependiendo de que ejecutamos un comando para ver cualquier parámetro que se halla establecido
o verifiquemos la existencia y caracterísitcas de un archivo.
- Fachada: debido a que dentro del cliente utilizamos una interfaz para ocultar toda esta complegidad del sensor consideramos que el metodo de fachada es otro patrón empleado.

  ## Code structure

- bin/: En este apartado instanciamos las clases necesarias y agregamos nuestras especificaciones REST.
- dms2021sensor/: Paquete principal
  - data/: Apartados de datos del programa.
    - config/: Aquí tenemos nuestra configuración del sensor.
    - db/: Base de datos del sensor (No implementada)
  - logic/: Apartado en el que encontramos la implementación de los sensores y nuestra interfaz del sensor.
  - presentation/: 
    - rest/: Este es el apartado donde se genera una respuesta al sensor en base a las solicitudes entrantes.



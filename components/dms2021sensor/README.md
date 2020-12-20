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
  
  ## Arquitectura y diseno del sensor

- Descripcion de la arquitectura y diseno del sensor
  
  - Diseno basado en el modelo-vista-controlador (MVC)
  
  - La arquitectura del servicio del sensor se divide en 3 carpetas. 
    - Una primera carpeta de datos (`data`) que no es usada debido a que creamos los sensores como instancias de objetos y obtenemos sus datos con sus propios metodos no mediante una bases de datos.
    - Una carpeta llamada `logic` que contiene la logia de negocio del sesnsor. Dentro de ella encontramos los sensores `sensor1`, `sensor2`, `sensor3`. Estos implementan algun tipo de monitorizacion del sistema. Por ahora la aplicacion solo implementa la funcionalidad del `sensor1`, que calcula la memoria RAM usuada del sistema en el momento que se instancie el objeto y podra ser actualizada. Tambien encontramos el fichero `sensorAbs` que implementa la clase abstracta de la que heredan los sensores del sistema marcando su estructura interna minima.
    - Una ultima carpeta que implementa la capa de presentacion (`presentation`). Dentro de ella encontramos la carpeta `rest` qeu contiene el archivo `sensorrest` qeu implementa el API Rest del servicio sensor. Esta implementacion permite la conexion con los demas servicios del sistema.
  
- Diagrama UML de la arquitectura del sensor
  - En la siguiente imagen podemos ver el diagrama UML que muestra la estructura interna del servicio del sensor
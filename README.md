# Kosmos-TCP-Challenge

Este proyecto está conformado por un cliente y servidor desarrollado con Python y el módulo `socket`. El cliente puede enviar mensajes al servidor, el cual convierte los mensajes que recibe del cliente a mayúscula y los envía de vuelta. El cliente puede terminar la conexión al enviar el mensaje `"DESCONEXION"`

## Requerimientos

- Python 3.x

## Ejecución

### 1. Inicia el servidor

Abre una terminal en el folder raíz del proyecto e ingresa el siguiente comando:

```sh
python server.py
```

El servidor iniciara y esperara por la conexión del cliente.

### 2. Inicia el cliente

En una **nueva ventana de terminal**, corre:

```sh
python client.py
```

El cliente se conectará al servidor y te pedirá que ingreses un mensaje.

### 3. Envía mensajes

- Teclea cualquier mensaje en la terminal del cliente para que se convierta a mayúscula.
- El servidor recibirá el mensaje y enviará la versión en mayúscula de vuelta al cliente.

### 4. Desconectar el cliente

Para desconectar al cliente, teclea:

```
DESCONEXION
```

De esta forma el cliente terminara la conexión con el servidor.

### 5. Detener el servidor

Para terminar la ejecución del servidor es muy probable que se tenga que terminar el proceso de la terminal de forma manual. Debido a las restricciones de tiempo de la prueba no se implementó una manera simple de cerrar el servidor, pero esto se puede lograr utilizando la librería de `threading` que ofrece Python.

## Pruebas Manuales (Ejemplo)

**Cliente:**

```sh
What message do you want converted to uppercase?
hola
HOLA
What message do you want converted to uppercase?
DESCONEXION
Disconnecting from server
```

**Servidor:**

```sh
Waiting to connect with a client
Connected to client in port 54032
Received message "hola" from client in port 54032
Received message "DESCONEXION" from client in port 54032
Client disconnected from server
Waiting to connect with a client
```

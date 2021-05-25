===================
 API de anime hole 
===================

OBTENER FRASES DE PERSONAJES (GET)
-----------------------------------
.. http:get:: /api/quotes

**Ejemplo de petición**

.. sourcecode:: http
    GET /api/quotes HTTP/1.1

**Ejemplo de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "quote": "Those who underestimate their enemies will not last long in this world.",
        "character": "Horobi"
    }

.. sourcecode:: http

    HTTP/1.1 502 BAD GATEWAY
    Content-Type: application/json

    {
        "code": "problem_during_petition",
        "detailed": "problema durante petición",
        "data": "404 - NOT FOUND"
    }

:status 200: Frase obtenida exitosamente
:status 502: Error durante petición a API de terceros

OBTENER IMAGENES DE WAIFUS (GET)
-----------------------------------
.. http:get:: /api/waifus

**Ejemplo de petición**

.. sourcecode:: http
    GET /api/quotes HTTP/1.1

**Ejemplo de respuesta**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: image/png

.. sourcecode:: http

    HTTP/1.1 502 BAD GATEWAY
    Content-Type: application/json

    {
        "code": "problem_during_petition",
        "detailed": "problema durante petición",
        "data": "404 - NOT FOUND"
    }

:status 200: Imagen obtenida exitosamente
:status 502: Error durante petición a API de terceros
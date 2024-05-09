# Proyecto: Manejo del CRUD

## Contexto
Una empresa dedicada al arriendo de inmuebles requiere de su ayuda para crear un sitio
web donde usuarios puedan revisar inmuebles disponibles para el arriendo, separado por
comuna y región. El sitio web poseerá dos tipos de usuarios: arrendatarios y arrendadores.
Los distintos usuarios deberán poder realizar distintas operaciones dentro del sitio que
serán detalladas a continuación.

## Hitos de desarrollo
<details>
<summary>Hito 1</summary>
Requerimiento 1: Ambiente de desarrollo

![Ambiente de desarrollo](https://raw.githubusercontent.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/main/screenshots_hitos/hito1/1%20ambiente%20desarrollo.png)

Requerimiento 2a: Representación del modelo relacional de datos

![Modelo de datos](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/2a%20modelo%20datos.png)

Rquerimiento 2b: Conexión a BDD

![Conexion a BDD](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/2b%20conexion%20bdd.png)

Requerimiento 2c: Definición y manejo de llaves primarias en columnas foráneas

![Claves Foráneas](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/2c%20FK.png)

Requerimiento 3a: Crear un objeto con el modelo

![Crear objeto](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/3a%20Crear%20objeto.png)

Requerimiento 3b: Enlistar desde modelo de datos

![Enlistar registros](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/3b%20enlistar%20registros.png)

Requerimiento 3c: Actualizar un registro en el modelo de datos

![Actualizar registro](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/3c%20actualizar%20registro.png)

Requerimiento 3d: Borrar un registro del modelo de datos

![Borrar registro](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito1/3d%20borrar%20registro.png)

</details>

<details>
<summary>Hito 2</summary>

Requerimiento 1a: Loaddata Regiones y Comunas

![loaddata regiones y comunas](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito2/1a%20loaddata%20regiones%20y%20comunas.png)

Requerimiento 1b: Loaddata Tipos de inmuebles

No aplica, tipo_inmueble es un choices en vez de una tabla.

Requerimiento 1c: Loaddata Usuarios e Inmuebles

![loaddata usuarios e inmuebles](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito2/1c%20loaddata%20usuarios%20e%20inmuebles.png)

Requerimiento 2: Consultar con SQL inmuebles por comunas

![Listado de inmuebles por comuna con SQL](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito2/2%20listado%20inmuebles%20comuna%20con%20SQL.png)

[Documento de salida](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/hito2_req2_inmuebles_comuna.txt)

Requerimiento 3: Consultar con SQL inmuebles por Región

![Listado de inmuebles por región con SQL](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/raw/main/screenshots_hitos/hito2/3%20listado%20inmuebles%20region%20SQL.png)

[Documento de salida](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/hito2_req3_inmuebles_region.txt)

</details>

<details>
<summary>Hito 3</summary>

Requerimiento 1.1: Generar una vista de login de usuario
Se usa funcionalidad de django para el login, solo se modifica apariencia de formulario

![Vista Login](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/1.1%20Generar%20una%20vista%20de%20login%20de%20usuarios.png)

Requerimiento 1.2: Generar una vista de registro
Se crea view y template registro_usuario que recibe formulario personalizado

![Vista Registro](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/1.2%20Generar%20una%20vista%20de%20registro.png)

Requerimiento 1.3: Realizar redireccionamiento de urls

![URLs](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/1.3%20Realizar%20redireccionamiento%20de%20urls.png)

Requerimiento 1.4: Desplegar los datos de usuario
En página principal se le da la bienvenida al usuario logueado mediante su nombre

![Bienvenida](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/1.4%20Desplegar%20los%20datos%20del%20usuario%20-%20Bienvenida.png)

Se crea template Mi Perfil para mostrar los datos del usuario

![Mi perfil](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/1.4%20Desplegar%20los%20datos%20del%20usuario%20-%20Mi%20perfil.png)

Rquerimiento 2: Agregar a la página personal de un Arrendatario y Arrendador la posibilidad de modificar sus datos personales.

</details>

## Características Base del Sitio Web

Sitio web desarrollado con Django 4.2, Bootstrap 5.0.2 y PosgreSQL 15

## Problemas o Dificultades al Desarrollar el Sitio Web


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

En template Mi Perfil se añade un link al formulario de modificación de datos de contacto.
En el formulario de edición, no se permite modificar RUT, nombre de usuario ni contraseña.

![Editar perfil](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito3/2%20Editar%20perfil.png)

</details>

<details>
<summary>Hito 4</summary>

Requerimiento 1: Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.

![Agregar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/1%20P%C3%A1gina%20Agregar%20nuevos%20inmuebles.png)

Requerimiento 1.a: Generar las rutas para la vista para agregar nuevas viviendas.

![Ruta Agregar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/1.a%20Generar%20las%20rutas%20para%20la%20vista%20para%20agregar%20nuevas%20viviendas.png)

Requerimiento 1.b: Generar el objeto de formulario.
Se crea un formulario personalizado para el ingreso de datos y actualización de inmueble.

![Formulario Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/1.b%20Generar%20el%20objeto%20de%20formulario.png)

Requerimiento 1.c: Agregar la función para guardar el objeto.
Se crea una view que recibe el formulario y lo guarda en la base de datos.

![View Agregar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/1.c%20Agregar%20la%20funci%C3%B3n%20para%20guardar%20el%20objeto.png)

Requerimiento 2: Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble existente.

![Editar/Borrar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/2%20P%C3%A1ginas%20Editar%20Borrar%20un%20inmueble.png)

Requerimiento 2.a: Generar las rutas para la vista para actualizar las viviendas por usuario.

![Ruta Editar/Borrar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/2.a%20Generar%20las%20rutas%20para%20la%20vista%20para%20actualizar%20las%20viviendas%20por%20usuario.png)

Requerimiento 2.b: Generar el objeto de formulario en base a él modelo definido.
Se utiliza el mismo formulario del requerimiento 1.b

Requerimiento 2.c: Agregar la función para actualizar el objeto.
Se crean una views que reciben el formulario y lo actualiza o elimina en la base de datos. 
El formulario lleva la instancia del inmueble que se desea editar/borrar para identificarlo.

![View Editar inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/2.c%20Agregar%20la%20funci%C3%B3n%20para%20actualizar%20el%20objeto.png)

Requerimiento 3: Crear una página web básica donde los arrendatarios puedan ver la oferta disponible.

![Oferta Inmuebles Disponibles](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/3%20p%C3%A1gina%20web%20b%C3%A1sica%20donde%20los%20arrendatarios%20puedan%20ver%20la%20oferta%20disponible.png)

Requerimiento 3.a: Generar las rutas para ver las viviendas.

![Ruta Lista Inmuebles (index)](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/3.a%20Generar%20las%20rutas%20para%20ver%20las%20viviendas.png)

Requerimiento 3.b: Crear la vista y el controlador que le permitan enlistar las viviendas.
Se crea una view que busca los inmuebles disponibles y lo muestra en la página principal.
Esta se puede filtrar por región y/o comuna.

![Lista Inmuebles](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/3.b%20Crear%20la%20vista%20y%20el%20controlador%20que%20le%20permitan%20enlistar%20las%20viviendas.png)


</details>

## Características Base del Sitio Web

Sitio web desarrollado con Django 4.2, PosgreSQL 15 y Bootstrap 5.0.2. 

<details>
<summary>Index: Página principal que muestra la lista de inmuebles disponibles para arriendo. Permite filtrar por REgión y/o comuna.</summary>
También se puede acceder desde la opción Inmuebles disponibles. No requiere login.

![Index](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Index.png)

</details>

<details>
<summary>Login: Permite el ingreso a usuarios registrados, funcionalidad disponible mediante menú desplegable "Ingresar".</summary>
En caso de no tener cuenta permite acceder al registro mediante un link.
El cierre de sesión está disponible mediante menú desplegable "Bienvenido". Al cerrar la sesión se redirige al Index. 

![Login](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Login.png)

</details>

<details>
<summary>Registrate: Permite el registro de nuevos usuarios, pueden escoger entre tipo Arrendador o Arrendatario</summary>

![Registrate](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Registro.png)

</details>

<details>
<summary>Mi Perfil: Muestra los datos del usuario logueado y da acceso a la modificación de estos mediante un link.</summary>

![Mi perfil](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Mi%20perfil.png)

</details>

<details>
<summary>Editar Perfil: Permite a los uauarios registrados modificar nombre, apellido y sus datos de contacto</summary>

![Editar perfil](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Editar%20perfil.png)

</details>

<details>
<summary>Dashboard Arrendador: Permite que el usuario identificado como arrendador vea un listado de sus inmuebles, sin importar el estado de disponibilidad y que pueda administrar las solicitudes de arriendo recibidas.</summary>

![Dashboard Arrendador](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Dashboard%20Arrendador.png)

</details>

<details>
<summary>Dashboard Arrendatario: Permite que el usuario identificado como arrendatario vea un listado de sus solicitudes.</summary>
Permite cancelar las solicitudes con estado Pendiente.

![Dashboard Arrendatario](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Dashboard%20Arrendatario.png)

</details>

<details>
<summary>Ingresar Inmueble: Formulario para registro de nuevos inmuebles. Se requiere login como arrendador.</summary>

![Ingresar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Ingresar%20inmueble.png)

</details>

<details>
<summary>Detalle Inmueble: Muestra los datos completos del inmueble.</summary>
Para Arendatarios da acceso al ingreso de Solicitudes de arriendo para ese inmueble.

![Detalle inmueble - Arrendatario](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Detalle%20Inmueble%20-%20Arrendatario.png)

Para Arendador da acceso a Editar y Eliminar el Inmueble. Pide confirmación antes de derivar a las páginas correspondientes.

![Detalle inmueble - Arrendador](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Detalle%20Inmueble%20-%20Arrendador.png)

</details>

<details>

<summary>Ingresar solicitud de arriendo: Se accede desde detalle de inmueble y permite ingresar una solicitud para esa publicación en especifico</summary>
Sólo permite enviar un mensaje personalizado al Arrendador, los demás datos no son modificables.

![Ingresar solicitud de arriendo](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Ingresar%20solicitud%20de%20arriendo.png)

![Ingreso solicitud exitoso](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Ingresar%20solicitud%20de%20arriendo%20-%20Success.png)

</details>

<details>
<summary>Editar Inmueble: Permite a los arrendadores modificar los datos de sus inmuebles.</summary>
Al finalizar la modificación redirecciona a Mi Perfil.

![Editar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Editar%20inmueble.png)

</details>

<details>
<summary>Eliminar Inmueble: Permite eliminar el inmueble desde el que se accedió. Es una reconfirmación de eliminación.</summary>
Luego de eliminar redirecciona al Index.

![Eliminar Inmueble](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Eliminar%20inmueble.png)

</details>

<details>

<summary>Solicitudes: Es visible para los usuarios Arrendador y muestra un listado completo de solicitudes recibidas.</summary>
No permite administración de éstas.

![Solicitudes](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito5/Solicitudes.png)

</details>

## Problemas o Dificultades al Desarrollar el Sitio Web

<details><summary>Conseguir que el modelo de Usuario herede correctamente de la clase AbstractUser para no repetir campos y poder crear el usuario correctamente.</summary>
La creación del usuario se solucionó con un formulario y administración de usuarios personalizados, pero formulario de edición quedó con mensaje que indica que no se puede manipular la contraseña.

![Modulo administración](https://github.com/LauDuhalde/PORTAL-INMOBILIARIO-V2/blob/main/Hitos/hito5/CustomUserAdmin.png)

![Formulario CustomUserCreationForm](https://github.com/LauDuhalde/PORTAL-INMOBILIARIO-V2/blob/main/Hitos/hito5/CustomUserCreationForm.png)

![Detalle Contraseña](https://github.com/LauDuhalde/PORTAL-INMOBILIARIO-V2/blob/main/Hitos/hito5/Editar%20perfil%20v2-%20detalle%20contrase%C3%B1a.png)

</details>


<details>
<summary>Realizar el filtrado de los inmuebles por región y comuna, ya que quería que se actualizara la lista de comunas al momento de seleccionar la región.</summary>
Se soluciona utilizando AJAX.

![Función JS/AJAX](https://github.com/LauDuhalde/PROYECTO-PORTAL-INMOBILIARIO/blob/main/screenshots_hitos/hito4/Funcion%20filtrar%20comuna.png)

</details>


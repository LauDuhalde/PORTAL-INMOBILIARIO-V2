  // Función para cargar las comunas correspondientes a la región seleccionada
  function cargarComunas() {
    var region_id = document.getElementById('region').value;
    var comunas_select = document.getElementById('comuna');

    // Limpiar las opciones existentes
    comunas_select.innerHTML = '';

    // Si no se ha seleccionado ninguna región, salir de la función
    if (!region_id) {
      comunas_select.innerHTML = '<option value="">Todas las comunas</option>';
      return;
    }

    // Realizar una petición AJAX para obtener las comunas de la región seleccionada
    fetch('/obtener_comunas/?region_id=' + region_id)
      .then(response => response.json())
      .then(data => {
         //Permite que el filtro comunas tenga la opción "Todas las comunas" al seleccionar una región
          var optionAll = document.createElement('option');
          optionAll.value = '';
          optionAll.textContent = 'Todas las comunas';
          comunas_select.appendChild(optionAll);

        // Agregar las comunas obtenidas como opciones al campo de selección
        data.forEach(comuna => {
          var option = document.createElement('option');
          option.value = comuna.id;
          option.textContent = comuna.nombre;
          comunas_select.appendChild(option);
        });
      });
  }

  // Agregar un event listener para el cambio en el campo de selección de regiones
  document.getElementById('region').addEventListener('change', cargarComunas);

  // Llamar a la función cargarComunas al cargar la página para actualizar las comunas inicialmente
  cargarComunas();

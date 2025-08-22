const ctx = document.getElementById('lineChart');
const ctx1 = document.getElementById('lineChart1');
const ctx2 = document.getElementById('lineChart2');
const ctx3 = document.getElementById('lineChart3');

var options = {
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        color: "rgba(204, 204, 204,0.1)"
      }
    },
    x: {
      title: {
        display: true,
        text: 'Eje X (Tiempo)',
        color: 'white',
        font: {
          size: 14,
          weight: 'bold'
        },
        
      },
      display: false,
      ticks: {
          display: false // Oculta los labels (etiquetas) del eje X
      },
    }
  }
};

var data = {
  labels: [], // Inicia vacío
  datasets: [{
    label: 'Aceleración eje X',
    data: [],
    borderColor: 'rgba(255,99,132,1)',
    borderWidth: 1,
    fill: false,
    tension: 0,
    pointRadius: 0
  }]
};
var data1 = {
  labels: [], // Inicia vacío
  datasets: [{
    label: 'Aceleración eje X',
    data: [],
    borderColor: 'rgba(255,99,132,1)',
    borderWidth: 1,
    fill: false,
    tension: 0,
    pointRadius: 0
  }]
};
var data2 = {
  labels: [], // Inicia vacío
  datasets: [{
    label: 'Aceleración eje X',
    data: [],
    borderColor: 'rgba(255,99,132,1)',
    borderWidth: 1,
    fill: false,
    tension: 0,
    pointRadius: 0
  }]
};
var data3 = {
  labels: [], // Inicia vacío
  datasets: [{
    label: 'Aceleración eje X',
    data: [],
    borderColor: 'rgba(255,99,132,1)',
    borderWidth: 1,
    fill: false,
    tension: 0,
    pointRadius: 0
  }]
};

const grafico = new Chart(ctx, {
  type: 'line',
  data: data,
  //options: options
});

const grafico1 = new Chart(ctx1, {
  type: 'line',
  data: data1,
  //options: options
});

const grafico2 = new Chart(ctx2, {
  type: 'line',
  data: data2,
  //options: options
});

const grafico3 = new Chart(ctx3, {
  type: 'line',
  data: data3,
  options: options
});

let tiempo = 0;
function actualizarDato() {
  
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');
  const valor = document.getElementById("customRange1").value;
  //console.log(valor);
  
   
  $.ajax({
      url: "/dato/",
      type: "POST",
      data: JSON.stringify({ valor: valor }),
      contentType: "application/json",
      headers: { "X-CSRFToken": csrftoken },
      dataType: "json", 
      success: function(response) {
          console.log("Respuesta del servidor:", response);
          
          const json = JSON.parse(response.respuesta_arduino);

          //actualizar graficas
          console.log(json.distancia_ejex);
          agregarDato(grafico, tiempo, json.distancia_ejex);
          agregarDato(grafico1, tiempo, json.aceleracion_ejex);
          agregarDato(grafico2, tiempo, json.aceleracion_ejey);
          agregarDato(grafico3, tiempo, json.aceleracion_ejez);

          tiempo ++;
          
          
          //console.log(json);
          $("#numero_eje_x").text(json.distancia_ejex);
          
          $("#numero_eje_x").text(json.distancia_ejex);
          $("#aceleracion_eje_x").text(json.aceleracion_ejex);
          $("#aceleracion_eje_y").text(json.aceleracion_ejey);
          $("#aceleracion_eje_z").text(json.aceleracion_ejez);
      }
  });


}




let intervalo = null;

function miFuncion() {
    console.log("Ejecutando función...");
    // Aquí va tu lógica
    //actualizarDato()
}

document.getElementById("iniciar").addEventListener("click", function() {
    if (!intervalo) { // Evita múltiples intervalos
        intervalo = setInterval(actualizarDato, 95); // Se ejecuta cada 1 segundo
        console.log("Bucle iniciado");
    }
});

document.getElementById("detener").addEventListener("click", function() {
    if (intervalo) {
        clearInterval(intervalo);
        intervalo = null;
        console.log("Bucle detenido");
    }
});
/*

// Función para agregar un nuevo dato
function agregarDato(nuevaEtiqueta, nuevoValor) {
  grafico3.data.labels.push(nuevaEtiqueta);
  grafico3.data.datasets[0].data.push(nuevoValor);
  grafico3.update();
}*/


// Máximo de puntos visibles (10 segundos)
const maxPuntos = 40;

// Función para agregar un nuevo dato con efecto deslizante
function agregarDato(grafico_x,nuevaEtiqueta, nuevoValor) {
  grafico_x.data.labels.push(nuevaEtiqueta);
  grafico_x.data.datasets[0].data.push(nuevoValor);

  // Si excede el máximo de puntos, elimina el primero
  if (grafico_x.data.labels.length > maxPuntos) {
    grafico_x.data.labels.shift(); // Quita la primera etiqueta
    grafico_x.data.datasets[0].data.shift(); // Quita el primer dato
  }

  grafico_x.update();
}

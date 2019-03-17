jQuery.ajaxSetup({async:false});
var contador = 1;
var selector;
var titulos_tablas = [{"title": "Empleado", "targets": 0}, {"title": "Plaza", "targets": 1}, {"title": "Salario", "targets": 2}, {"title": "Institucion", "targets": 3}, {"title": "Tipo de contrato", "targets": 4}, {"title": "Ultima actualizacion", "targets": 5}];
		// Define a plugin to provide data labels
		Chart.plugins.register({
			afterDatasetsDraw: function(chart) {
				var ctx = chart.ctx;

				chart.data.datasets.forEach(function(dataset, i) {
					var meta = chart.getDatasetMeta(i);
					if (!meta.hidden) {
						meta.data.forEach(function(element, index) {
							// Draw the text in black, with the specified font
							ctx.fillStyle = 'rgb(0, 0, 0)';

							var fontSize = 12;
							var fontStyle = 'bold';
							var fontFamily = 'Helvetica Neue';
							ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);

							// Just naively convert to string for now
							//console.log(dataset.data[index].r);
							var dataString = dataset.data[index].ins;

							// Make sure alignment settings are correct
							ctx.textAlign = 'right';
							ctx.textBaseline = 'middle';

							var padding = 5;
							var position = element.tooltipPosition();
							ctx.fillText(dataString, position.x +50, position.y - (fontSize / 2) + 10);
						});
					}
				});
			}
		});

var ctx = document.getElementById("bubble");
var myChart = new Chart(ctx, {
    type: 'bubble',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: 'Empleados: ',
            data: [{x:5,y:5,r:0,ins:"",ar:"",empleados:""}, {x:14,y:12,r:40,ins:"Asamblea Legislativa",ar:"001",empleados:"2,278"}, {x:16,y:14,r:25,ins:"IAIP",ar:"002",empleados:"48"},{x:25,y:20,r:0,ins:"",ar:"",empleados:""}],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
		onClick : prueba,
		maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:false,
					display: false
                },
				gridLines:{color: "rgba(0, 0, 0, 0)"}
            }],
			xAxes:[{
				ticks: {
                    beginAtZero:false,
					display: false
                },
				gridLines:{color: "rgba(0, 0, 0, 0)"}
			}]
        },
		legend: {
			display: false
		},
		tooltips:{
			callbacks:{
				label: function(tooltipItem, data) {
                    var label = data.datasets[tooltipItem.datasetIndex].label || '';

                    label += data.datasets[0].data[tooltipItem.index].empleados;
                    return label;
                }
			}
		}
    },
	axes:{
		display: false
	}
});

function prueba(e,array){
	if (array[0]){
		//console.log(array[0]._index);
		//console.log(array[0]["_chart"]["data"]["datasets"][0]["data"]);
		Papa.parse("./data/"+array[0]._index+".csv", {
			download: true,
			complete: function(results) {
				crearTabla(results);
				contador += 1;
			}
		});		
	}
	
	
}

/*function crearTabla(datos){
	$('#tabla-datos').empty();	
	$.each(datos,function(indice,lista){
		$.each(lista,function(numero,valores){
			$('#tabla-datos').append("<tr>");
			$.each(valores,function(otroindice,resultado){
				$('#tabla-datos').append("<td>"+resultado+"</td>");
			});
			$('#tabla-datos').append("</tr>");
			
		});
	});
	$('#tabla').DataTable();
}*/


function crearTabla(datos){
	if (contador > 1){
		 $('#tabla').dataTable().fnClearTable();
		selector.rows.add(datos.data).draw();
		return;
	}
	selector = $('#tabla').DataTable( {
            data: datos.data,
            responsive: true,
            "columnDefs": titulos_tablas,
            //"columns": columnas[ano],

            language: {
                search: "Buscar:",
                lengthMenu: "Mostrar _MENU_ elementos",
                info: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_",
                paginate: {
                    first:      "Primero",
                    previous:   "Previo",
                    next:       "Siguiente",
                    last:       "Último"
                },
            }
        } );
}
		// Define a plugin to provide data labels
		Chart.plugins.register({
			afterDatasetsDraw: function(chart) {
				var ctx = chart.ctx;

				chart.data.datasets.forEach(function(dataset, i) {
					var meta = chart.getDatasetMeta(i);
					if (!meta.hidden) {
						meta.data.forEach(function(element, index) {
							// Draw the text in black, with the specified font
							ctx.fillStyle = 'rgb(255, 255, 255)';

							var fontSize = 15;
							var fontStyle = 'normal';
							var fontFamily = 'Helvetica Neue';
							ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);

							// Just naively convert to string for now
							console.log(Objects.keys(dataset.data[index]));
							var dataString = dataset.data[index].r.toString();

							// Make sure alignment settings are correct
							ctx.textAlign = 'right';
							ctx.textBaseline = 'middle';

							var padding = 5;
							var position = element.tooltipPosition();
							ctx.fillText(dataString, position.x , position.y - (fontSize / 2) + 10);
						});
					}
				});
			}
		});

//Crea las graficas cuando es llamada
function crearGrafica(objeto_grafica,conjunto_datos){
        console.log(conjunto_datos["labels"],conjunto_datos["data"]);
        new Chart(objeto_grafica, {
        type: 'horizontalBar',
        data: {
            labels: conjunto_datos["labels"],
            datasets: [{
                label: 'Votos',
                data: conjunto_datos["data"],
                backgroundColor: conjunto_datos["colores"],
                borderColor: conjunto_datos["colores"],
                borderWidth: 1
            }]
        },
        options: {
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero:true,
                        callback: function(value, index, values) {
                                if(parseInt(value) >= 1000){
                                   return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                                } else {
                                   return value;
                                }
                           }
                    }
                }]
            },

            tooltips: {
                callbacks: {
                    label: function(tooltipItem, data) {
						//var multistringText = [tooltipItem.yLabel];
						var publicar = [];
                        var value = data.datasets[0].data[tooltipItem.index];
                        if(parseInt(value) >= 1000){
                                   publicar.push(value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")+"%");
								   publicar.push('Votos: '+ conjunto_datos["votos"][tooltipItem.index].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
                                } else {
                                   publicar.push(value+"%");
								   publicar.push('Votos: '+ conjunto_datos["votos"][tooltipItem.index].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","));
                                }
								
						return publicar;
                    }
              }
            },
            title: {
                display: true,
				fontSize: 14,
                text: 'Última actualización - 11:55 a.m. - Actas procesadas: 99.94%'
            },
            legend: {
                display: false
            }
        }
    });
}

var primer_grafica = {
    "1994":{"nombreg":"elec_1994-g1","labels":["ARENA/COALICIÓN", "FMLN","GANA", "VAMOS"],"colores":['rgba(0, 90, 171, 1)','rgba(224, 4, 11, 1)','rgba(99, 190, 227, 1)','rgba(28, 93, 167, 1)'],"data":[31.8, 14.4, 53.0, 0.8],"votos":[831726, 377404, 1388009, 20423]},

};


$.each(primer_grafica,function(ano,contenedor){
    

    
    crearGrafica(document.getElementById(contenedor["nombreg"]).getContext('2d'),contenedor);
});


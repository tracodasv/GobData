jQuery.ajaxSetup({async:false});
var contador = 1;
var selector;
var titulos_tablas = [{"title": "Empleado", "targets": 0}, {"title": "Plaza", "targets": 1}, {"title": "Salario", "targets": 2}, {"title": "Institucion", "targets": 3}, {"title": "Tipo de contrato", "targets": 4}, {"title": "Ultima actualizacion", "targets": 5}];


var ctx = document.getElementById("gm-1").getContext('2d');
var ctx2 = document.getElementById("gm-2").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["2015", "2016", "2017", "2018"],
        datasets: [{
            label: 'Deuda: ',
            data: [10,11,18,11,10],
			fill:false,
            backgroundColor: [
                'rgb(24, 55, 99,0.9)',
                'rgb(24, 55, 99,0.9)',
                'rgb(24, 55, 99,0.9)',
                'rgb(24, 55, 99,0.9)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
			backgroundColor:[
			'rgb(0, 171, 110)',
			'rgb(0, 171, 110)',
			'rgb(0, 171, 110)',
			'rgb(0, 171, 110)',
			],
            borderWidth: 0
        }]
    },
    options: {
		maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:false,
					display: true
                },
				gridLines:{color: "rgba(0, 171, 110, 0)"}
            }],
			xAxes:[{
				ticks: {
                    beginAtZero:false,
					display: true
                },
				gridLines:{color: "rgba(0, 0, 0, 0)"}
			}]
        },
		legend: {
			display: false
		},
    },
	axes:{
		display: false
	}
});


var myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: ["2015", "2016", "2017", "2018"],
        datasets: [{
            label: 'Deuda: ',
            data: [16,17,11,14,9],
			fill:false,
            backgroundColor: [
                'rgb(24, 55, 99,0.9)',
                'rgba(24, 55, 99,0.9)',
                'rgba(24, 55, 99,0.9)',
                'rgba(24, 55, 99,0.9)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderWidth: 1
        }]
    },
    options: {
		maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:false,
					display: true
                },
				gridLines:{color: "rgba(0, 0, 0, 0)"}
            }],
			xAxes:[{
				ticks: {
                    beginAtZero:false,
					display: true
                },
				gridLines:{color: "rgba(0, 0, 0, 0)"}
			}]
        },
		legend: {
			display: false
		},

    },
	axes:{
		display: false
	}
});



const MAPWIDTH = document.getElementById('mapa').offsetWidth;
const MAPHEIGHT = document.getElementById('mapa').offsetHeight;

var genderIneq = d3.csv('https://raw.githubusercontent.com/danipequelangos/Programming/master/Proyecto%20Desi/DesigualdadGenero.csv');
var mapData = d3.json('https://raw.githubusercontent.com/danipequelangos/Programming/master/Proyecto%20Desi/custom.geo.json');

var svg = d3.select("#mapa")
			.append("svg")
    		.attr("width",MAPWIDTH)
    		.attr("height",MAPHEIGHT);

Promise.all([genderIneq, mapData]).then(function(data){

	var genderIneq = data[0];
	var mapData = data[1];

	//Valor inicial de las variables de representacion
	var gen = "M.";
	var varRep = "GII";

	var path = d3.geoPath(d3.geoMercator().translate([MAPWIDTH/2, MAPHEIGHT*0.6]).scale(150));


	var color = changeData(gen, varRep, genderIneq, mapData);
	
	var map = svg
    	.append("g")
    	.call(d3.zoom().scaleExtent([1,8]).on("zoom", function () {
       map.attr("transform", d3.event.transform)
    }));

    map.attr("width",MAPWIDTH)
    	.attr("height",MAPHEIGHT);
    	

	map.selectAll("path")
		.data(mapData.features)
		.enter()
		.append("path")
		.attr("d", path)
		.style("fill", changeColor)
		.on("mouseover", mouseover)
		.on("mouseout", mouseout);

	svg.append("text")
		.attr("x", MAPWIDTH/2)
		.attr("y", 20)
		.attr("text-anchor","middle")
		.style("fill","black")
		.style("font-family","Garamond")
		.style("font-weight","bold")
		.style("font-size","25px")
		.text("Desigualdad de Genero por País");


	d3.select("#selecVar")
		.on("change", function(){
			varRep = d3.select("#selecVar").property("value");
			color = changeData(gen, varRep, genderIneq, mapData);
			d3.selectAll("path")
        		.style("fill", changeColor);
		});

	d3.select("#selecGen")
		.on("change", function(){
			gen = d3.select("#selecGen").property("value");
			color = changeData(gen, varRep, genderIneq, mapData);
			d3.selectAll("path")
        		.style("fill", changeColor);
		});

	function changeColor(d){
		var value = d.properties.value;
		if (value >= 0) {
			//If value exists...
			return color(value);
		} else {
			//If value is undefined...
			return "#bbb";
		}
	}

	function mouseover(features){
		var pais = features.properties.name_long;
		//Si el valor no esta definido lo llamamos NaN
		if(features.properties.value == undefined){
			var valor = "NaN";
		}else if(features.properties.value % 1 != 0){ 
			//Si es un decimal recortamos el valor para que sea mas legible
			var valor = (features.properties.value).toFixed(6);
		}else{
			var valor = features.properties.value;
		}
		var infoBox = d3.select("body")
						.append("div")
						.attr("class", "infoBox")
						.attr("id", "infoBox")
						.style("opacity", 1)
				
		infoBox.html("<b>Pais</b>: " + pais + "<br><b>Valor de " + varRep + "</b>: " + valor)
			.style("left", d3.event.pageX + "px")
			.style("top", d3.event.pageY + "px");
	}

	function mouseout(features){
		d3.select("#infoBox").remove();
	}

});

function changeData(gen, varRep, genderIneq, mapData){
	var low = "purple"; var high = "#E5CCFF";
	var min = 999; var max = 0;
	//Elijo los colores segun la variable y el genero elegidos 
	switch(varRep){
		case "GII": break;
		case "Mort.Maternal": low = "#FFC0C0"; high = "red"; break;
		case "Nac.Adolescentes": low = "#FFC0C0"; high = "red"; break;
		case "AsientosParlamento": 
			if(gen=="M."){
				low = "#FFC4EA"; high = "#FF00A2";
			}else{
				low = "#B5CBFF"; high = "#004DFF";
			}
			break;
		case "Educacion": varRep = String(gen).concat(String(varRep));
			if(gen=="M."){
				low = "#FFC4EA"; high = "#FF00A2";
			}else{
				low = "#B5CBFF"; high = "#004DFF";
			}
			break;
		case "Pob.Activa": varRep = String(gen).concat(String(varRep));
			if(gen=="M."){
				low = "#FFC4EA"; high = "#FF00A2";
			}else{
				low = "#B5CBFF"; high = "#004DFF";
			}
			break;
	}
	//Eliminamos los datos anteriores que pudiese haber
	for (var i = 0; i < mapData.features.length; i++){
		mapData.features[i].properties.value = undefined;
	}
	//Concatenamos los datos al mapData
	for (var i = 0; i < genderIneq.length; i++) {
		dataState = String(genderIneq[i].Pais);
		//Cogemos el valor varRep y lo convertimos a float
		if (varRep == "AsientosParlamento" & gen == "H."){
			var dataValue = 100 - parseFloat(genderIneq[i][varRep]);
		}else{
			var dataValue = parseFloat(genderIneq[i][varRep]);
		}
		//Buscamos valores maximos y minimos en los datos
		if(min > dataValue){
			min = dataValue;
		}
		if(max < dataValue){
			max = dataValue;
		}
		//Buscamos el estado correspondiente en el json mapData
		for (var j = 0; j < mapData.features.length; j++) {
			var mapState = String(mapData.features[j].properties.name_long);
			//Miramos si es un substring uno del otro en lugar de si son iguales
			if (dataState.includes(mapState)) {
				if(mapData.features[j].properties.value == undefined){
					mapData.features[j].properties.value = dataValue;
					break;
				}
			}
		}
	}
	var color = d3.scalePow()
                .exponent(1)
                .domain([min,max])
                .range([low,high]);
    return color;
}

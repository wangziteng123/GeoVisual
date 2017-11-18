// queue()
//     .defer(d3.json, "/mapdata")
//     .await(makeGraphs);

// function makeGraphs(error, mapjson) {

// 	// var div = document.getElementById('location-row-chart');
// 	// div.innerHTML = maprecords[1];
	
// 	var maprecords = mapjson;

// 	//create a crossfilter instance
// 	var ndx = crossfilter(maprecords);

// 	//define dimensions
// 	var materialNoDim = ndx.dimension(function(d) { return d["Material_No"]; });
// 	var plantDim = ndx.dimension(function(d) { return d["Plant"]; });
// 	var oriplantDim = ndx.dimension(function(d) { return d["OriPlant"]; });
// 	var allDim = ndx.dimension(function(d) {return d;});

// 	//Group Data
// 	var plantgroup = plant.group();
// 	var oriplantgroup = oriplant.group();
// 	var all = ndx.groupAll();

// 	//Charts
// 	// var locationChart = dc.rowChart("#location-row-chart");

//  //   locationChart
//  //    	.width(200)
// 	// 	.height(510)
//  //        .dimension(locationdDim)
//  //        .group(locationGroup)
//  //        .ordering(function(d) { return -d.value })
//  //        .colors(['#6baed6'])
//  //        .elasticX(true)
//  //        .labelOffsetY(10)
//  //        .xAxis().ticks(4);


// 	var map = L.map('map')
// 	var drawMap = function(){

// 	    map.setView([31.75, 110], 4);
// 		mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
// 		L.tileLayer(
// 			'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
// 				attribution: '&copy; ' + mapLink + ' Contributors',
// 				maxZoom: 15,
// 			}).addTo(map);

// 		//HeatMap
// 		var geoData = [];
// 		_.each(allDim.top(Infinity), function (d) {
// 			geoData.push([d["plantlatitude"], d["plantlongitude"], 1]);
// 	      });
// 		var heat = L.heatLayer(geoData,{
// 			radius: 10,
// 			blur: 20, 
// 			maxZoom: 1,
// 		}).addTo(map);

// 	};

// 	//Draw Map
// 	drawMap();

// 	// //Update the heatmap if any dc chart get filtered
// 	// dcCharts = [locationChart];

// 	// _.each(dcCharts, function (dcChart) {
// 	// 	dcChart.on("filtered", function (chart, filter) {
// 	// 		map.eachLayer(function (layer) {
// 	// 			map.removeLayer(layer)
// 	// 		}); 
// 	// 		drawMap();
// 	// 	});
// 	// });

// 	//dc.renderAll();

// };




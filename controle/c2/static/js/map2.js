  var streets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    subdomains:['mt0','mt1','mt2','mt3'],
   attribution: 'Google Streets'
  });
    
  var Satellite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    subdomains:['mt0','mt1','mt2','mt3'], attribution: 'Google Satellite'
  }); 
  
  var Topographic = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
		attribution: 'OpenStreetMap'
});
  
   // Set up initial map center and zoom level
   var map = L.map('map', {
    center: [-29.5972, -55.3611], 
    zoom: 13,  
    scrollWheelZoom: false,
    fullscreenControl: true,
			fullscreenControlOptions: { // optional
				title:"Show me the fullscreen !",
				titleCancel:"Exit fullscreen mode"
			},
    tap: false,
    layers: [streets],
  });

  
var baseLayers = {
    "Streets": streets,
    "Satellite": Satellite,
    "Topographic": Topographic,
};

var control = L.control.layers(baseLayers).addTo(map); 

  
// see more basemap options at https://leaflet-extras.github.io/leaflet-providers/preview/
  
// you can set .my-div-icon styles in CSS

//2
//icons do mapa

var blueTank = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/blue_tank.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

//1

var redTank = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/red_tank.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});
//3
var sensor = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/sensor.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});
//4
var uav = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/uav.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var blueSoldier = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/blue_soldier.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});

var redSoldier = L.icon({
  iconUrl: 'http://127.0.0.1:8000/static/img/red_soldier.png',
  shadowUrl: '',
  iconSize:     [20, 20], // size of the icon
  shadowSize:   [0, 0], // size of the shadow
  iconAnchor:   [0, 0], // point of the icon which will correspond to marker's location
  shadowAnchor: [0, 0],  // the same for the shadow
  popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
});


// função de notificações e eventos
  var infoClick = function(){
    $.notify("Alert!", {type:"warning", align:"center", verticalAlign:"top"});
  }

  // Read markers data from data.csv

  $.get('http://127.0.0.1:8000/static/img/data.csv', function(csvString) {

     // Use PapaParse to convert string to array of objects
    var data = Papa.parse(csvString, {header: true, dynamicTyping: true}).data;

    // For each row in data, create a marker and add it to the map
    // For each row, columns `Latitude`, `Longitude`, and `Title` are required
    for (var i in data) {
      var row = data[i];
         
      if (row.icon == 1){
        teste = redTank;
        infoClick();
        }
      if (row.icon == 2){
        teste = blueTank;
        }
      if (row.icon == 3){
        teste = sensor;
        }
      if (row.icon == 4){
        teste = uav;
        }
      if (row.icon == 5){
        teste = blueSoldier;
        }
      if (row.icon == 6){
        teste = redSoldier;
        }

      var marker = L.marker([row.latitude, row.longitude], { icon: teste

      }).bindPopup(row.title + '</br>' + row.latitude + '</br>' + row.longitude).addTo(map)
      
    }    
   
  }); 
  
  var c = new L.Control.Coordinates(); 
  c.addTo(map);
  
  map.on('click', function(e) {
    c.setCoordinates(e);
  });

  
 var streets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    subdomains:['mt0','mt1','mt2','mt3', 'mt4'],
   attribution: 'Google Streets'
  });
    
  var Satellite = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    subdomains:['mt0','mt1','mt2','mt3', 'mt4'], attribution: 'Google Satellite'
  }); 
  
  var Topographic = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
		attribution: 'OpenStreetMap'
});
  
   // Set up initial map center and zoom level
   var map = L.map('map', {
    center: [-29.5972, -55.3611], 
    zoom: 13, 
    measureControl:false,
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


//ferramentas de desenho
map.pm.addControls({
  position: 'topright',
  editControls: false
});
var drawnItems = new L.FeatureGroup().addTo(map);
  map.on("pm:create", function (e) {
      var type = e.shape,
          layer = e.layer;

      if (type === 'Marker') {
        layer.bindPopup('A popup!');
      }

      drawnItems.addLayer(layer);
  });


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

      // leitura dos marcadores de data.csv

  $.get('http://127.0.0.1:8000/static/img/data1.csv', function(csvString) {

     // Use PapaParse to convert string to array of objects
    var data = Papa.parse(csvString, {header: true, dynamicTyping: true}).data;

    // For each row in data, create a marker and add it to the map
    // For each row, columns `Latitude`, `Longitude`, and `Title` are required
    for (var i in data) {
      var row = data[i];
         
      if (row.icon == 1){
        teste = redTank;
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

  
// Mostra latitude e longitude com 1 click no mapa
var c = new L.Control.Coordinates(); 
c.addTo(map);

map.on('click', function(e) {
  c.setCoordinates(e);
});


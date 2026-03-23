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
  layers: [Topographic],
});

  var leafletView = new PruneClusterForLeaflet();

	//marker mais rápido
    var marker = new PruneCluster.Marker(-29.5972, -55.3511, {num: "special"});
    leafletView.RegisterMarker(marker);
    var marker1 = new PruneCluster.Marker(-29.6002, -55.4211, {num: "special"});
    leafletView.RegisterMarker(marker1);
    
       	//10 marcadores próximos
    var marke = [], size = 10;
    for (var i = 0; i < size;++i) {
        var m = new PruneCluster.Marker(-29.5992,-55.4111+i*0.006, {num: i});
        marke.push(m);
        leafletView.RegisterMarker(m);
    }
    
      	//5 marcadores próximos
    var mark = [], size = 5;
    for (var i = 0; i < size;++i) {
        var n = new PruneCluster.Marker(-29.6152,-55.4051+i*0.006, {num: i});
        mark.push(n);
        leafletView.RegisterMarker(n);
    }

    leafletView.PrepareLeafletMarker = function(marker, data) {
        var t = "Num: " + data.num;
        if (marker.getPopup()) {
            marker.setPopupContent(t);
        } else {
            marker.bindPopup(t);
        }
        console.log(data);
    };

    window.setInterval(function () {
        marker.position.lat += 0.0001;
        marker1.position.lat += 0.0001;
        for (var i = 0; i < size;++i) {
            mark[i].position.lat += 0.0001;
        }
        leafletView.ProcessView();
    }, 200);

    map.addLayer(leafletView);

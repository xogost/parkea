// Note that using Google Gears requires loading the Javascript
// at http://code.google.com/apis/gears/gears_init.js

var initialLocation;
var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var browserSupportFlag =  new Boolean();
var map = null;
var myposition_latitud = "";
var myposition_longitud = "";
var myposition_latitud_d = "";
var myposition_longitud_d = "";
var position_marker = "";

function load_map(json_markers) {
    var myOptions = {
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        streetViewControl: true
    };

    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  
    // Try W3C Geolocation (Preferred)
    if(navigator.geolocation) {
        browserSupportFlag = true;

        navigator.geolocation.getCurrentPosition(function(position) {
            initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);

            myposition_latitud = initialLocation.Ua;
            myposition_longitud = initialLocation.Va;


            var marker = new google.maps.Marker({
                position: initialLocation,
                map: map, 
                title:"Ubicación Actual!",
                //icon: '../static/img/marker.png',
                draggable: true
            });
			
            for (var i = json_markers.length - 1; i >= 0; i--) {
                eval("var marker_" + i + " = new google.maps.Marker({  position: new google.maps.LatLng(" + json_markers[i].fields.latitude + "," + json_markers[i].fields.longitud + "), map: map, title:'" + json_markers[i].fields.nombre + "', draggable: false, });");

                eval("google.maps.event.addListener(marker_" + i + ", 'click', function() { position_marker = marker_" + i +".position; Trazar(); });");
                

            };
            


            google.maps.event.addListener(marker, "dragend", function(event) {
                var point = marker.getPosition();

                alert(point);
            });

            

            map.setCenter(initialLocation);
        }, function() {
            handleNoGeolocation(browserSupportFlag);
                        
        });

    // Try Google Gears Geolocation
    } else if (google.gears) {
        browserSupportFlag = true;
        var geo = google.gears.factory.create('beta.geolocation');
                    
        geo.getCurrentPosition(function(position) {
            initialLocation = new google.maps.LatLng(position.latitude,position.longitude);
            myposition_latitud = position.latitude;
            myposition_longitud = position.longitude;
            map.setCenter(initialLocation);
        }, function() {
            handleNoGeoLocation(browserSupportFlag);
                          
            var marker = new google.maps.Marker({
                position: initialLocation,
                map: map, 
                title:"Hello World!"
            });

        });

    // Browser doesn't support Geolocation
    } else {
        browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }
  
    function handleNoGeolocation(errorFlag) {
        if (errorFlag == true) {
            alert("Geolocation service failed.");
            initialLocation = newyork;
        } else {
            alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
            initialLocation = siberia;
        }
        map.setCenter(initialLocation);

                    
    }

               
}
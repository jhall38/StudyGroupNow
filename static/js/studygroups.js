/* google map */
/* api key below */
/* AIzaSyBYxOP1Eb_CAGqLl2XrZBpADTaeV40MuBA 
var myCenter = new google.maps.LatLng(47.655078,-122.307882);

function initialize() {
	var mapProp = {
	  center:myCenter,
	  zoom:15,
	  mapTypeId:google.maps.MapTypeId.ROADMAP
	};

	var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
	var markers = [['111', 'seattle', 98103, 47.65895, -122.307636 ],['321', 'seattle', 98103, 47.656639, -122.310318]]; /* {{django list of addresses and coordinates}} 

	for(i = 0; i < markers.length; i++) {
		var coordinates = new google.maps.LatLng(markers[i][3], markers[i][4]);
		var address = markers[i][0] + ' ' + markers[i][1] + ' ' + markers[i][2];
		var marker = new google.maps.Marker({
			position: coordinates,
			map: map,
			title: address,
			icon: 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=' + i + '|FF0000|000000'
		});
	}
}

google.maps.event.addDomListener(window, 'load', initialize);
 end map */

/* search page 
toggle the search result info*/
/*$(document).ready(function(){
    $(".toggle-info").click(function(){
        $(this).children(".search-info").slideToggle();
    });
/*});*/


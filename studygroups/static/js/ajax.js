$(function(){
	$('#search_courses').click(function(){
		$.ajax({
			type: "POST",
			url: "search/",
			data: {
				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
	$('#newlocation').click(function(){
		$.ajax({
			type: "POST",
			url: "/new_location/",
			data: {
				'new_location_name' : $('#location_name').val(),
				'new_location_address' : $('#location_address').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: newLocationSuccess,
			error: newLocationFail,
			dataType: 'html'
		});
	});
	
	$.get("/load_courses/", function(data) {
		$('#classes').html(data);
	});
	$.get("/load_locations/", function(data) {
		$('#locations').html(data)
		$("#locations").val($('#selected').val());		
	});
});

function searchSuccess(data, textStatus, jqXHR){
	$('#results').html(data);

}

function newLocationSuccess(data, textStatus, jqXHR){
	$('#newlocation_div').hide();	
	$('#locations').html(data);
	$('#locations').val($('#location_name').val());
}
function newLocationFail(data, textStatus, jqXHR, thrownError){
	alert("Address is invalid or does not exist. Remember this address should not inlcude city, state, country or zip code.");
	$('#newlocation_div').show();
}

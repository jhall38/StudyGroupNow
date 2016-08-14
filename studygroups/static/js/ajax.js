$(function(){
	$('#search').keyup(function(){
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
	$.get("/load_courses/", function(data) {
		$('#classes').html(data);
	});
	$.get("/load_locations/", function(data) {
		$('#locations').html(data)
	});
});

function searchSuccess(data, textStatus, jqXHR){
	$('#search-results').html(data);

}


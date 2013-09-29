function submitAjaxQuery(event)
{
    if (event.preventDefault)
        event.preventDefault();
    else
        event.cancel = true;

	var queryForm = $('#queryForm').serialize();

    if (!queryForm) { //No query val
    	return;
    }
    
    $.ajax({
  		type: "POST",
  		url: "/getTimeline",
  		data: queryForm,
  		success: function(data) {
                    var hits = [];
                    for(var i = 0; i < data.length; i++){
                        hits[i] = data[i]["hits"];
                    }
        			$('#dynamicsparkline').sparkline(hits, {
        				type: 'line',
        				width:'80%', 
        				fillColor:'rgba(55,0,0,.05)',
        				spotRadius:'5',
        				composite: false,
        				height:'50%'});
    			}
	});
}


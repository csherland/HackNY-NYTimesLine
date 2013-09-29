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
        			var myvalues = [10,8,5,7,4,4,1];
        			$('#dynamicsparkline').sparkline(myvalues, {
        				type: 'line',
        				width:'80%', 
        				fillColor:'rgba(55,0,0,.05)',
        				height:'50%'});
    			}
	});
}


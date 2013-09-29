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
	});
}


function submitAjaxQuery(event)
{
    if (event.preventDefault)
        event.preventDefault();
    else
        event.cancel = true;

    // run ajax calling function here.
    var queryVal = $("#searchQuery").val();

    if (!queryVal) { //No query val
    	return;
    }
    
    $.ajax({
  		type: "POST",
  		url: "/getTimeline",
  		data: {query : queryVal},
	});
}


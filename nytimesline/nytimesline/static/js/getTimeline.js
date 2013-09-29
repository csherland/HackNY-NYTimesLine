function submitAjaxQuery(event)
{
    if (event.preventDefault)
        event.preventDefault();
    else
        event.cancel = true;

    // run ajax calling function here.
    $.ajax({
  		type: "POST",
  		url: "/getTimeline",
  		data: {query : event.text},
  		success: success,
	});
}


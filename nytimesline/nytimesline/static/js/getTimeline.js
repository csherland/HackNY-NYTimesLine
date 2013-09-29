function submitAjaxQuery(event)
{
    if (event.preventDefault)
        event.preventDefault();
    else
        event.cancel = true;

	alert('I worked fool');

    // run ajax calling function here.
    //$.ajax({
  	//	type: "POST",
  	//	url: url,
  	//	data: data,
  	//	success: success,
  	//	dataType: dataType
	//});
}


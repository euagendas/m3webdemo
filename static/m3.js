$(document).ready(function(){
	console.log("m3 started.");
	//var test_data={"input": {"description": "Sr Data Scientist @oiioxford & @turinginst Fellow researching multilingualism, UX,  i18n/l10n, mobilization/collective action, SNA, and visualization.", "id": "1", "img_path": "static/m3/computermacgyve.jpg", "lang": "en", "name": "Scott Hale", "screen_name": "computermacgyve"}, "output": {"gender": {"male": 0.9999, "female": 0.0001}, "age": {"<=18": 0.0082, "18-29": 0.0281, "30-39": 0.0767, ">=40": 0.887}, "org": {"non-org": 0.9979, "is-org": 0.0021}}};
	//set_data(test_data);
	//clear_data();
	$("#m3submit").click(function(){
	  var screen_name=$("#screen_name_input").val();
	  console.log("Calling m3 with " + screen_name)
	  //clear_data();
	  $.ajax({
		url: "infer/"+screen_name
	  }).done(function(data) {
		console.log(data);
		set_data(data);
	  });
	  return false;

	});

	function clear_data(){
		$("#img").attr("src","static/placeholder.png")
		$("#bio").html("");
		$("#screen_name").html("");
		$("#name").html("");
		$("#output").html("");
	}

	function set_data(data){
		$("#img").attr("src",data["input"]["img_path"])
		$("#bio").html(data["input"]["description"]);
		$("#screen_name").html(data["input"]["screen_name"]);
		$("#name").html(data["input"]["name"]);
		$("#output").html(JSON.stringify(data["output"],space=5));
	}


  });
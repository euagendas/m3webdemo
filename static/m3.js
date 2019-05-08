$(document).ready(function(){
	console.log("m3 started.");

	//https://github.com/devbridge/jQuery-Autocomplete
	$('#screen_name_input').autocomplete({
		serviceUrl: '/autocomplete/screen_name',
		preventBadQueries: false,
		noCache: true,
		dataType: 'json'
	});

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
		if ("output" in data) {
			set_data(data);
		} else {
			clear_data();
			$("#bio").html("No data for " + data["input"]["screen_name"] + ". Please check for a typo.");

		}
	  });
	  return false;

	});

	function clear_data(){
		$("#img").attr("src","static/placeholder.png")
		$("#bio").html("");
		$("#screen_name").html("");
		$("#name").html("");
		$("#output").html("");
		$('#gender-prediction').text("");
		$('#gender-plot').html("");
		$('#age-prediction').text("");
		$('#age-plot').html("");
		$('#org-prediction').text("");
		$('#org-plot').html("");
	}

	function set_data(data){
		$("#img").attr("src", data["input"]["img_path"])
		$("#bio").html(data["input"]["description"]);
		$("#screen_name").html(' (@' + data["input"]["screen_name"] +")");
		$("#name").html(data["input"]["name"]);
		$("#output").html(JSON.stringify(data["output"], null, space=5));
		//$("#input").html(JSON.stringify(data["input"], null, space=5));

		//--------------- ADDED BY GM ---------------

		const {gender, age, org} = data.output;
		const ageGroups = ['<=18','18-29','30-39','>=40'];  //ensure desired order
		const xBaseAxis = {axis: {title: '', labelFontSize: 10}, scale: {domain: [0,1]}};
		const yBaseAxis = {axis: {title: '', labelFontSize: 10.5}};
		const plotWidth = 240;

		//gender
		$('#gender-prediction').text(gender.male > gender.female ? 'Male' : 'Female');
		vegaEmbed(
			'#gender-plot',
			vz([
					{Gender: 'Female', Probability: gender.female},
					{Gender: 'Male',   Probability: gender.male}
				])
				.bar()
				.x('Probability', 'q', xBaseAxis)
				.y('Gender',      'n', yBaseAxis)
				.width(plotWidth)
				.prep(),
			{actions: false}
		);

		//age
		$('#age-prediction').text(() => {
			const ageProbs = ageGroups.map(g => age[g]);
			return ageGroups[ageProbs.indexOf(Math.max(...ageProbs))];
		});
		vegaEmbed(
			'#age-plot',
			vz(ageGroups.map(g => ({Age: g, Probability: age[g]})))
				.bar()
				.x('Probability', 'q', xBaseAxis)
				.y('Age',         'n', Object.assign({sort: ageGroups}, yBaseAxis))
				.width(plotWidth)
				.prep(),
			{actions: false}
		);

		//org
		$('#org-prediction').text(org["is-org"] > org["non-org"] ? 'Organization' : 'Non-organization');
		vegaEmbed(
			'#org-plot',
			vz([
					{Org: 'Org',     Probability: org['is-org']},
					{Org: 'Non-org', Probability: org['non-org']}
				])
				.bar()
				.x('Probability', 'q', xBaseAxis)
				.y('Org',         'n', yBaseAxis)
				.width(plotWidth)
				.prep(),
			{actions: false}
		);

	}

});

$(".converter").ready(function(){
	var con, country, value;
	$.ajax({
		url: "cgi-bin/currency_converter.py",
		type : "post",
		dataType : "json",
		success : function(response){
			for (x in response){
				$("#country").append(new Option(response[x], response[x]));
			}
		}
	});
	function connect(country, con, value){
		var data_send = {"country":country, "con":con, "value":value};
		$.ajax({
			url: "cgi-bin/currency_calculate.py",
			type : "post",
			data : data_send,
			dataType : "json",
			success : function(response) {
			(response['conversion'] == 0)?($("#other").val(response['value'])):($("#inr").val(response['value']));
			}
		});
	}
	$("#inr, #other, #country").bind({
		keyup : function(){
			con = (String(this.id) === "inr")?0:1;
			country = $("#country").find("option:selected").attr("value");
			value = $(this).val(); 
			connect(country, con, value);
		},
		change : function(){
			country = $(this).find("option:selected").attr("value");
			value = $("#other").val();
			con = 1;
			connect(country, con, value);
		}
		
	});
});
		
		
		
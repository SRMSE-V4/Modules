	//Author:Ashwin Balasubramanian
	//Vertical: V4.
	/*
	This is the javascript file for conversion of all metric vales.
	It links the metric_ui.py to metric.py.....
	*/		
			
		$(document).ready(function(){
			
			//Hiding all the other conversion ui by default.
			$('#Speed , #Time, #Mass, #DigitalStorage, #FuelConsumption, #Length').hide();
			/*To be done
			1. length
			2. volume
			3. fuel consumption*/
			$('#metric').change(function(){
			/*
				This function changes the user interface on changing the select value.
			*/
			$('.convert').hide();

			$('#'+$(this).val()).fadeIn('medium');
				version=$(this).val();
			});

			$('input').change(function(){
				/*
					This operation is done on any change on the input.
					Getting the values:
					1. value entered.
					2. The unit of the value
					3. The type of metric conversion
				*/
				var value = $(this).val();
				var unit = $(this).attr('id');
				var metric = $('select').val();
				var answer = metric_selector(metric, value, unit);
				var keys = Object.keys(answer);
				for (var i in keys){
					(isNaN(answer[keys[i]]))?(answer[keys[i]] = 0.0):($('#'+keys[i]).val(parseFloat(answer[keys[i]]).toFixed(4)));
					}
				/*This line is for debuggong purpose...
				console.log("unit:"+unit+"\nmetric:"+metric+"\nvalue:"+value);
				*/
				});
				
				//More functions.. Corresponding tot the user interface.	
			$('.more').hide();

			$('#more-button').hover(function(){
				$('.more').slideToggle("fast");
			});
		});

		//-------------------------------------------------------------------------------------
		function temperature(num, unit){
			var farenheit, celcius, kelvin;
			farenheit = celcius = kelvin = 0;
			switch(unit){
				case 'farenheit':{
					celcius = ((num-32)*(5/9));
					kelvin = (num + 459.67)*(5/9);
					farenheit = num;
				}
					break;
				case 'celcius':{
					farenheit =  (num*(9/5))+32;
					kelvin = num + 273;
					celcius = num;
				}
					break;
				case 'kelvin':
				{
					celcius = num - 273.15;
					farenheit = (num - (9/5))-459.67;
					kelvin = num;
				}
					break;
			}
			return {"farenheit":farenheit,"celcius": celcius,"kelvin": kelvin};
		}
		function speed(num, unit){
			var mph, kmph, fs, knot, ms;
			kmph = fs = knot = ms =0.0;
			switch(unit){
				case 'mph':{
					kmph = num * 1.609344;
					fs = num * 1.46667;
					knot = num * 0.868976;
					ms = num * 0.44704;
					mph = num;
				}
				break;
				case 'kmph':{
					mph = num * 0.621371;
					fs = num * 0.911344;
					ms = num * 0.277778;
					knot = num * 0.539957;
					kmph = num;
				}
				break;
				case 'fs':{
					mph  = num * 0.681818;
					ms = num * 0.3048;
					kmph = num * 1.09728;
					knot = num * 0.592484;
					fs = num;
				}
				break;
				case 'knot':{
					mph = num * 1.15078;
					fs = num * 1.68781;
					ms = num * 0.514444;
					kmph = num * 1.852;
					knot = num; 
				}
				break;
				case 'ms':{
					mph = num * 2.23694;
					fs = num * 1.46667;
					kmph = num * 3.6;
					knot = num * 1.94384;
					ms = num;
				}
				break;
				default:
					break;
			}
			return {"mph" : mph, "kmph": kmph, "fs": fs, "knot": knot, "ms":ms};
		}
		function mass(num, unit){
			var metric_ton, kilogram, gram, milligram, pound, ounce;
			metric_ton= kilogram= gram= milligram= pound= ounce= 0;
			switch(unit){
				case 'metric_ton':{
					metric_ton =num ;
					kilogram = num * 1000;
					gram = num * 1000000;
					milligram = num * 1000000000;
					pound = num * 2204.62;
					ounce = num * 35274;
				}
				break;
				case 'kilogram':{
					metric_ton = num * 0.001;
					kilogram = num;
					gram = num * 1000;
					milligram = num * 1000000;
					pound = num * 2.20462;
					ounce = num * 35.274;
				}
				break;
			case 'milligram':{
				metric_ton = num / 100000000;
				kilogram = num /1000000 ;
				milligram =num;
				gram = num * 0.001;
				pound = num * 2.2046 * 1000000;
				ounce = num * 3.5274 * 100000;
			}
			break;
			case 'gram':{
				metric_ton = num / 1000000;
				kilogram = num * 0.001;
				milligram  =num * 1000;
				pound  = num * 0.00220462;
				ounce  = num * 0.035274;
			}
			break; 
			case 'pound':{
				metric_ton = num * 0.000453592;
				kilogram = num * 0.453592;
				milligram = num * 453592;
				gram = num * 453.592;
				pound  = num ;
				ounce = num * 16;
			}
			break;
			case 'ounce':{
				metric_ton = num * (2.835 / 100000);
				kilogram = num * 0.0283495;
				milligram = num * 28349.5;
				gram = num * 28.3495;
				ounce = num * (3.5274/100000);
			}
			break;
			default:
				break;
			}
			return {'metric_ton': metric_ton, 'milligram': milligram, 'gram':gram, 'kilogram': kilogram, 'pound': pound, 'ounce':ounce};
		}	
		function digitalStorage(num, unit){
			var byt_, kilobyte, megabyte, gigabyte, terabyte;
			byt_= kilobyte= megabyte= gigabyte= terabyte;
			switch(unit){
				case 'byt_':{
					byt_ = num ;
					kilobyte = num * 0.001;
					megabyte =num / 1000000;
					gigabyte = num / 1000000000;
					terabyte = num / 1000000000000;
				}
				break;
				case 'kilobyte':{
					byt_ = num * 1000;
					kilobyte= num;
					megabyte =num * 0.001;
					gigabyte = num / 1000000;
					terabyte = num / 1000000000;
				}
				break;
				case 'megabyte':{
					byt_ = num * 1000000;
					kilobyte = num * 1000;
					megabyte = num;
					gigabyte = num * .001;
					terabyte = num / 1000000;
				}
				break;
				case 'gigabyte':{
					byt_ = num * 1000000000;
					kilobyte = num * 100000000;
					megabyte =num * 1000;
					gigabyte = num ;
					terabyte = num / 1000 ;
				}
				break;
				case 'terabyte':{
					byt_ = num *  1000000000000;
					kilobyte = num * 1000000000;
					megabyte =num * 1000000;
					gigabyte = num * 1000;
					terabyte = num  ;
				}
				break;
				default:
					break;
			}
			return {'byt_':byt_, 'kilobyte':kilobyte, 'megabyte': megabyte, 'gigabyte': gigabyte, 'terabyte':terabyte};
			//Petabyte to be added....
		}
		function time(num, unit){
			var second , minute, hour, day, month, year, decade, century;
			second = minute = hour = day = month = year = decade =century =0;
			switch(unit){
				case 'second':{
					second = num  ;
					minute = num * 0.0166667;
					hour  = num * 0.000277778;
					day = num * (1.1574/ 100000);
					month = num * (3.8027 / 10000000);
					year = num * (3.1689 / 100000000);
					decade = num * (3.1689 / 1000000000);
					century = num * (3.1689 / 10000000000);
				} break;
				case 'minute':{
					second = num * 60;
					minute = num ;
					hour  = num * 0.0166667;
					day = num * 0.000694444;
					month = num * (2.2816 / 100000);
					year = num * (1.9013 / 1000000);
					decade = num * (1.9013 / 10000000);
					century = num * (1.9013 / 100000000);
				} break;
				case 'hour':{
					second = num * 3600;
					minute = num * 60;
					hour  = num ;
					day = num * 0.0416667;
					month = num * 0.00136895;
					year = num * 0.00011408;
					decade = num * (1.1408 / 100000);
					century = num * (1.1408 / 1000000);
				} break;
				case 'day':{
					second = num * 86400;
					minute = num * 1440;
					hour  = num * 24;
					day = num  ;
					month = num * 0.0328549;
					year = num * 0.00273791;
					decade = num * 0.000273791;
					century = num * (2.7379 / 100000);
				} break;
				case 'month':{
					second = num * 2.63 * 1000000;
				}
					/*minute = num * ;
					hour  = num * ;
					day = num * ;
					month = num ;
					year = num * ;
					decade = num * ;
					century = num * ;
				} break;
				case 'year':{
					second = num * ;
					minute = num * ;
					hour  = num * ;
					day = num * ;
					month = num * ;
					year = num  ;
					decade = num * ;
					century = num * ;
				} break;
				case 'decade':{
					second = num * ;
					minute = num * ;
					hour  = num * ;
					day = num * ;
					month = num * ;
					year = num * ;
					decade = num ;
					century = num * ;
				} break;
				case 'century':{
					second = num * ;
					minut = num * ;
					hour  = num * ;
					day = num * ;
					month = num * ;
					year = num * ;
					decade = num * ;
					century = num ;
				} */ break;
				default:
					break;
			}
		}
		function fuel_consumption(num, unit){
			var km_litre, MPG, litre_100;
			km_litre = MPG = litre_100 = 0;
			switch(unit){
				case 'km_litre':{
					km_litre = num;
					MPG = num * 2.82481;
					litre_100 = num * 100;
					break;
				}
				case 'MPG':{
					km_litre = num * 0.354006;
					MPG  = num;
					litre_100 = num * 282.481;
					break;
				}
				case 'litre_100':{
				km_litre = num * 100;
				MPG = num * 282.481;
				litre_100 = num;
				break;
				}
				default : 
					break;
			}

			return {'km_litre':km_litre, 'MPG':MPG, 'litre_100':litre_100};
		}
		function length(num,unit){
			var kilometre, metre, mile, foot, yard, inch;
			kilometre = metre = mile = foot = yard = inch = 0;
			switch(unit){
				case 'kilometre':{
					kilometre = num;
					metre = num * 1000;
					mile = num * 0.621371;
					foot = num * 3280.84;
					yard = num * 1093.61;
					inch = num * 39370.1;
					break;
				}
				case 'metre':{
					kilometre = num * 0.001;
					metre = num;
					mile = num * 0.000621371;
					foot = num * 3.28084;
					yard = num * 1.09361;
					inch = num * 39.3701;
					break;
				}
				case 'mile':{
					kilometre = num * 1.60934;
					metre = num * 1609.34;
					mile = num ;
					foot = num * 5280;
					yard = num * 1760;
					inch = num * 63360;
					break;
				}
				case 'foot':{
					kilometre = num * 0.0003048;
					metre = num * 0.3048;
					mile = num * 0.000189394;
					foot = num;
					yard = num * 0.333333;
					inch = num * 12;
				}
				case 'yard':{
					kilometre = num * 0.0009144;
					metre = num * 0.9144;
					mile = num * 0.000568182;
					foot = num * 3;
					yard = num;
					inch = num * 36;

				}
				case 'inch':{
					kilometre = num * Math.pow(2.54, -5);
					metre = num * 0.0254;
					mile = num * Math.pow(1.5783, -5);
					foot = num * 0.0833333;
					yard = num * 0.0277778;
					inch = num;
				}
				default: break;
			}
			return {'kilometre':kilometre, 'metre':metre, 'mile':mile, 'foot':foot, 'yard':yard, 'inch':inch};
		}
		function metric_selector(metric, value, unit){
			value = parseInt(value);
			switch(metric){
				case 'Temperature':
					return temperature(value, unit);
					break;
				case 'Speed':
					return speed(value, unit);
					break;
				case 'Mass':
					return mass(value, unit);
					break;
				case 'DigitalStorage':
					return digitalStorage(value, unit);
					break;
				case 'Time':
					return time(value, unit);
					break;
				case 'FuelConsumption':
					return fuel_consumption(value, unit);
					break;
				case 'Length':
					return length(value, unit);
					break;
				default:
					break;
			}
		}
//End of the program.
 

			
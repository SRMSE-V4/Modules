var M = {
// constant used in approximations
'SMALL_NUMBER': 1e-10,
'log': function log(x, base) {
if (typeof base != "number" && !(base instanceof Number)) {
base = 10;
}
return (Math.log(x) / Math.log(base));
},

'round': function round(x, places) {
if (typeof places != "number" && !(places instanceof Number)) {
places = 2;
}
return (Math.round(x * Math.pow(10, places)) / Math.pow(10,places));
},
'approximateFraction': function approximateFraction(x, maxDenominator) {
maxDenominator = parseInt(maxDenominator);
if (typeof maxDenominator != "number" && !(maxDenominator instanceof Number)) {
maxDenominator = 16;
}
var approx = 0;
var error = 0;
var best = 0;
var besterror = 0;
for (var i = 1; i <= maxDenominator; i++) {
approx = Math.round(x / (1 / i));
error = (x - (approx / i))
if (i==1) {
best = i;
besterror = error;
}
if (Math.abs(error) < Math.abs(besterror)) {
best = i;
besterror = error;
}
}
// return x/1 instead of 0/0 if a better solution can't be found
var solution = (Math.round(x / (1 / best)) + "/" + best)
if (solution == "0/0") {
solution = x + "/" + 1
}
return solution;
},
'sum':function sum(a,b){
	sum=a+b;
	return sum;
}
'difference':function difference(a,b){
	difference=a-b;
	return difference;
}
'product':function product(a,b){
	product=a*b;
	return product;
}
'divide':function divide(a,b){
	quotient=a/b;
	return quotient;
}
'convertBase': function convertBase (number, ob, nb) {
number = number.toUpperCase();
var list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var dec = 0;
for (var i = 0; i <= number.length; i++) {
dec += (list.indexOf(number.charAt(i)) * Math.pow(ob, (number.length - i - 1)));
}
number = "";
var magnitude = Math.floor(Math.log(dec) / Math.log(nb));
for (var i = magnitude; i >= 0; i--) {
var amount = Math.floor(dec / Math.pow(nb, i));
number = number + list.charAt(amount);
dec -= amount * Math.pow(nb, i);
}
return number;
},
'ln': function(x) {
return Math.log(x);
},
'toDegrees': function toDegrees(radians) {
return (radians / (Math.PI / 180));
},
'toRadians': function toRadians(degrees) {
return (degrees * (Math.PI / 180));
},
'random': function random(rangeStart, rangeEnd) {
if (typeof rangeStart != "number" && !(rangeStart instanceof Number)) {
rangeStart = 0;
}
if (typeof rangeEnd != "number" && !(rangeEnd instanceof Number)) {
rangeEnd = 1;
}
// if there's no difference between the two points
if (rangeStart == rangeEnd) {
// throw new Error("The start and end points of the range in which the random number is to be found are the same, meaning that no random number can be generated.");
return rangeStart;
}
// make sure rangeEnd > rangeStart
if (rangeEnd < rangeStart) {
var tmp = rangeEnd;
rangeEnd = rangeStart;
rangeStart = tmp;
}
return ((Math.random() * (rangeEnd - rangeStart)) + rangeStart);
},
'randint': function random(min, max) {
if (typeof min != "number" && !(min instanceof Number)) {
throw new RangeError("min must be a valid number >= 0")
}
if (typeof max != "number" && !(max instanceof Number)) {
throw new RangeError("max must be a valid number >= 0")
}
return Math.floor(Math.random()*(max-min+1)+min)
},
'normal': function normal(mean, deviation) {
if (typeof mean != "number" && !(mean instanceof Number)) {
throw new RangeError("mean must be a valid number")
}
if (typeof deviation != "number" && !(deviation instanceof Number)) {
throw new RangeError("deviation must be a valid number > 0")
}
var x = this.random(0, 1);
var y = this.random(0, 1);
var z1 = Math.sqrt(-2*Math.log(x))*Math.cos(2*Math.PI*y);
return (z1 * deviation) + mean;
},
'factorial': function factorial(num) {
num = parseInt(num)
if (num < 0) {
return NaN;
}
if (num == 0 || num == 1) {
return 1;
}
var result = 1;
do {
result *= num;
} while (--num > 1)
return result;
},
'bigFactorial': function bigFactorial(num) {
var result = 0
for (var k = 1; k <= num; k++) {
result += Math.log(k);
}
result *= Math.LOG10E;
return Math.exp((result % 1) / Math.LOG10E) + 'e' + Math.floor(result);
},
'gcd': function gcd() {
var args = Array.prototype.slice.call(arguments);
function __gcd(a, b) {
return (b == 0) ? a : __gcd(b, a % b);
}
if (args.length > 1) {
args.push(__gcd(args.shift(), args.shift()));
return gcd.apply(this, args);
}
return args[0];
},
'lcm': function lcm() {
var args = Array.prototype.slice.call(arguments);
function __lcm(a, b) {
return (a / gcd(a,b) * b);
}
if (args.length > 1) {
args.push(__lcm(args.shift(), args.shift()));
return lcm.apply(this, args);
}
return args[0];
},
'limit': function limit(f, x, places) {
if (typeof places != "number" && !(places instanceof Number)) {
places = 10;
}
var atX = f(x);
if (!isNaN(atX)) {
return atX;
} else { // else we got a NaN
// if x is Infinity
if (x === Number.POSITIVE_INFINITY) {
return this.limitLeft(f, x, places);
// else if x is -Infinity
} else if (x === Number.NEGATIVE_INFINITY) {
// approach from the right
return this.limitRight(f, x, places);
// else if we don't have a number
} else if (isNaN(x)) {
return Number.NaN;
} else {
// approach from both left and right
var left = this.limitLeft(f, x, places);
var right = this.limitRight(f, x, places);
if (left == right) {
return left;
}
return Number.NaN;
}
}
},
// approach x from values greater than x
'limitRight': function limitRight(f, x, places) {
if (typeof places != "number" && !(places instanceof Number)) {
places = 10;
}
// populate test numbers
var testNums = [];
var testResults = [];
// use x as the input seed for the numbers used in our approximation
var testNumber = x;
if (x === Number.POSITIVE_INFINITY) {
return Number.NaN;
} else if (x === Number.NEGATIVE_INFINITY) {
testNumber = -Number.MAX_VALUE / 10;
}
var verySmallNumber = M.SMALL_NUMBER;
if (places > 10) {
verySmallNumber = eval("1e-" + places);
}
// check five times against our numbers very slightly different from x
for (var k = 0; k < 5; k++) {
testNumber += verySmallNumber;
testNums.push(testNumber);
testResults.push(f(testNumber));
}
var allRounded = testResults.map(function(a) {
return M.round(a, places);
});
var allEqual = true;
for (var k = 1; k < allRounded.length; k++) {
allEqual = allEqual && (allRounded[k-1] == allRounded[k]);
}
// if all the rounded values are equal
if (allEqual == true) {
// return the rounded value
return allRounded[0];
}
return Number.NaN;
},
// approach x from values less than x
'limitLeft': function limitLeft(f, x, places) {
if (typeof places != "number" && !(places instanceof Number)) {
places = 10;
}
// populate test numbers
var testNums = [];
var testResults = [];
// use x as the input seed for the numbers used in our approximation
var testNumber = x;
if (x === Number.NEGATIVE_INFINITY) {
// can't approach from the left
return Number.NaN;
} else if (x === Number.POSITIVE_INFINITY) {
// use the largest number possible to approach Infinity
testNumber = Number.MAX_VALUE / 10;
}
var verySmallNumber = M.SMALL_NUMBER;
if (places > 10) {
verySmallNumber = eval("1e-" + places);
}
for (var k = 0; k < 5; k++) {
testNumber -= verySmallNumber;
testNums.push(testNumber);
testResults.push(f(testNumber));
}
var allRounded = testResults.map(function(a) {
return M.round(a, places);
});
var allEqual = true;
for (var k = 1; k < allRounded.length; k++) {
allEqual = allEqual && (allRounded[k-1] == allRounded[k]);
}
// if all the rounded values are equal
if (allEqual == true) {
// return the rounded value
return allRounded[0];
}
return Number.NaN;
},
'derivative': function derivative(f, x) {
return (f(x + M.SMALL_NUMBER) - f(x)) / M.SMALL_NUMBER;
},
// RFC 4122 version 4 UUID
'UUID': function() {
return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
return v.toString(16);
});
}


//the integrate function, requires the module to be imported first, math.js

function f(x) {
	//enter the function here, in terms of X. Need to take that as the input
}

/*
var math = require('../index');

/**
 * Calculate the numeric integration of a function
 * @param {function} f
 * @param {number} start
 * @param {number} end
 * @param {number} [step=0.01]
 */
function integrate(f, start, end, step) {
  var total = 0;
  step = step || 0.01;
  for (var x = start; x < end; x += step) {
    total += f(x + step / 2) * step;
  }
  return total;
}

*/




};


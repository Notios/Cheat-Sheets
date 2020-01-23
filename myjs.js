function myFunction() {

	document.getElementById("demo").innerHTML = "Paragraph changed.";
}

var x, y, z;    
x = 5; 
y = 6;
z = x + y;  

function myAdd() {

	document.getElementById("sum").innerHTML = z;
}


var price1 = 5;
var price2 = 6;
var total = price1 + price2;

function sum() {

	document.getElementById("demo1").innerHTML = z;
}

//

function mynumb() {
	var x, text;

	// Get the value of the input field with id="numb"
	x = document.getElementById("numb").value;

	// If x is Not a Number or less than one or greater than 10
	if (isNaN(x) || x < 1 || x > 10) {
		text = "Input not valid";
	} 
	else {
		text = "Input OK";
	}
	document.getElementById("numb1").innerHTML = text;
}

function birthday() {

	var x,text;

	// Get the value of the input field with id="numb"
	x = document.getElementById("birth").value;
	text = 2020-x;
	
	document.getElementById("birth1").innerHTML = text;
}
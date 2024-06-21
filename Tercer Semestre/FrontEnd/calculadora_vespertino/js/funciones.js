var operador_aritmetico = "";

function asignarNumero(numero){
	// Si no se ha seleccionado un operador aritmético, se asigna el número al primer input
	if(!operador_aritmetico || !document.getElementById("inputNumero1").value){
		let numero_completo = document.getElementById("inputNumero1").value;
		numero_completo += numero;
		document.getElementById("inputNumero1").value = numero_completo;
	// Si se ha seleccionado un operador aritmético, se asigna el número al segundo input
	}else{
		let numero_completo = document.getElementById("inputNumero2").value;
		numero_completo += numero;
		document.getElementById("inputNumero2").value = numero_completo;
	}
}

function operadorAritmetico(operador){
	if(!document.getElementById("inputNumero1").value){
		alert("Debe ingresar un número antes de seleccionar un operador aritmético");
		return;
	}
	operador_aritmetico = operador;
	document.getElementById("inputOperador").value = operador_aritmetico;
}

function calculo(){
	let numero1 = parseInt(document.getElementById("inputNumero1").value);
	let numero2 = parseInt(document.getElementById("inputNumero2").value);
	
	switch(operador_aritmetico){
		case '+':
			document.getElementById("inputResultado").value = numero1 + numero2;
			break;
		case '-':
			document.getElementById("inputResultado").value = numero1 - numero2;
			break;
		case '*':
			document.getElementById("inputResultado").value = numero1 * numero2;
			break;
		case '/':
			document.getElementById("inputResultado").value = numero1 / numero2;
			break;
		default:
			console.log("Debe seleccionar un operador");
	}
}

function limpiar(){
	document.getElementById("inputNumero1").value = "";
	document.getElementById("inputNumero2").value = "";
	document.getElementById("inputOperador").value = "";
	document.getElementById("inputResultado").value = "";
	operador_aritmetico = "";
}
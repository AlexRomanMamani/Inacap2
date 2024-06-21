// Creación de un objeto myCar utilizando new Object()
const myCar = new Object();
myCar.make = 'Ford';    // Asignación de la propiedad make
myCar.model = 'Mustang'; // Asignación de la propiedad model
myCar.year = 1969;      // Asignación de la propiedad year

// Creación de un objeto myCar2 utilizando la sintaxis de objeto literal
const myCar2 = {
    make: 'AAA',
    model: 'Elantra',
    year: 1969
};

// Mostrar las propiedades del objeto myCar
console.log(myCar.make, myCar.model, myCar.year);

// Iteración sobre las propiedades del objeto myCar2 y mostrar claves y valores
for (let key in myCar2) { 
    console.log(key, myCar2[key]);
}

// Crear variables y usarlas para crear otro objeto myCar3
let make = "Mazda";
let model = "Demio";
let year = 2000;
const myCar3 = { year, make, model }; // Asignación de variables directamente como propiedades
console.log(myCar3); // Mostrar el objeto myCar3

// Definir una función de flecha sumar que toma dos argumentos y devuelve su suma
const sumar = (a, b) => a + b;
console.log(sumar(2, 3)); // Llamar a la función sumar y mostrar el resultado

// Crear variables x y y, y usarlas para crear el objeto rectangulo
let x = 10;
let y = 20;
const rectangulo = { x, y };

// Definir una función que calcula el área de un rectángulo usando destructuración
function calcularArea(rectangulo) {
    const { x, y } = rectangulo;
    return x * y; // Calcular y devolver el área
}

// Definir otra función que calcula el área de un rectángulo usando destructuración en el parámetro
function calcularArea2({ x, y }) {
    return x * y; // Calcular y devolver el área
}

// Definir una función de flecha que calcula el área de un rectángulo usando destructuración en el parámetro
const calcular3 = ({ x, y }) => x * y;

console.log(calcularArea(rectangulo)); // Llamar a la función calcularArea y mostrar el resultado
console.log(calcularArea2(rectangulo)); // Llamar a la función calcularArea2 y mostrar el resultado
console.log(calcular3(rectangulo)); // Llamar a la función calcular3 y mostrar el resultado

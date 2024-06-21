// Creación de objeto usuario, sintaxis de objeto literal
const usuario = {
    nombre: 'Alex',
    apellido: 'Mamani'
}
// Funcion 1
function obtenerNombreCompleto1(usuario){
    const {nombre, apellido} = usuario;
    return nombre + ' ' + apellido;
}
// Funcion 2
function obtenerNombreCompleto2({nombre, apellido}){
    return nombre + ' ' + apellido;
}
// Funcion 3
const obtenerNombreCompleto3 = ({nombre, apellido}) => nombre + ' ' + apellido;

console.log(obtenerNombreCompleto1(usuario));
console.log(obtenerNombreCompleto2(usuario));
console.log(obtenerNombreCompleto3(usuario));

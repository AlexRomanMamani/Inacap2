// Crea una función calcularTotalCompra que recibe un arreglo productos como parámetro. Cada elemento del
// arreglo productos es un objeto con las propiedades nombre, precio y cantidad. La función debe desestructurar
// cada objeto producto y calcular el total de la compra (precio por cantidad) para todos los productos. Finalmente,
// la función debe retornar el total de la compra.

const productos = [
    {
        nombre: 'Tornillo',
        precio: 5,
        cantidad: 2
    },
    {
        nombre: 'Martillo',
        precio: 3,
        cantidad: 2
    },
    {
        nombre: 'Alicate',
        precio: 2,
        cantidad: 2
    }
]

function calcularTotalCompra(productos){
    let total = 0;
    for (let i = 0; i < productos.length; i++) {
        // Desestructuración
        const {precio, cantidad} = productos[i];
        total += precio * cantidad;
    }
    return total;
}

console.log(productos[2])
console.log(calcularTotalCompra(productos));
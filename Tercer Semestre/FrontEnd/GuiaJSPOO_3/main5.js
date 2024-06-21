let productos = [
    {
        nombre: 'papasDoraditas',
        precio: 500,
        categoria: "Verduras"
    },
    {
        nombre: 'CebollasDulces',
        precio: 900,
        categoria: "Verduras"
    },
    {
        nombre: 'Manzana',
        precio: 1000,
        categoria: "Frutas"
    },
    {
        nombre: 'Platano',
        precio: 1500,
        categoria: "Frutas"
    }
]

console.log(productos)

let categoria = "Verduras";
let precioMaximo = 1500;

const filtros = {categoria, precioMaximo};

const filtrarYTransformarProductos = (productos, {categoria, precioMaximo}) => {
    let nuevoArreglo = [];
    for (let i = 0; i < productos.length; i++){
        if (categoria == productos[i].categoria && productos[i].precio <= precioMaximo){
            let nombreCorto = productos[i]['nombre'].substring(0,10);
            let precioConDescuento = productos[i]['precio'] * 0.9;
            let categoriaMayuscula = productos[i]['categoria'].toUpperCase();
            const nuevoProducto = {nombreCorto, precioConDescuento, categoriaMayuscula};
            nuevoArreglo.push(nuevoProducto);
        }
    }
    return nuevoArreglo;
}

console.log(filtrarYTransformarProductos(productos, filtros))

//Estudiar
//Manipulación DOM con JS
//Estructura Bootstrap
//Desestructuración: funciones, objetos, arreglos
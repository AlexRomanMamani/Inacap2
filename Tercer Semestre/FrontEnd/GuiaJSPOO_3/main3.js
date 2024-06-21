// Crea una función extraerPropiedades que recibe un objeto datos y un arreglo propiedades como parámetros. El
// objeto datos contiene diferentes propiedades. El arreglo propiedades contiene los nombres de las propiedades
// que se quieren extraer del objeto datos. La función debe desestructurar el arreglo propiedades y retornar un
// nuevo objeto que contenga solo las propiedades especificadas en el arreglo propiedades, con sus valores
// correspondientes del objeto datos.

function extraerPropiedades(datos, propiedades) {
    // Inicializamos un objeto vacío donde almacenaremos las propiedades extraídas
    const resultado = {};

    // Iteramos sobre el arreglo de propiedades
    for (const prop of propiedades) {
        // Usamos desestructuración para extraer la propiedad si existe
        const { [prop]: value } = datos;
        console.log(value)
        // Si la propiedad existe en datos, se agrega al resultado
        if (value !== undefined) {
            resultado[prop] = value;
        }
    }

    // Retornamos el objeto con las propiedades extraídas
    return resultado;
}

// Ejemplo de uso
const datos = {
    nombre: 'Juan',
    edad: 30,
    profesion: 'Ingeniero',
    pais: 'España'
};

const propiedades = ['nombre', 'pais'];

const resultado = extraerPropiedades(datos, propiedades);
console.log(resultado); // Output: { nombre: 'Juan', pais: 'España' }

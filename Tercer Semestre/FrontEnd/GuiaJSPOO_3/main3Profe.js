const datos = { a: 1, b: 2, c: 3, d: 4 };
const propiedades = ['a', 'c'];

const extraerPropiedades = (datos, propiedades) => {
  let objeto = {};
  /*
  propiedades.forEach(propiedad => {
    objeto[propiedad] = datos[propiedad];
  });
  */
  for (let i = 0; i < extraer.length; i++) {

    objeto[propiedades[i]] = datos[propiedades[i]];
  }
  return objeto;
}

console.log(extraerPropiedades(datos, propiedades));
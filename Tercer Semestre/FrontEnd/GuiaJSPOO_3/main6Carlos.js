const validarDatosUsuario = (datosUsuario) => {
    const {nombre = '', email = '', pais = ''} = datosUsuario;
    if (typeof nombre !== 'string' || nombre === '') {
        console.warn('Nombre no válido');
    }
    if (typeof email !== 'string' || !email.includes('@')) {
        console.warn('Email no válido');
    }
    //typeof es para saber si es un string, y .length para saber la longitud
    if (typeof pais !== 'string' || pais.length !== 2) {
        console.warn('País no válido');
    }
    return {nombre, email, pais};
}

const datosUsuario = {
    nombre: 'Juan',
    email: 'ssansasnasik@gmail.com',
    pais: 'AR'
};

console.log(validarDatosUsuario(datosUsuario));
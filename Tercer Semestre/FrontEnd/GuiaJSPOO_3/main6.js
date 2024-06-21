// Crear objeto
const datosUsuario = {
    nombre: '',
    email: 'correocorreo.cl',
    pais: 'CLasdasd'
}


const validarDatosUsuario = ({nombre, email, pais}) => {
    let nombre_temp, email_temp, pais_temp
    if (nombre === ""){
        nombre_temp = "nombre por defecto";
        console.log(`Advertencia, nombre venia vacio, se asigna nombre por defecto ${nombre_temp}`)
    }else{
        nombre_temp = nombre
    }
    if (!email.includes('@')){
        email_temp = "defecto@correo.cl"
        console.log(`Advertencia, email no cumple con formato, se asigna email por defecto ${email_temp}`)
    }else{
        email_temp = email
    }
    if (pais.length !== 2){
        pais_temp = "CL"
        console.log(`Advertencia, pais no cumple con formato, se asigna pais por defecto ${pais_temp}`)
    }else{
        pais_temp = pais
    }
    const usuarioValido = {nombre_temp, email_temp, pais_temp}
    return usuarioValido
}

console.log(validarDatosUsuario(datosUsuario))
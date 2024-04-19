function generarTabla(){
    let filas = document.getElementById("filas").value;
    let columnas = document.getElementById("columnas").value;
    let tabla = "<div class='table-responsive'><table class='table table-striped table-bordered table-hover table-sm'>";
    for(let i = 0; i < filas; i++){
        tabla = tabla + "<tr>";
        for(let j = 0; j < columnas; j++){
            tabla = tabla + "<td> Fila " + (i+1) + ", Columna " + (j+1) + "</td>";
        }
        tabla = tabla + "</tr>";
    }
    tabla = tabla + "</table></div>";
    document.getElementById("tabla").innerHTML = tabla;
}
clientes = {
    "5245905":{
        "nombre": "Mathias", 
        "apellido": "Santos", 
        "numero": "0986365554",
        "dir": "Lambare"
    }
}

def bucarCliente(ci):
    if ci in clientes:
        data = clientes[ci]
        return{
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": data["nombre"],
            "nombre": data["nombre"],
            "apellido": data["apellido"],
            "numero": data["numero"],
            "dir": data["dir"]
        }
    else:
        return{
            "accion": "Cliente no encontrado",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci,
        }
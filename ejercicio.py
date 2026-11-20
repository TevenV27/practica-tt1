peliculas = [
    {
        "name": "Harry Potter y la piedra filosofal",
        "year": "2001",
        "duration": "152 min"
    },
    {
        "name": "Piratas del caribe, la venganza de Salazar",
        "year": "2017",
        "duration": "136 min"
    }
]

for pelicula in peliculas:
    print(f"""
    Nombre: {pelicula["name"]}
    Año: {pelicula["year"]}
    Duración: {pelicula["duration"]}
    """
    )
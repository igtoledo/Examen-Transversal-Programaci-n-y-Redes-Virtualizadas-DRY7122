import requests

API_KEY = 'd3e2efb3-653d-48a0-85d3-00405cb629f5	' 

def obtener_datos_viaje(origen, destino, vehiculo):
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle={vehiculo}&locale=es&instructions=true&calc_points=true&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def mostrar_narrativa(data):
    for instruccion in data['paths'][0]['instructions']:
        print(f"{instruccion['distance']} metros: {instruccion['text']}")

def main():
    while True:
        print("Ingrese 's' para salir.")
        origen = input("Ingrese la Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese la Ciudad de Destino: ")
        if destino.lower() == 's':
            break
        
        vehiculo = input("Ingrese el medio de transporte (car, bike, foot): ").lower()
        if vehiculo == 's':
            break

        try:
            data = obtener_datos_viaje(origen, destino, vehiculo)
            distancia_km = data['paths'][0]['distance'] / 1000
            distancia_millas = distancia_km * 0.621371
            duracion = data['paths'][0]['time'] / 3600000 
            
            print(f"\nDistancia entre {origen} y {destino}:")
            print(f"{distancia_millas:.2f} millas")
            print(f"{distancia_km:.2f} kilómetros")
            print(f"Duración del viaje: {duracion:.2f} horas")

            print("\nNarrativa del viaje:")
            mostrar_narrativa(data)

        except Exception as e:
            print(f"Error al obtener datos del viaje: {e}")

if __name__ == "__main__":
    main()

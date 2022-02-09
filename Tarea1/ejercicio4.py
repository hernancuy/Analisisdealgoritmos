
import dijkstra
import csv

def ciudad(ciudades, busqueda):
    result = [ciudad for ciudad in ciudades if ciudad[2] == busqueda]

    if result == []: # or if not result
        return "item not found"
    else:
        return result


def main():
    
    # Ejercicio 4

    # Dada una base de datos con los costos de todos los vuelos del mundo, encontrar la serie de vuelos 
    # que con el menor costo posible nos permitan viajar desde Bogotá hacia la ciudad en la que queremos tomar vacaciones.
    print("\n\n")
    print("Ejercicio 4")
    print("\n\n")
    print("Dada una base de datos con los costos de todos los vuelos del mundo, encontrar la serie de vuelos") 
    print("que con el menor costo posible nos permitan viajar desde Bogotá hacia la ciudad en la que queremos tomar vacaciones.")
    print("\n\n")

    #define el grafo
    g = dijkstra.Grafica()

    # Cargue archivo aeropuertos https://es.wikipedia.org/wiki/Anexo:Aeropuertos_seg%C3%BAn_el_c%C3%B3digo_IATA      
    with open("aeropuertos.csv", "r", encoding="utf-8") as csv_file:
        csv_reader_ciudades = csv.reader(csv_file, delimiter=';')    
        ciudades = list(csv_reader_ciudades)
        for row in ciudades:
            g.agregaVertice(row[0])
        
    #Carga base de datos de aeropuertos de las vuelos

    with open("vuelos.csv", "r", encoding="utf-8") as csv_file:
        csv_reader_vuelos = csv.reader(csv_file, delimiter=';')    
        vuelos = list(csv_reader_vuelos)
        for row2 in vuelos:
            g.agregarArista(row2[0],row2[1], int(row2[2]))


    #funcionando
    #ciudad origen
    origin = input("Ingrese el nombre de la ciudad origen: ")
    ciudadOrigen = ciudad(ciudades, origin)
    
    #ciudad destino
    destination = input("Ingrese el nombre de la ciudad destino: ")
    ciudadDestino = ciudad(ciudades, destination)
    
    print("\nSu viaje será desde el " +str(ciudadOrigen[0][1])+ " ubicado en la ciudad de " + str(ciudadOrigen[0][2]) + "/"+str(ciudadOrigen[0][3])+" \nhasta el " +str(ciudadDestino[0][1])+ " en ciudad de " +str(ciudadDestino[0][2])+ "/"+str(ciudadOrigen[0][3])+". ")
 
    #Respuesta final
    print("\n\nLa ruta más rapida por Dijkstra junto con su costo es: ")

    #Nodo inicial
    g.dijkstra(ciudadOrigen[0][0])
    
    #Camino total

    ruta = g.camino(ciudadOrigen[0][0], ciudadDestino[0][0])
    print(ruta)
    #Impresion de la grafica opcional
    #print("\n Los valores finales de la grafica son los siguientes:")
    #g.imprimirGrafica()
    
main()

import csv, sys
nome_ficheiro = 'Data_frame_ordenado.csv'

matriz = []
with open(nome_ficheiro, 'rb') as ficheiro:
    reader = csv.reader(ficheiro)
    try:
        for linha in reader:
			matriz.append(linha)
           
    except csv.Error as e:
        sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))

matrizfinal = []
erros = []

def newAresta(j):
		aresta = []
		aresta.append(matriz[j][0])
		aresta.append(matriz[j][1])
		aresta.append(matriz[j][2])
		aresta.append(matriz[j][3])
		aresta.append(matriz[j][4])
		aresta.append(matriz[j][6])
		aresta.append(matriz[j][7])
		matrizfinal.append(aresta)


def newerro(j):
		aresta = []
		aresta.append(matriz[j][0])
		aresta.append(matriz[j][1])
		aresta.append(matriz[j][2])
		aresta.append(matriz[j][3])
		aresta.append(matriz[j][4])
		aresta.append(matriz[j][6])
		aresta.append(matriz[j][7])
		aresta.append(matriz[j][5])
		erros.append(aresta)

for i in range(1,len(matriz)):
	erro = False
	if(not matriz[i][0] == 0):
		for j in range(i+1,len(matriz)):
				
			if(matriz[i][5] == matriz[j][5]):
				newerro(j)
				matriz[j][0] = 0
				erro = True
										
		if(not erro):
			newAresta(i)
		else:
			newerro(i)


		
with open("df_filtro_vin.csv", 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Price', 'Year', 'Mileage', 'City', 'State', 'Make', 'Model'])
    for linha in matrizfinal:
        spamwriter.writerow(linha)
        
        		
with open("df_vin_erros.csv", 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Price', 'Year', 'Mileage', 'City', 'State', 'Make', 'Model','erro'])
    for linha in erros:
        spamwriter.writerow(linha)


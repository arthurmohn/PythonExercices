def tempo_download(tam, vel):
    tempo_segundos = tam/vel
    minutos = tempo_segundos//60
    segundos = tempo_segundos - minutos

    return minutos, segundos

tam = float(input("Entre com o tamanho do arquivo: "))
vel = float(input("Entre com a velocidade da internet: "))

minutos, segundos = tempo_download(tam, vel)

print(f"O tempo de download eh: {minutos} minutos e {segundos} segundos")
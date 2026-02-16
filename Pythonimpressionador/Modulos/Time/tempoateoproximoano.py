import time

# Pega a data/hora atual
agora = time.localtime()
anoatual = agora.tm_year
anonovo = anoatual + 1

# Define 1º de janeiro do próximo ano às 00:00
data_anonovo = (anonovo, 1, 1, 0, 0, 0, 0, 0, -1)

# Converte para timestamp
timestamp_anonovo = time.mktime(data_anonovo)
timestamp_agora = time.mktime(agora)

# Diferença total em segundos
diferenca_segundos = int(timestamp_anonovo - timestamp_agora)

# Quebra em dias, horas, minutos e segundos
dias = diferenca_segundos // (60 * 60 * 24)
resto = diferenca_segundos % (60 * 60 * 24)

horas = resto // (60 * 60)
resto = resto % (60 * 60)

minutos = resto // 60
segundos = resto % 60

print("Timestamp do início do próximo ano:", timestamp_anonovo)
print(f"Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o Ano Novo!")
import time
segundos_hoje = time.time()
print(segundos_hoje)
hora_atual = time.ctime()
print(hora_atual)

#def despertador():
#    minutos = int(input("Digite quantos minutos deseja esperar: "))
#    segundos = minutos * 60
#    print(f"Despertador iniciado! Vou esperar {minutos} minutos...")
#    time.sleep(segundos)
#    print("⏰ O tempo acabou! Despertador tocando!")
#despertador()

def pedagio():
    segundos = 10   # tempo fixo de espera no pedágio (em segundos)
    print(f"🚗 Esperando no pedágio por {segundos} segundos...")

    # contador regressivo
    for i in range(segundos, 0, -1):   # começa em 'segundos' e vai até 1
        print(i)
        time.sleep(1)                  # pausa 1 segundo entre cada número

    print("✅ O pedágio terminou, pode seguir viagem!")

pedagio()


hora_local = time.localtime()
hora_geral = time.gmtime()
print("Hora Local:", hora_local)
print("Hora Geral (UTC):", hora_geral)

dia = hora_local.tm_mday
mes = hora_local.tm_mon
ano = hora_local.tm_year
dia_semana = hora_local.tm_wday

print(f"Data Atual: {dia}/{mes}/{ano}, Dia da Semana: {dia_semana}")
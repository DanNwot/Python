import time
import locale
tempostruct = time.localtime()
print(tempostruct)

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Define para português do Brasil

tempoformatado = time.strftime("%A, %d de %B %Y %H:%M", tempostruct)
print("Data e hora formatada:", tempoformatado)


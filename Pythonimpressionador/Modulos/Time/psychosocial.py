import time

def psychosocial():
    # Duração total aproximada: ~282 segundos (4:42)
    # Tempos aproximados em segundos (início de cada frase principal / parte marcante)
    partes = [
        (0.0,   "♪ Ooh, yeah ♪"),
        (4.0,   "♪ I did my time, and I want out ♪"),
        (9.0,   "♪ So effusive - fade - it doesn't cut ♪"),
        (13.5,  "♪ The soul is not so vibrant ♪"),
        (17.5,  "♪ The reckoning, the sickening ♪"),
        (21.0,  "♪ Packaging subversion, pseudo-sacrosanct perversion ♪"),
        (27.0,  "♪ Go drill your deserts, go dig your graves ♪"),
        (32.0,  "♪ Then fill your mouth with all the money you will save ♪"),
        (38.5,  "♪ Sinking in, getting smaller again ♪"),
        (43.0,  "♪ I'm undone, it has begun ♪"),
        (46.5,  "♪ I'm not the only one ♪"),
        
        (51.0,  "♪ And the rain will kill us all ♪"),
        (54.5,  "♪ Throw ourselves against the wall ♪"),
        (58.0,  "♪ But no one else can see ♪"),
        (61.5,  "♪ The preservation of the martyr in me ♪"),
        
        (66.0,  "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        (69.5,  "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        
        (80.0,  "♪ Oh, there are cracks in the road we lay ♪"),
        (84.5,  "♪ From where the devil fell ♪"),
        (88.0,  "♪ The secrets have gone mad ♪"),
        (91.5,  "♪ This is nothing new ♪"),
        (94.0,  "♪ But when we kill it all before ♪"),
        (98.0,  "♪ The hate was all we had ♪"),
        
        (102.0, "♪ Who needs another mess? We could start over ♪"),
        (108.0, "♪ Just look me in the eyes and say I'm wrong ♪"),
        (113.5, "♪ Now there's only emptiness ♪"),
        (117.5, "♪ But I'm missing something ♪"),
        
        (122.0, "♪ Yeah! ♪"),
        
        (130.0, "♪ And the rain will kill us all ♪"),
        (133.5, "♪ Throw ourselves against the wall ♪"),
        (137.0, "♪ But no one else can see ♪"),
        (140.5, "♪ The preservation of the martyr in me ♪"),
        
        (145.0, "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        (148.5, "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        
        # Parte mais pesada / breakdown ~ 2:45~
        (165.0, "♪ Psychosocial! Psychosocial! ♪ (mais agressivo)"),
        (172.0, "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        (180.0, "♪ Psychosocial! Psychosocial! Psychosocial! ♪"),
        
        # Final com repetição e fade
        (210.0, "♪ Psychosocial... Psychosocial... ♪"),
        (225.0, "♪ Psychosocial... Psychosocial... ♪"),
        (240.0, "♪ (instrumental pesado + gritos) ♪"),
        (260.0, "♪ Psychosocial! ♪"),
        (270.0, "♪ Yeahhhhh! ♪"),
    ]

    print("▶ Iniciando Psychosocial (Slipknot) - modo karaoke/tempo aproximado...\n")
    print("   Dica: toque a música junto pra sincronizar melhor!\n")
    
    inicio = time.time()
    
    for segundos, fala in partes:
        while time.time() - inicio < segundos:
            time.sleep(0.1)   # precisão melhor que 0.5s
        
        # Mostra o tempo formatado mm:ss
        minutos = int(segundos // 60)
        secs = int(segundos % 60)
        print(f"[{minutos:02d}:{secs:02d}] {fala}")
    
    # Espera terminar de vez (pra dar o fade out)
    while time.time() - inicio < 285:
        time.sleep(0.3)
    
    print("\n⏰ Fim da simulação - Psychosocial complete! \\m/")
    print("   Slipknot - All Hope Is Gone (2008) \\m/")

# Roda a função
if __name__ == "__main__":
    psychosocial()
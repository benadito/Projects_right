trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print(f"tv50={tv_50} tv32={tv_32} sorvete={sorvete} saudavel={mais_saudavel}")

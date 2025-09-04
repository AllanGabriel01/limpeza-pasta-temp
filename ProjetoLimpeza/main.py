import os
import shutil
import time

def limpar_temp():
    temp_path = os.environ.get("TEMP")  # Pega a pasta TEMP do usuário
    print(f"Limpando: {temp_path}")

    for item in os.listdir(temp_path):
        item_path = os.path.join(temp_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)  # remove arquivo
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # remove pasta
            print(f"Apagado: {item_path}")
        except Exception as e:
            print(f"Não foi possível apagar {item_path}: {e}")

def executar_periodicamente(intervalo_segundos=3600):
    while True:
        limpar_temp()
        print(f"Aguardando {intervalo_segundos/60:.0f} minutos para próxima limpeza...")
        time.sleep(intervalo_segundos)

if __name__ == "__main__":
    executar_periodicamente(600)  # limpa a cada 10 minutos

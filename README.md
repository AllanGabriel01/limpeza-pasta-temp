# limpeza-pasta-temp
Código Python usado para limpar a pasta de arquivos temporário do usuário do windows.

O código usa bibliotecas padrão do Python (os, shutil e time) para:
Identificar a pasta TEMP do usuário.
Apagar arquivos e pastas dentro dela.
Repetir esse processo de tempos em tempos.

import os: Permite interagir com o sistema operacional (listar arquivos, remover, acessar variáveis de ambiente, etc).

import shutil: Biblioteca usada para apagar pastas inteiras.

import time: Usada para pausar o programa por um tempo (sleep) antes de rodar de novo.

def limpar_temp(): Cria uma função chamada limpar_temp, responsável por apagar os arquivos temporários.

temp_path = os.environ.get("TEMP")  # Pega a pasta TEMP do usuário
os.environ.get("TEMP"): Acessa a variável de ambiente TEMP do Windows, que guarda o caminho da pasta de arquivos temporários (geralmente C:\Users\SEU_USUARIO\AppData\Local\Temp).

Guarda esse caminho na variável temp_path.

print(f"Limpando: {temp_path}")
Mostra na tela qual pasta está sendo limpa (ajuda para depuração e monitoramento).

for item in os.listdir(temp_path):
os.listdir(temp_path): Lista todos os arquivos e pastas dentro da pasta TEMP.

O for percorre cada item dessa lista.

item_path = os.path.join(temp_path, item)
Junta o caminho da pasta temp_path com o nome do arquivo/pasta item, formando o caminho completo.

Exemplo: C:\Users\Allan\AppData\Local\Temp\arquivo123.tmp.

try:
Inicia um bloco try para tentar apagar os arquivos.

Isso é importante porque alguns arquivos podem estar em uso e não podem ser removidos no momento.

if os.path.isfile(item_path) or os.path.islink(item_path):
    os.remove(item_path)  # remove arquivo
Se o item_path for um arquivo ou um atalho (link), apaga com os.remove().


elif os.path.isdir(item_path):
    shutil.rmtree(item_path)  # remove pasta
Se for uma pasta, apaga ela inteira com shutil.rmtree().
Isso remove a pasta e tudo dentro dela.


except Exception as e:
    print(f"Não foi possível apagar {item_path}: {e}")
Se não conseguir apagar (por exemplo, porque o arquivo está em uso), mostra a mensagem de erro, mas continua o processo sem travar o programa.


def executar_periodicamente(intervalo_segundos=3600):
Cria uma função chamada executar_periodicamente que executa a limpeza de tempos em tempos.
intervalo_segundos=3600 define o tempo entre cada limpeza (por padrão, 1 hora).

while True:
Um laço infinito (while True) para o programa rodar continuamente.

limpar_temp()
Chama a função que apaga os arquivos da pasta TEMP.

print(f"Aguardando {intervalo_segundos/60:.0f} minutos para próxima limpeza...")
Mostra na tela quanto tempo falta para a próxima execução.

Divide intervalo_segundos por 60 para converter em minutos.


time.sleep(intervalo_segundos)
Faz o programa aguardar o tempo definido antes de repetir.


if __name__ == "__main__":
    executar_periodicamente(600)  # limpa a cada 10 minutos
Essa parte é o ponto de entrada do programa.

if __name__ == "__main__": garante que o código só rode se for executado diretamente, e não quando importado como módulo em outro script.

executar_periodicamente(600) define que a limpeza será feita a cada 600 segundos (10 minutos).

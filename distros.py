# Cria o arquivo especificado e já adiciona duas distros inicialmente
import os
nome_arquivo = input("Digite o nome do arquivo que deseja criar para salvar as distros: ")
nome_arquivo += ".txt"
conteudo = "Zorin Os \nopenSuse"

while os.path.exists(nome_arquivo):
    resposta = input(f"O arquivo '{nome_arquivo}' já existe. Deseja escolher outro nome? (s/n): ")
    if resposta.lower() == 's':
        nome_arquivo = input("Digite um novo nome para o arquivo: ") + ".txt"
    else:
        break

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo)
print(f"Arquivo '{nome_arquivo}' criado e salvo com sucesso.")

# Adiciona outra distro ao arquivo existente
nova_distro = "\nLinux Mint \n"
with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write(nova_distro)
print(f"Distro  adicionada ao arquivo especificado '{nome_arquivo}' com sucesso.")


#Adicionar itens de uma lista, um por linha, ao arquivo existente
lista_de_distros = ['Ubuntu', 'Kali', 'Debian', 'Arch Linux', 'Fedora']
with open(nome_arquivo, 'a', encoding='utf-8') as arquivo_lista:
    for item in lista_de_distros:
        arquivo_lista.write(item + '\n')
print(f"Distros  adicionadas ao arquivo '{nome_arquivo}' com sucesso.")

# Exibir o conteúdo final do arquivo
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    conteudo_final = arquivo.read()
print("Conteúdo final do arquivo:")
print(conteudo_final)

from cryptography.fernet import Fernet
import os

def carregar_chave():
    if not os.path.exists("chave.key"):
        raise FileNotFoundError("Arquivo de chave não encontrado. Gere uma chave primeiro.")
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    try:
        dados = f.decrypt(dados_encriptados)
    except Exception as e:
        print(f"[!] Erro ao descriptografar {arquivo}: {e}")
        return
    with open(arquivo, "wb") as file:
        file.write(dados)
    print(f"[+] Arquivo descriptografado: {arquivo}")

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "descriptografar.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("\n✅ Todos os arquivos foram descriptografados com sucesso!")

if __name__ == "__main__":
    main()

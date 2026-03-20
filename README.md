# Relatório de Paralelização de Logs

**Aluno:** Kelvin Raphael de Souza Pereira  
**Disciplina:** Concorrência e Paralelismo  
**Atividade:** Processamento Paralelo de Arquivos de Log  
**Professor:** [Nome do Professor]  
**Dados:** Pasta log2, 1000 arquivos .txt

---

## 1. Descrição do Problema
O problema consiste em processar arquivos de log contendo milhões de linhas de texto. O objetivo é extrair informações relevantes (linhas, palavras, caracteres e palavras-chave: erro, warning, info) utilizando execução serial e paralela, medindo tempo, speedup e eficiência.

**Algoritmo utilizado:** leitura de arquivos linha a linha, contagem de palavras e caracteres, paralelizado usando processos do Python (`multiprocessing.Pool`) dividindo os arquivos entre os processos.

**Tamanho da entrada:** 1000 arquivos .txt, totalizando 10.000.000 de linhas.

**Objetivo da paralelização:** reduzir o tempo total de processamento dos arquivos utilizando múltiplos processos.

**Complexidade aproximada:** O algoritmo tem complexidade O(n), onde n é o número total de linhas nos arquivos.

---

## 2. Ambiente Experimental

| Item                  | Descrição                                    |
|-----------------------|----------------------------------------------|
| Processador           | Intel(R) Core(TM) i5-12500 de 12ª geração   |
| Número de núcleos     | 6 núcleos                                    |
| Memória RAM           | 16 GB                                        |
| Sistema Operacional   | Windows 11                                   |
| Linguagem utilizada   | Python 3.10                                  |
| Biblioteca de paralelização | multiprocessing                         |

---

## 3. Metodologia de Testes
- Medição de tempo: `time.time()` antes e depois de cada execução.
- Número de execuções: 1 execução por número de processos.
- Entrada utilizada: pasta `log2` com 1000 arquivos de log `.txt`.
- Configurações testadas:
  - 1 processo (serial)
  - 2 processos
  - 4 processos
  - 8 processos
  - 12 processos
- Cada processo recebeu uma parte dos arquivos da pasta para processar em paralelo.  
- O tempo de execução foi registrado em segundos.

---

## 4. Resultados Experimentais

| Nº de Processos | Tempo de Execução (s) |
|-----------------|----------------------|
| Serial (1)      | 115.96               |
| 2               | 10.71                |
| 4               | 5.75                 |
| 8               | 3.66                 |
| 12              | 3.22                 |

**Resumo de arquivos processados e contagens:**

- Arquivos processados: 1000  
- Total de linhas: 10.000.000  
- Total de palavras: 200.000.000  
- Total de caracteres: 1.366.663.305  

**Contagem de palavras-chave:**

| Palavra | Quantidade |
|---------|------------|
| erro    | 33.332.083 |
| warning | 33.330.520 |
| info    | 33.329.065 |

---

## 5. Cálculo de Speedup e Eficiência

**Fórmulas utilizadas:**

\[
\text{Speedup(p)} = \frac{T_2}{T_p}, \quad
\text{Eficiência(p)} = \frac{\text{Speedup(p)}}{p}
\]

> Observação: usamos o tempo de 2 processos como referência para o speedup inicial.

| Processos | Tempo (s) | Speedup | Eficiência |
|-----------|-----------|---------|------------|
| 2         | 10.71     | 1.0     | 50%        |
| 4         | 5.75      | 1.86    | 46%        |
| 8         | 3.66      | 2.93    | 36%        |
| 12        | 3.22      | 3.33    | 28%        |

---

## 6. Gráficos
- **Gráfico de Tempo:** eixo X = número de processos, eixo Y = tempo total.
- **Gráfico de Speedup:** eixo X = número de processos, eixo Y = speedup.
- **Gráfico de Eficiência:** eixo X = número de processos, eixo Y = eficiência.

*(Os gráficos serão gerados em Python ou Excel usando os dados das tabelas acima.)*

---

## 7. Análise dos Resultados
- O tempo de execução diminuiu conforme aumentamos o número de processos.  
- O ganho de paralelização é visível (speedup maior que 1).  
- A eficiência diminui com mais processos devido a overhead de gerenciamento de processos e distribuição de arquivos.  
- Todos os 1000 arquivos foram processados corretamente, e a contagem de linhas, palavras, caracteres e palavras-chave conferiu com os resultados esperados.

---

## 8. Conclusão
- O paralelismo via processos trouxe ganho significativo de desempenho em comparação à execução serial.  
- O melhor desempenho foi obtido com 12 processos (3.22 s).  
- A eficiência diminui com o aumento do número de processos devido a overhead, mas o tempo total de execução foi reduzido consideravelmente.  

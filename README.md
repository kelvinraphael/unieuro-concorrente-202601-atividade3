# Relatório da Atividade 3 – Paralelização de Logs

**Disciplina:** Concorrência e Paralelismo  
**Aluno:** Kelvin Raphael de Souza Pereira  
**Turma:** [Sua turma]  
**Professor:** [Nome do professor]  
**Dados do experimento:** Processamento de arquivos de log para contagem de linhas, palavras, caracteres e palavras-chave.

---

## 1. Descrição do Problema

O problema consiste em processar milhares de arquivos de log contendo registros operacionais, extraindo informações como número de linhas, palavras, caracteres e contagem de palavras-chave (erro, warning, info). O objetivo é comparar o desempenho do processamento **serial** (1 processo) com o **paralelo** utilizando múltiplos processos (2, 4, 8, 12), medindo tempo, speedup e eficiência.

**Objetivo da paralelização:** reduzir o tempo de execução usando múltiplos processos, aproveitando CPUs multi-core.  

**Complexidade aproximada:** O algoritmo tem complexidade O(n), onde n é o total de linhas de todos os arquivos.

---

## 2. Ambiente Experimental

| Item | Descrição |
|------|-----------|
| Processador | Intel(R) Core(TM) i5-12500 12ª geração |
| Núcleos | 6 núcleos físicos |
| Memória RAM | 16 GB |
| Sistema Operacional | Windows 11 |
| Linguagem utilizada | Python 3.13 |
| Biblioteca de paralelização | multiprocessing |
| Compilador / Versão | Python 3.13 |

---

## 3. Metodologia de Testes

- **Medição de tempo:** utilizou-se `time.time()` antes e depois da execução de cada configuração.  
- **Número de execuções:** 1 execução por configuração.  
- **Entrada utilizada:** pasta `log2` com 1000 arquivos de teste, 10.000 linhas cada.  
- **Configurações testadas:**
  - 1 processo (serial)
  - 2 processos
  - 4 processos
  - 8 processos
  - 12 processos

Cada processo recebeu uma parte dos arquivos para processar, e os resultados foram consolidados no final.

---

## 4. Resultados Experimentais

### 4.1 Tabela de Tempos de Execução

| Nº de Processos | Tempo (s) |
|-----------------|-----------|
| 1 (Serial)      | 20.473    |
| 2               | 10.71     |
| 4               | 5.75      |
| 8               | 3.66      |
| 12              | 3.22      |

### 4.2 Speedup e Eficiência

| Processos | Speedup | Eficiência |
|-----------|---------|------------|
| 1         | 1.00    | 1.00       |
| 2         | 1.91    | 0.955      |
| 4         | 3.56    | 0.89       |
| 8         | 5.59    | 0.699      |
| 12        | 6.36    | 0.53       |

---

## 5. Contagem Consolidade de Arquivos

| Métrica | Quantidade |
|---------|------------|
| Total de linhas | 10.000.000 |
| Total de palavras | 200.000.000 |
| Total de caracteres | 1.366.663.305 |

**Contagem de palavras-chave:**

| Palavra | Quantidade |
|---------|------------|
| erro    | 33.332.083 |
| warning | 33.330.520 |
| info    | 33.329.065 |

---

## 6. Gráficos

- **Tempo de execução x nº de processos:**  
  ![Tempo de execução](grafico/grafico_tempo.png)

- **Speedup x nº de processos:**  
  ![Speedup](grafico/grafico_speedup.png)

- **Eficiência x nº de processos:**  
  ![Eficiência](grafico/grafico_eficiencia.png)

---

## 7. Análise dos Resultados

- O **tempo de execução diminuiu significativamente** ao aumentar o número de processos, mostrando que a paralelização foi eficiente.  
- O **speedup** aumenta com o número de processos, mas **a eficiência cai** à medida que mais processos são usados, devido ao overhead de paralelização.  
- A consolidação dos resultados de milhares de arquivos foi feita corretamente, sem perda de dados.  
- O desempenho ótimo é atingido entre 8 e 12 processos, já que a sobrecarga de gerenciamento de processos começa a se tornar relevante.

---

## 8. Conclusão

- A paralelização utilizando múltiplos processos reduziu drasticamente o tempo de execução comparado ao serial.  
- A eficiência diminui com o aumento de processos devido a overhead de sincronização e balanceamento de carga.  
- O uso do modelo produtor-consumidor com buffer limitado permitiu processar os arquivos em paralelo de forma segura e eficiente.  
- Para operações CPU-bound em Python, o **multiprocessing** é a forma mais adequada para contornar o GIL e obter verdadeiro paralelismo.

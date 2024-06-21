Title: Introdução a biblioteca Pandas
Date: 2024-04-04 10:20
Modified: 2024-06-10 19:30
Category: Python
Tags: pandas, python, data science, data analysis, programming, análise de dados, ciência de dados
Slug: introducao-pandas
Author: Priscyla Santos
Lang: pt
Status: published
Summary: A biblioteca Pandas é uma das ferramentas mais poderosas e versáteis para análise de dados em Python. Desenvolvida por Wes McKinney  em 2008, 

<style>body {text-align: justify}</style>

A biblioteca Pandas é uma das ferramentas mais poderosas e versáteis para análise de dados em Python. Desenvolvida por Wes McKinney  em 2008, ela se tornou indispensável para cientistas de dados, analistas e pesquisadores devido à sua eficiência em manipular e analisar grandes volumes de dados.

A biblioteca Pandas introduz principalmente duas estruturas de dados ao Python: DataFrame e Series.

Um DataFrame é  uma estrutura de dados bidimensional, basicamente uma tabela com linhas e colunas, semelhante a uma planilha do Excel ou uma tabela de banco de dados SQL. Cada coluna em um DataFrame pode ter tipos de dados variados (por exemplo, float, int, boolean), e o DataFrame é ótimo para representar dados reais, permitindo a manipulação de grandes volumes de informações, limpeza de dados, filtragem, agregação, entre outros.

Uma Series é uma estrutura de dados unidimensional, semelhante a uma coluna de um DataFrame. Você pode pensar em uma Series como uma única coluna de dados, com índices.

Uma das maiores vantagens é a sua capacidade de ler e escrever uma ampla variedade de formatos de arquivo, incluindo CSV (Comma Separated Values), Excel, SQL(Structured Query Language), JSON (JavaScript Object Notation) e outros. Isso facilita enormemente o processo de importação e exportação de dados para análise.

Pandas oferece funcionalidades abrangentes que facilitam diversas operações para análise de da testes e dados de ensaios clínicos.

Ciência de dados: Uma ferramenta fundamental para cientistas de dados que trabalham com Machine Learning, análise de Big Data e outras áreas.



Agora, vou compartilhar com você alguns comandos  que são utilizados para qualquer tarefa de análise de dados. Acesse o projeto [Análise dos dados do Desenrola Brasil](https://www.kaggle.com/code/priscylasantos/an-lise-dos-dados-do-desenrola-brasil) para ver o uso desses comandos na prática:

---
- **read_csv()**: Realiza a leitura de arquivos CSV  e converter esses dados em um DataFrame

- **read_excel()**: Realiza a leitura do arquivo Excel (.xls, .xlsx) em converter esses dados em um DataFrame

---
- **head()**: Exibe as primeiras linhas de um DataFrame.

- **tail()**: Exibe as últimas linhas de um DataFrame.

- **info()**: Fornece informações sobre um DataFrame, como tipo de dados, tamanho, entre outros.

- **describe()**: Apresenta estatísticas descritivas de um DataFrame, como média, mediana, desvio padrão, entre outros.

- **shape**: Fornece a forma (linhas, colunas) de um DataFrame.

- **columns**: Fornece uma lista com os nomes das colunas de um DataFrame.

- **dtypes**: Fornece os tipos de dados de cada coluna de um DataFrame.

---
- **mean()**: Calcula a média de uma coluna de um DataFrame.

- **sum()**: Calcula a soma de uma coluna de um DataFrame.

- **max()**: Fornece o valor máximo de uma coluna de um DataFrame.

- **min()**: Fornece o valor mínimo de uma coluna de um DataFrame.

---
- **isnull().sum()**: Exibe a quantidade de valores nulos em cada coluna de um DataFrame.

- **fillna()**: Substitui valores nulos em um DataFrame com um valor específico.

---
- **sort_values()**: Ordena um DataFrame por uma coluna específica.

- **groupby()**: Agrupa um DataFrame por uma coluna específica e aplica funções agregadas.

---
- **merge()**: Une dois DataFrames em um único DataFrame.

- **to_csv()**: Exporta um DataFrame para um arquivo CSV.

- **to_excel()**: Exporta um DataFrame para um arquivo Excel.

---

**Referências**

[Documentação do Pandas](https://pandas.pydata.org/docs/)

[API do Pandas](https://pandas.pydata.org/docs/reference/index.html)
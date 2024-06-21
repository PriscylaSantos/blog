Title: Um Guia Comparativo de Limpeza de Dados com SQL e Pandas
Date: 2024-06-03 10:20
Modified: 2024-06-05 19:30
Category: Python
Tags: sql, pandas, python, data science, data analysis, programming, análise de dados, ciência de dados
Slug: sql-to-pandas
Author: Priscyla Santos
Lang: pt
Status: published
Summary: No campo da ciência de dados, a limpeza de dados é um passo fundamental que garante a precisão e a qualidade da análise de dados. Seja usando SQL para gerenciamento

<style>body {text-align: justify}</style>


No campo da ciência de dados, a limpeza de dados é um passo fundamental que garante a precisão e a qualidade da análise de dados. Seja usando SQL para gerenciamento de banco de dados ou Pandas para manipulação de dados em Python, entender como limpar seus dados de forma eficaz é crucial. Este guia fornece uma visão comparativa das tarefas comuns de limpeza de dados realizadas em SQL e Pandas, com base no infográfico fornecido.
___
#### 1. **Remover Duplicatas**

- SQL
```sql 
DELETE FROM tabela WHERE id NOT IN (SELECT MIN(id) FROM tabela GROUP BY coluna_duplicada);
```

- Pandas
```python
df.drop_duplicates(subset='coluna_duplicada', keep='first', inplace=True)
```

Remover duplicatas é essencial para evitar análises distorcidas. SQL usa uma subconsulta para identificar e manter a primeira instância de registros duplicados. Em Pandas, `drop_duplicates` alcança o mesmo especificando a coluna e mantendo a primeira ocorrência.

___
#### 2. **Preencher Valores Ausentes com Zero**

- SQL
```sql
UPDATE tabela SET coluna = 0 WHERE coluna IS NULL;
```

- Pandas
```python
df['coluna'].fillna(0, inplace=True)
```

Lidar com dados ausentes é crítico para manter a integridade do seu conjunto de dados. Tanto SQL quanto Pandas oferecem métodos diretos para substituir valores `NULL` por zeros.
___
#### 3. **Padronizar Nomes para Maiúsculas**

- SQL
```sql
UPDATE tabela SET nome = UPPER(nome);
```

- Pandas
```python
df['nome'] = df['nome'].str.upper()
```

A formatação consistente de dados textuais, como converter nomes para maiúsculas, ajuda a manter a uniformidade no conjunto de dados.

___
#### 4. **Remover Espaços em Branco Extras**

- SQL
```sql
UPDATE tabela SET coluna = TRIM(coluna);
```

- Pandas
```python
df['coluna'] = df['coluna'].str.strip()
```

Espaços em branco extras podem levar a imprecisões no processamento de dados. A função `TRIM` do SQL e o método `str.strip` do Pandas servem para eliminar espaços desnecessários.

___
#### 5. **Tratar Outliers - Definir Limite Superior**

- SQL
```sql
UPDATE tabela SET valor = limite_superior WHERE valor > limite_superior;
```

- Pandas
```python
df.loc[df['valor'] > limite_superior, 'valor'] = limite_superior
```

O tratamento de outliers é essencial para uma análise estatística robusta. Tanto SQL quanto Pandas permitem definir um limite para valores que excedem um determinado limite.

___
#### 6. **Converter String para Número (se possível)**

- SQL
```sql
UPDATE tabela SET coluna_numerica = CAST(coluna_texto AS DECIMAL);
```

- Pandas
```python
df['coluna_numerica'] = pd.to_numeric(df['coluna_texto'], errors='coerce')
```

Converter tipos de dados garante compatibilidade com operações analíticas. SQL e Pandas oferecem funções de conversão, com o Pandas fornecendo o parâmetro adicional `errors='coerce'` para lidar com erros de conversão de forma elegante.

___
#### 7. **Formatar Datas no Formato 'YYYY-MM-DD'**

- SQL
```sql
UPDATE tabela SET data = DATE_FORMAT(data, '%Y-%m-%d');
```

- Pandas
```python
df['data'] = pd.to_datetime(df['data']).dt.strftime('%Y-%m-%d')
```

A formatação de datas é essencial para consistência e comparabilidade. Tanto SQL quanto Pandas facilitam essa transformação com suas respectivas funções de formatação.

___
#### 8. **Tratar Valores Extremos (Limitar a um Intervalo)**

- SQL
```sql
UPDATE tabela SET valor = MAX(valor, limite_inferior) WHERE valor < limite_inferior;
```

- Pandas
```python
df.loc[df['valor'] < limite_inferior, 'valor'] = limite_inferior
```

Para garantir que os dados estejam dentro de um intervalo razoável, SQL e Pandas oferecem mecanismos para ajustar valores que estão fora dos limites especificados.

___
#### 9. **Remover Caracteres Especiais (Exceto Alfanuméricos)**

- SQL
```sql
UPDATE tabela SET coluna_texto = REGEXP_REPLACE(coluna_texto, '[^A-Za-z0-9 ]', '');
```

- Pandas
```python
df['coluna_texto'] = df['coluna_texto'].str.replace('[^A-Za-z0-9 ]', '', regex=True)
```

A limpeza de dados textuais, removendo caracteres especiais, ajuda na padronização das entradas e melhora a qualidade dos dados.

___
#### 10. **Excluir Registros com Valores Ausentes**

- SQL
```sql
DELETE FROM tabela WHERE coluna IS NULL;
```

- Pandas
```python
df.dropna(subset=['coluna'], inplace=True)
```

Excluir registros incompletos é, por vezes, necessário para garantir a confiabilidade da análise. Tanto SQL quanto Pandas fornecem métodos para eliminar registros com valores ausentes em colunas especificadas.

---

Dominar técnicas de limpeza de dados tanto em SQL quanto em Pandas te equipa com ferramentas versáteis para manter alta qualidade de dados, essencial para qualquer processo de tomada de decisão baseado em dados. Cada plataforma tem seus pontos fortes, e entender suas funcionalidades aumenta sua eficiência nas tarefas de pré-processamento de dados.
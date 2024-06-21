Title: Comandos Básicos do SQL
Date: 2024-06-01 20:29
Modified: 2024-06-10 19:30
Category: Database
Tags: sql, banco de dados, database
Slug: introducao-sql
Author: Priscyla Santos
Lang: pt
Status: published
Summary: O SQL (Structured Query Language) é uma linguagem padrão utilizada para gerenciar e manipular bancos de dados relacionais. Abaixo, exploramos os principais

<style>body {text-align: justify}</style>


O SQL (Structured Query Language) é uma linguagem padrão utilizada para gerenciar e manipular bancos de dados relacionais. Abaixo, exploramos os principais comandos básicos do SQL, essenciais para a administração e operação de dados em um sistema de gerenciamento de banco de dados.

### 1. **SELECT**

O comando `SELECT` é utilizado para consultar dados de uma ou mais tabelas no banco de dados. Ele permite especificar quais colunas deseja-se visualizar.

```sql
SELECT coluna1, coluna2 FROM nome_da_tabela;
```

Exemplo:

```sql
SELECT nome, idade FROM alunos;
```

### 2. **INSERT**

O comando `INSERT` insere novos registros em uma tabela.

```sql
INSERT INTO nome_da_tabela (coluna1, coluna2) VALUES (valor1, valor2);
```

Exemplo:

```sql
INSERT INTO alunos (nome, idade) VALUES ('João', 20);
```

### 3. **UPDATE**

O comando `UPDATE` é utilizado para modificar registros existentes em uma tabela.

```sql
UPDATE nome_da_tabela SET coluna1 = valor1, coluna2 = valor2 WHERE condição;
```

Exemplo:

```sql
UPDATE alunos SET idade = 21 WHERE nome = 'João';
```

### 4. **DELETE**

O comando `DELETE` remove registros de uma tabela.

```sql
DELETE FROM nome_da_tabela WHERE condição;
```

Exemplo:

```sql
DELETE FROM alunos WHERE nome = 'João';
```

### 5. **CREATE TABLE**

O comando `CREATE TABLE` cria uma nova tabela no banco de dados.

```sql
CREATE TABLE nome_da_tabela (
  coluna1 tipo_de_dado,
  coluna2 tipo_de_dado,
  ...
);
```

Exemplo:

```sql
CREATE TABLE alunos (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  idade INT
);
```

### 6. **DROP TABLE**

O comando `DROP TABLE` exclui uma tabela existente e todos os seus dados.

```sql
DROP TABLE nome_da_tabela;
```

Exemplo:

```sql
DROP TABLE alunos;
```

### 7. **ALTER TABLE**

O comando `ALTER TABLE` modifica a estrutura de uma tabela existente, como adicionar, alterar ou excluir colunas.

```sql
ALTER TABLE nome_da_tabela ADD nova_coluna tipo_de_dado;
ALTER TABLE nome_da_tabela MODIFY coluna_existente novo_tipo_de_dado;
ALTER TABLE nome_da_tabela DROP COLUMN coluna_existente;
```

Exemplo:

```sql
ALTER TABLE alunos ADD email VARCHAR(100);
ALTER TABLE alunos MODIFY idade SMALLINT;
ALTER TABLE alunos DROP COLUMN email;
```

### 8. **JOIN**

O comando `JOIN` combina registros de duas ou mais tabelas com base em uma coluna relacionada entre elas.

```sql
SELECT tabela1.coluna1, tabela2.coluna2 FROM tabela1
JOIN tabela2 ON tabela1.coluna_comum = tabela2.coluna_comum;
```

Exemplo:

```sql
SELECT alunos.nome, cursos.nome_do_curso FROM alunos
JOIN cursos ON alunos.id_curso = cursos.id;
```

## Conclusão

Compreender e saber utilizar os comandos básicos do SQL é fundamental para gerenciar eficientemente um banco de dados relacional. Esses comandos permitem criar, modificar, consultar e excluir dados, oferecendo uma base sólida para operações mais avançadas em SQL.
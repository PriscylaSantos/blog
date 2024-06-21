Title: Comandos básicos do Linux
Date: 2024-02-26 10:20
Modified: 2024-06-10 19:30
Category: Linux
Tags: comandos, linux, terminal
Slug: comandos-basicos
Author: Priscyla Santos
Lang: pt
Status: published
Summary: Este guia apresenta os comandos básicos do Linux para navegação em arquivos, informações do sistema, gerenciamento de arquivos, rede e outros utilitários.

<style>body {text-align: justify}</style>

## Introdução:

Este guia apresenta os comandos básicos do Linux para navegação em arquivos, informações do sistema, gerenciamento de arquivos, rede e outros utilitários.

## Navegação e arquivos:
- `ls`: Lista todos os arquivos e pastas do diretório atual.
- `cd`: Muda para o diretório especificado.
- `pwd`: Mostra o diretório atual.
- `mkdir`: Cria um novo diretório.
- `rmdir`: Remove um diretório vazio.
- `rm`: Remove um arquivo.
- `cp`: Faz cópia de um arquivo.
- `mv`: Move um arquivo ou renomeia-o.
- `touch file`: Cria um novo arquivo vazio "file" ou atualiza a data de modificação de um arquivo existente.
- `cat file`: Mostra o conteúdo de um arquivo.
- `cat >> file`: Concatena a entrada padrão com o conteúdo de um arquivo.
- `tail -f file`: Mostra o conteúdo de um arquivo à medida que ele é modificado.

---
### 1. ls
    
O comando `ls` significa `list` em inglês e é usado para listar arquivos e diretórios. É um dos comandos mais básicos e usados com frequência na linha de comando.


**Função do comando ls:**

* **Listar os nomes de arquivos e diretórios** em um determinado diretório.
* Mostrar informações adicionais sobre os arquivos, como tipo, tamanho, data de modificação e permissões.
* Ordenar os resultados por nome, tamanho, data ou outros critérios.
* Filtrar os resultados por nome, tipo, data ou outros critérios.


**Opções do comando ls:**

O comando ls possui diversas opções que podem ser usadas para personalizar a saída do comando. Algumas das opções mais comuns são:

* **-a:** `all(todos)`. Lista todos os arquivos, incluindo arquivos ocultos.
* **-l:** `long listing format(formato de listagem longa)`. Lista os arquivos e diretórios com detalhes extensivos, incluindo permissões, número de links, proprietário, grupo, tamanho, data de última modificação e nome
* **-r:** `reverse(reverso)`. Ordena os resultados em ordem inversa.
* **-t:** `time(tempo)`. Ordena os arquivos pela data de modificação, com os mais recentes primeiro.
* **-h:** `human-readable(legível para humanos)`. Mostra o tamanho dos arquivos em um formato mais legível.


**Exemplos de uso do comando ls:**

* **Listar o conteúdo do diretório atual:**

```
ls
```

* **Listar o conteúdo do diretório "/home/user":**

```
ls /home/user
```

* **Listar os arquivos com a extensão ".txt":**

```
ls *.txt
```

* **Listar os arquivos em ordem decrescente de tamanho:**

```
ls -lS
```

* **Mostrar informações detalhadas sobre um arquivo:**

```
ls -l arquivo.txt
```


**Para mais informações sobre o comando ls, consulte a página de manual do comando via terminal:**

```
man ls
```


---
### 2. cd

O comando `cd` significa `change directory (mudar diretório)` e é usado para navegar pelos diretórios do sistema operacional. É um dos comandos mais básicos e usados com frequência na linha de comando.


**Função do comando cd:**

* **Mudar o diretório atual** para o diretório especificado.
* **Listar os arquivos e diretórios** do diretório atual.
* **Navegar para um diretório superior** usando o comando "cd ..".


**Opções do comando cd:**

O comando cd possui algumas opções que podem ser usadas para personalizar seu uso. Algumas das opções mais comuns são:

* **-L:** `logical(lógico)`. Se o diretório especificado for um link simbólico, muda para o diretório que o link aponta.
* **-P:** `physical(físico)`. Se o diretório especificado for um link simbólico, muda para o diretório pai do link.
* **-V:** `verbose(detalhado)`. Mostra informações detalhadas sobre o processo de mudança de diretório.


**Exemplos de uso do comando cd:**

* **Mudar para o diretório "/home/usuario":**

```
cd /home/usuario
```

* **Listar o conteúdo do diretório atual:**

```
ls
```

* **Navegar para o diretório superior:**

```
cd ..
```

**Para mais informações sobre o comando cd, consulte a página de manual do comando via terminal:**

```
man cd
```

---
### 3. pwd
    
O comando `pwd` significa `print working directory` e é usado para mostrar o caminho completo do diretório no qual você está trabalhando.


**Função do comando pwd:**

* **Não modifica nada no sistema.** Ele apenas **recupera e mostra o caminho absoluto** do diretório no qual você está navegando.
* **Benefícios:** Saber a localização exata ajuda você a entender sua posição atual na estrutura de diretórios e navegar de forma eficiente usando outros comandos como `cd` (mudar diretório).
* **Uso:** Basta digitar `pwd` no terminal e pressionar Enter. Ele imprimirá o caminho completo do diretório atual na próxima linha.


**Exemplo:**

Se você estiver no diretório `/home/user/documentos`, digitar `pwd` e pressionar Enter mostrará:

```
/home/user/documentos
```

**Pontos adicionais:**

* "pwd" é um **comando autônomo** e não requer argumentos.
* É um comando **frequentemente usado**, especialmente para iniciantes que estão aprendendo a navegar na linha de comando.

**Para mais informações sobre o comando pwd, consulte a página de manual do comando via terminal:**

```
man pwd
```

---
### 5. mkdir
    
O comando `mkdir` significa  `make directory (criar diretório)`. É usado para criar novos diretórios (pastas) no sistema de arquivos.

**Função do comando mkdir:** 
* **Cria um novo diretório:** Você especifica o nome e o local do diretório que deseja criar.
* **Organiza arquivos:** Diretórios ajudam a organizar seus arquivos, agrupando-os por tipo, projeto ou qualquer outra categoria que seja útil para você.
* **Funciona em diferentes locais:** Você pode criar diretórios no diretório atual, em subdiretórios existentes ou em qualquer outro local no sistema de arquivos, desde que tenha permissão para gravar naquele local.

**Exemplo:**
Para criar um diretório chamado "Documentos" no diretório atual, você digitaria:

```
mkdir Documentos
```

**Observações:**

* Você precisa ter permissão de gravação no local onde deseja criar o diretório.
* O nome do diretório deve seguir as regras do sistema de arquivos, como não conter caracteres especiais restritos.
* O comando `mkdir` é um dos comandos básicos e mais usados para gerenciar arquivos e diretórios na linha de comando.

**Para mais informações sobre o comando mkdir, consulte a página de manual do comando via terminal:**

```
man mkdir
```

---
### 6. rmdir
 
O comando `rmdir` significa `remove directory(remover diretório)`. É utilizado para apagar diretórios vazios do sistema de arquivos.

**Função do comando rmdir:**

* **Remove diretórios vazios:** Ele somente pode remover diretórios que não contenham nenhum arquivo ou subdiretório dentro deles.
* **Organiza o sistema de arquivos:** Ao remover diretórios desnecessários, você mantém seu sistema de arquivos organizado e evita o acúmulo de pastas vazias.
* **Funciona em diferentes locais:** Você pode remover diretórios no diretório atual, em subdiretórios existentes ou em qualquer outro local no sistema de arquivos, desde que tenha permissão para gravar naquele local.

**Exemplo:**

Para remover um diretório chamado "Temporários" no diretório atual, você digitaria:

```
rmdir Temporários
```

**Observações importantes:**

* **Nunca use o `rmdir` com a opção para remover diretórios não vazios, pois isso pode levar à perda permanente de dados.**
* Certifique-se sempre de que o diretório esteja realmente vazio antes de tentar removê-lo.
* Você precisa ter permissão de gravação no diretório que deseja remover.
* O nome do diretório deve seguir as regras do sistema de arquivos.

**Recomendação:**

Antes de remover qualquer diretório, é sempre aconselhável verificar se ele está realmente vazio e se você tem certeza de que não precisa mais dele. Se houver arquivos importantes dentro do diretório, é crucial fazer um backup antes de prosseguir com a remoção.

**Para mais informações sobre o comando rmdir, consulte a página de manual do comando via terminal:**

```
man rmdir
```

---
### 7. rm

O comando `rm` significa `remove(remover)`. É usado para apagar arquivos do sistema de arquivos.

**Função do comando rm:**

* **Remove arquivos:** Permite eliminar arquivos específicos do seu sistema.
* **Libera espaço em disco:** Ao remover arquivos desnecessários, você libera espaço de armazenamento no seu computador.
* **Funciona em diferentes locais:** Você pode apagar arquivos no diretório atual, em subdiretórios existentes ou em qualquer outro local no sistema de arquivos, desde que tenha permissão para gravar naquele local.

**Opções do comando rm:**

O comando rm possui algumas opções que podem ser usadas para personalizar seu uso. Algumas das opções mais comuns são:

* **-f:** `force(forçar)`. Remove o arquivo sem pedir confirmação, mesmo se o arquivo estiver protegido contra escrita..
* **-r:** `recursive(recursivo)`. Remove o diretório e todo o seu conteúdo recursivamente


**Exemplos:**

Para remover um arquivo chamado "foto.jpg" no diretório atual, você digitaria:

```
rm foto.jpg
```

Para remover todos os arquivos .txt no diretório atual, você digitaria:

```
rm *.txt
```

**Observações importantes:**

* **Use o comando `rm` com cuidado, pois ele pode apagar arquivos permanentemente.**
* **Sempre faça backup de arquivos importantes antes de removê-los.**
* O comando `rm` não remove diretórios vazios. Utilize o comando `rmdir` para essa finalidade.
* Tenha cuidado ao usar opções como `-r` (remover recursivamente) e `-f` (forçar remoção sem confirmação), pois elas podem levar à perda acidental de dados.

**Para mais informações sobre o comando rm, consulte a página de manual do comando via terminal:**

```
man rm
```

---
### 8. cp


O comando `cp` significa `copy(copia)`. É usado para copiar arquivos de um local para outro no sistema de arquivos.

**Função do comando cp:**

* **Copia arquivos:** Permite duplicar arquivos existentes em diferentes locais do seu computador.
* **Cria backups:** Uma das principais utilidades do `cp` é criar backups de arquivos importantes.
* **Organiza arquivos:** Você pode usar o `cp` para organizar seus arquivos, copiando-os para pastas específicas.

**Como usar o `cp`:**

A sintaxe básica do comando `cp` é:

```
cp [opções] arquivo_origem arquivo_destino
```

* **opções:** São opcionais e permitem especificar comportamentos específicos do comando, como copiar recursivamente dentro de diretórios, preservar permissões e atributos dos arquivos, etc.
* **arquivo_origem:** É o nome do arquivo que você deseja copiar.
* **arquivo_destino:** É o nome e local do arquivo copiado.

**Exemplos:**

Para copiar um arquivo chamado "foto.jpg" para o diretório "Imagens", você digitaria:

```
cp foto.jpg Imagens/
```

Para copiar todos os arquivos .txt do diretório atual para o diretório "Documentos", você digitaria:

```
cp *.txt Documentos/
```

**Observações importantes:**

* O comando `cp` não sobrescreve arquivos existentes por padrão. Se o arquivo de destino já existir, você será questionado se deseja sobrescrevê-lo.
* Use a opção `-f` para forçar a sobrescrição do arquivo de destino.
* Tenha cuidado ao usar opções como `-r` (copiar recursivamente) e `-f` (forçar sobrescrição), pois elas podem levar à perda acidental de dados.

**Recomendação:**

Sempre que possível, utilize o comando `rsync` ao invés de `cp` para copiar arquivos grandes ou diretórios. O `rsync` é mais eficiente e oferece recursos adicionais como sincronização de arquivos e pastas.

**Dicas adicionais:**

* Você pode usar o comando `man cp` para obter mais informações sobre o comando `cp` e suas opções.
* Você pode usar o atalho `Ctrl+C` para cancelar a execução do comando `cp` a qualquer momento.
* Utilize a opção `-v` para ver o progresso da copiação do arquivo.

Espero que esta resposta tenha sido útil! Se você tiver mais perguntas sobre o comando `cp` ou como usá-lo, fique à vontade para perguntar.

**Para mais informações sobre o comando cp, consulte a página de manual do comando via terminal:**

```
man cp
```

---
### 9. mv

**Para mais informações sobre o comando mv, consulte a página de manual do comando via terminal:**

```
man mv
```



## Informações do sistema:

- `date`: Mostra a data e hora atual.
- `uptime`: Mostra o tempo que o sistema está ativo.
- `whoami`: Mostra o nome do usuário atual.
- `w`: Mostra os usuários que estão conectados no momento.
- `cat /proc/cpuinfo`: Mostra informações sobre a CPU.
- `cat /proc/meminfo`: Mostra informações sobre a memória.
- `free`: Mostra a memória livre e usada.
- `du`: Mostra o uso do espaço em disco.
- `df`: Mostra o espaço livre em disco em cada partição.
- `uname -a`: Mostra informações sobre o kernel.

## Gerenciamento de arquivos:

- `tar cf file.tar files`: Cria um arquivo tar "file.tar" com os arquivos especificados.
- `tar xf file.tar`: Extrai o conteúdo do arquivo tar "file.tar" no diretório atual.
- `tar tf file.tar`: Mostra o conteúdo do arquivo tar "file.tar".

## Rede:

- `ping host`: Envia pacotes ping para o host especificado.
- `whois domain`: Mostra informações sobre o domínio especificado.
- `dig domain`: Mostra informações de DNS para o domínio especificado.
- `wget file`: Baixa o arquivo especificado da internet.
- `curl url`: Mostra o conteúdo da página web especificada.
- `ssh user@host`: Conecta-se ao host especificado como o usuário especificado.

## Permissões:

- `chmod octal file`: Altera as permissões do arquivo especificado.

## Outros:

- `ps`: Mostra os processos em execução.
- `ps aux`: Mostra os processos em execução com mais detalhes.
- `kill pid`: Mata o processo com o ID especificado.
- `killall proc`: Mata todos os processos com o nome especificado.
- `grep pattern files`: Procura o padrão especificado nos arquivos especificados.
- `grep -r pattern dir`: Procura o padrão especificado recursivamente no diretório especificado.
- `locate file`: Procura o arquivo especificado no sistema.
- `whereis app`: Mostra os locais possíveis do aplicativo especificado.
- `man command`: Mostra a página de manual do comando especificado.
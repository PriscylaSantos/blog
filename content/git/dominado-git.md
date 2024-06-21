Title: Guia Completo do Git para Desenvolvedores: Dominando o Controle de Versão
Date: 2024-06-10 10:20
Modified: 2024-06-17 19:30
Category: Git
Tags: git, versionamento
Slug: dominando-git
Author: Priscyla Santos
Lang: pt
Status: published
Summary: No mundo do desenvolvimento de software, o Git é uma ferramenta indispensável para controle de versão e colaboração. Como desenvolvedora 

<style>body {text-align: justify}</style>

No mundo do desenvolvimento de software, o Git é uma ferramenta indispensável para controle de versão e colaboração. Como desenvolvedora, utilizo o Git diariamente para gerenciar projetos com eficiência. Este artigo é um guia prático, desmistificando comandos essenciais do Git para desenvolvedores de todos os níveis.

___
## Criando um Repositório

**Do zero - Criar um novo repositório local:**
```bash
$ git init [nome_do_projeto]
```
Para começar um novo projeto, utilize o comando `git init`. Isso cria um novo repositório Git em um diretório vazio. Exemplo:
```bash
$ git init meu_projeto
```
Isso inicializa um repositório vazio no diretório "meu_projeto".

**Baixar de um repositório existente:**
```bash
$ git clone [url_do_repositório]
```
Para obter uma cópia de um projeto já existente, use `git clone` seguido da URL do repositório:
```bash
$ git clone https://github.com/usuario/projeto.git
```
Isso cria uma cópia completa do repositório em seu sistema local.

___
## Observando Seu Repositório

**Listar novos arquivos ou arquivos modificados ainda não comitados:**
```bash
$ git status
```
O comando `git status` é usado para verificar o status do repositório. Ele mostra quais arquivos foram modificados e quais estão prontos para serem comitados.

**Mostrar as mudanças em arquivos que ainda não foram 'stageados':**
```bash
$ git diff
```
Para ver as mudanças realizadas em arquivos antes de prepará-los para o commit, utilize `git diff`. Este comando mostra as diferenças entre seu diretório de trabalho e a área de staging.

**Mostrar as mudanças em arquivos 'stageados':**
```bash
$ git diff --cached
```
Depois de usar `git add`, você pode ver as mudanças preparadas para commit com `git diff --cached`.

**Mostrar todas as mudanças (stageadas e não stageadas):**
```bash
$ git diff HEAD
```
Para visualizar todas as alterações no seu repositório, tanto as preparadas quanto as não preparadas para commit, use `git diff HEAD`.

**Mostrar diferenças entre dois commits:**
```bash
$ git diff commit1 commit2
```
Se precisar comparar dois commits específicos, `git diff commit1 commit2` mostra as diferenças entre eles.

**Listar alterações e autores para um arquivo:**
```bash
$ git blame [arquivo]
```
Quer saber quem fez o quê em um arquivo? `git blame` mostra o autor de cada linha de um arquivo, útil para rastrear mudanças.

**Mostrar as mudanças de um commit para um arquivo específico:**
```bash
$ git show [commit]:[arquivo]
```
Para ver as alterações de um commit específico em um arquivo, use `git show`.

**Mostrar o histórico completo de commits:**
```bash
$ git log
```
O comando `git log` exibe o histórico de commits do repositório, incluindo mensagens de commit, autores e datas.

**Mostrar o histórico de mudanças para um arquivo ou diretório específico, incluindo diffs:**
```bash
$ git log -p [arquivo/diretório]
```
Para um histórico detalhado com diferenças incluídas, use `git log -p`.
___
## Trabalhando com Branches

**Listar todas as branches locais:**
```bash
$ git branch
```
Para ver todas as branches locais do seu repositório, `git branch` lista elas.

**Listar todas as branches, locais e remotas:**
```bash
$ git branch -av
```
Para uma visão completa de todas as branches, locais e remotas, use `git branch -av`.

**Alternar para uma branch e atualizar o diretório de trabalho:**
```bash
$ git checkout [nome_da_branch]
```
Para mudar de branch, use `git checkout` seguido do nome da branch desejada.

**Criar uma nova branch:**
```bash
$ git branch [nova_branch]
```
Crie uma nova branch com `git branch`, útil para iniciar novos recursos ou correções.

**Deletar uma branch:**
```bash
$ git branch -d [branch]
```
Para remover uma branch que não é mais necessária, utilize `git branch -d`.

**Mesclar uma branch em outra:**
```bash
$ git checkout [branch_b]
$ git merge [branch_a]
```
Para mesclar mudanças de uma branch em outra, primeiro faça checkout da branch de destino, depois use `git merge`.

**Taguear o commit atual:**
```bash
$ git tag [nome_da_tag]
```
Para marcar um ponto específico na história do seu repositório, como uma versão lançada, use `git tag`.

___
## Fazendo Mudanças

**Preparar o arquivo para commit:**
```bash
$ git add [arquivo]
```
Para preparar um arquivo para commit, use `git add`.

**Preparar todos os arquivos modificados para commit:**
```bash
$ git add .
```
Para preparar todos os arquivos modificados no diretório atual, utilize `git add .`.

**Comitar todas as alterações 'stageadas' com uma mensagem:**
```bash
$ git commit -m "mensagem do commit"
```
Para salvar suas alterações no histórico de commits, use `git commit` com uma mensagem descritiva.

**Comitar todas as alterações 'tracked' com uma mensagem:**
```bash
$ git commit -am "mensagem do commit"
```
Para preparar e comitar todas as alterações em um único comando, use `git commit -am`.

**Desfazer o 'stage' de um arquivo, mantendo as alterações:**
```bash
$ git reset [arquivo]
```
Se você preparou um arquivo por engano, `git reset` remove-o da área de staging, mantendo as mudanças no diretório de trabalho.

**Reverter tudo para o último commit:**
```bash
$ git reset --hard
```
Para desfazer todas as mudanças e retornar ao estado do último commit, use `git reset --hard`.

___
## Sincronização

**Obter as últimas mudanças da origem (sem mescla):**
```bash
$ git fetch
```
Para atualizar seu repositório local com as mudanças do repositório remoto, use `git fetch`.

**Obter as últimas mudanças da origem e mesclar:**
```bash
$ git pull
```
Para buscar e mesclar as mudanças do repositório remoto em sua branch atual, use `git pull`.

**Obter as últimas mudanças da origem e rebasear:**
```bash
$ git pull --rebase
```
Para buscar as últimas mudanças e rebasear sua branch atual, use `git pull --rebase`.

**Enviar as mudanças locais para a origem:**
```bash
$ git push
```
Para enviar suas mudanças locais para o repositório remoto, use `git push`.

___
## Conclusão

Dominar o Git é essencial para qualquer desenvolvedor. Com este guia, você está equipado para gerenciar seu código de forma eficiente e colaborar melhor com sua equipe. Para mais informações, consulte a documentação oficial do Git ou participe de treinamentos disponíveis no [GitHub Training](https://training.github.com/).

Quando estiver em dúvida, lembre-se de que a ajuda está sempre à mão:
```bash
$ git command --help
```

Vamos melhorar nosso fluxo de trabalho e elevar a qualidade dos nossos projetos com Git! 🚀
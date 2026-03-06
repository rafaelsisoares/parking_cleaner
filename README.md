# Projeto Parking Cleaner 🚗🚦🧹

### Objetivo:
Este projeto tem como objetivo automatizar a limpeza das credenciais que permaneceram abertas no sistema

### Motivação:
Todos os dias, ao final do expediente era necessário limpar as credenciais que ficaram abertas no sistema pois caso não fosse feita tal limpeza, as pessoas que estivessem com as credenciais abertas no sistema poderiam ter problemas ao entrar no pátio, então eu decidi automatizar essa tarefa para economizar tempo e testar meus conhecimentos e habilidades com ferramentas de automação WEB e tecnicas de Web Scraping.


### Tecnologias usadas no projeto:
* Python -> Linguagem de programação.
* Selenium -> Biblioteca usada para fazer a automação
* Dotenv -> Para carregar as variaveis de ambiente
* VS Code -> IDE de desenvolviemto


## Usando o projeto:

**Para que o projeto possa funcionar corretamente siga os passos a seguir:**

1. Verifique se o Python está instalado na sua maquina.
    * Caso não saiba como instalar [clique aqui](https://www.python.org/downloads/)

2. Clone o repositório.
    * **Use esse comando** `git clone git@github.com:rafaelsisoares/parking_cleaner.git`
    * Depois entre no repositório com o comando `cd parking_cleaner`

3. Instale as dependências:
    * **Use esse comando** `pip install -r requirements.txt`

4. Configure as variaveis de ambiente:
    * Renomeie o arquivo `.env.example` para `.env`
    * Abra o arquivo e insira as credenciais de acesso corretamente
    * Obs: As linhas que começam com `#` são comentários e não irão interferir na leitura e carregamento das variaveis de ambiente.

5. Ative o ambiente virtual:
    * **Use esse comando** `source .venv/bin/activate`

6. Por fim execute o script:
    * `python3 app.py`

###### Feito com ❤ por [Rafael Soares](https://rafael-soares.vercel.app/) | Março de 2026
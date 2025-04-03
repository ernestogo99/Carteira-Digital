# Carteira Digital

Este é um projeto backend que tem como objetivo realizar transações financeiras,
como transferências e depósitos.

## Destaques do projeto

- **Operações**:

  - Realizar transferências para outros usuários.
  - Consultar saldo.
  - Depositar dinheiro.

- **Tipos de Usuário**:

  - Lojistas
  - Usuários comuns

- **Restrições**:

  - Somente usuários comuns podem realizar transferências.

- **Criação de Usuário**:

  - O sistema permite a criação de contas, definindo o tipo de usuário.

- **Autenticação**:

  - Implementada com JWT.

- **Histórico de Transações**:

  - Cada usuário pode visualizar sua lista de transações.

- **Segurança nas Transferências**:

  - A transação de transferência é revertida em caso de erro.

- **Documentação**:
  - API documentada com Swagger.

## Tecnologias utilizadas

- Python: Linguagem de programação para o back-end
- DJango Ninja: Framework utilizado para o desenvolvimento de apis

## Como rodar o projeto

1. crie uma virtual env:
   ```sh
   python -m venv venv
   ```
2. inicie o ambiente virtual,Execute o comando abaixo quando estiver na pasta do projeto:

   ```sh
   ./venv/Scripts/Activate
   ```

3. Instale os requisitos:

   ```sh
   pip intall -r requirements.txt
   ```

4. Rode o Projeto:

   ```sh
   python manage.py runserver
   ```

5. Para ver a documentação com o swagger, vá para:
   ```sh
    http://127.0.0.1:8000/api/docs
   ```

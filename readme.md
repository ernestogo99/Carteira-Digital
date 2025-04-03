# Carteira Digital

Este é um projeto backend que tem como objetivo realizar transações financeiras,
como transferências e depósitos.

## Destaques do projeto

- Operações:O usuário pode realizar uma transferência para outro usuário,checar seu saldo e depositar dinheiro.
- Tipos de usuário:Há dois tipos de usuário: Lojistas e usuários
- Restrições:Somente o usuário pode realizar transferência
- Criação de usuário: O sistema permite a criação de usuário, onde é definido seu tipo
- Autenticação com JWT
- Cada usuário pode verificar sua lista de transações
-A transação de transferência é revertida em caso de erro
-Documentação com Swagger

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

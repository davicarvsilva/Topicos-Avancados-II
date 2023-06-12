Use Case ID: UC-001
Name: Registro do usuário
Description: Este caso de uso descreve o registro de um usuário na aplicação.
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa senha e login
2. O sistema verifica se o login está disponível
3. Usuário é salvo nos repositórios

Alternative Scenario A - Login já existe
2a. Caso o login informado pelo usuário não esteja disponível, retornar a mensagem: "login indisponível".


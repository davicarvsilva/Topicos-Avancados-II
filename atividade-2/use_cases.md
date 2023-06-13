Use Case ID: UC-001<br>
Name: Registro do usuário<br>
Description: Este caso de uso descreve o registro de um usuário na aplicação.<br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:<br>
1. Usuário informa senha e login
2. O sistema verifica se o login está disponível
3. Usuário é salvo 

Postconditions: Novo usuário é armazenado<br>

Alternative Scenario A - Login já existe<br>
2. Caso o login informado pelo usuário não esteja disponível, retornar a mensagem: "login indisponível".

Use Case ID: UC-002<br>
Name: Adição de chopeira<br>
Description: Este caso de uso descreve a adição de uma nova chopeira <br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:
1. Usuário informa os dados da chopeira
2. O sistema salva a nova chopeira

Postconditions: Nova chopeira é armazenada

Use Case ID: UC-003<br>
Name: Adição de barril<br>
Description: Este caso de uso descreve a adição de um novo barril<br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:
1. Usuário informa os dados do barril
2. O sistema salva o novo barril

Postconditions: Novo barril é armazenado<br>

Use Case ID: UC-004<br>
Name: Adição de cilindro<br>
Description: Este caso de uso descreve a adição de um novo cilindro<br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:
1. Usuário informa os dados do cilindro
2. O sistema salva o novo cilindro

Postconditions: Novo cilindro é armazenado<br>

Use Case ID: UC-005<br>
Name: Adição de manômetro<br>
Description: Este caso de uso descreve a adição de um novo manômetro<br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:<br>
1. Usuário informa os dados do manômetro
2. O sistema salva o novo manômetro

Postconditions: Novo manômetro é armazenado<br>

Use Case ID: UC-006<br>
Name: Criação de ordem de serviço<br>
Description: Este caso de uso descreve a criação de uma ordem de serviço. Cada ordem de serviço precisa contem ao menos um barril, e pode ou não conter o material para extração (chopeira, cilindro, manometro)
<br>
Actors: Usuário<br>
Preconditions: Nenhuma<br>
Steps:<br>
1. Usuário informa tamanho do barril
2. Usuário informa se haverá necessidade de material para extração
3. Sistema verifica disponibilidade de cilindro, chopeira e manômetro
4. Ordem de serviço é criada

Alternative Scenario A - Não há material para extração disponível<br>
3. Sistema não cria ordem de serviço caso não haja materiais disponíveis

Postconditions: Nova ordem de serviço é armazenada. Chopeira, manômetro e cilindro tem seus status alterados para "ocupado". 



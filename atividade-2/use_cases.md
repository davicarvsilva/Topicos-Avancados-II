Use Case ID: UC-001
Name: Registro do usuário
Description: Este caso de uso descreve o registro de um usuário na aplicação.
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa senha e login
2. O sistema verifica se o login está disponível
3. Usuário é salvo 

Postconditions: Novo usuário é armazenado

Alternative Scenario A - Login já existe
2. Caso o login informado pelo usuário não esteja disponível, retornar a mensagem: "login indisponível".

Use Case ID: UC-002
Name: Adição de chopeira
Description: Este caso de uso descreve a adição de uma nova chopeira 
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa os dados da chopeira
2. O sistema salva a nova chopeira

Postconditions: Nova chopeira é armazenada

Use Case ID: UC-003
Name: Adição de barril
Description: Este caso de uso descreve a adição de um novo barril
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa os dados do barril
2. O sistema salva o novo barril

Postconditions: Novo barril é armazenado

Use Case ID: UC-004
Name: Adição de cilindro
Description: Este caso de uso descreve a adição de um novo cilindro
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa os dados do cilindro
2. O sistema salva o novo cilindro

Postconditions: Novo cilindro é armazenado

Use Case ID: UC-005
Name: Adição de manômetro
Description: Este caso de uso descreve a adição de um novo manômetro
Actors: Usuário
Preconditions: Nenhuma
Steps:
1. Usuário informa os dados do manômetro
2. O sistema salva o novo manômetro

Postconditions: Novo manômetro é armazenado

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

Alternative Scenario A - Não há material para extração disponível
3. Sistema não cria ordem de serviço caso não haja materiais disponíveis

Postconditions: Nova ordem de serviço é armazenada. Chopeira, manômetro e cilindro tem seus status alterados para "ocupado". 



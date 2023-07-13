Funcionalidade: Criação de ordem de serviço
    Como um usuário
    Eu quero criar ordens de serviço
    Para que o sistema armazena os pedidos dos clientes

Cenário: Criação da ordem de serviço foi válida
    Given usuário está cadastrado
    Quando usuário informa os dados para criação de uma ordem de serviço
    And há material disponível para alocação
    Then o sistema deverá criar uma ordem de serviço e armazená-la.

Cenário: Não há material disponível para alocação
    Given usuário está cadastrado
    When usuário informa os dados para criação de uma ordem de serviço
    And não há material disponível para alocação
    Then uma mensagem de erro deve ser mostrada

Funcionalidade: Registro de usuário
    Como um usuário
    Eu quero registrar outros usuários
    Para que estes possam acessar o sistema

Cenário: Criação do usuário foi válida
    Given usuário está cadastrado
    Quando usuário informa os dados do novo usuário
    Then o sistema armazena o novo usuário

Cenário: Login já existe
    Given usuário está cadastrado
    When usuário informa os dados do novo usuário
    And já há um usuário com mesmo login cadastrado
    Then uma mensagem de erro deve ser mostrada

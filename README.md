# Web App de Gestão de Academia

## Arquitetura do Projeto

Nossa aplicação web foi projetada para proporcionar uma experiência intuitiva e eficiente na gestão de academias. A arquitetura da aplicação é composta pelos seguintes componentes:

### Acesso ao Web App

O usuário acessa a aplicação através de um navegador web. A página de boas-vindas apresenta as principais ações disponíveis na aplicação, que são:

- **Membros**
- **Atividades**
- **Personal Trainers (Instrutores)**

### Funcionalidades

Para cada uma dessas áreas, a aplicação oferece módulos específicos que permitem:
- **Consulta:** Visualização dos dados cadastrados.
- **Cadastro:** Inserção de novos dados no banco de dados.
- **Edição:** Atualização de dados existentes, com a possibilidade de salvar as alterações diretamente no banco de dados.

### Tecnologias Utilizadas

A aplicação web é desenvolvida utilizando as seguintes tecnologias:

- **Linguagem de Programação:** Python
- **Framework:** Flask, utilizado para processar a aplicação e gerenciar rotas, controllers e blueprints.
- **Templates:** HTML e CSS, responsáveis pela interface do usuário e estilização das páginas.
- **Banco de Dados:** Interação com o banco de dados via SQL, incluindo operações de consulta, alteração e cadastro.

### Estrutura de Código

- **Módulos Web:** Desenvolvidos em Python, são responsáveis pela lógica da aplicação.
- **Templates HTML e CSS:** Utilizados para a interface do usuário.
- **SQL:** Um único módulo SQL é utilizado para a comunicação entre os controllers e o banco de dados, facilitando as operações de CRUD (Create, Read, Update, Delete).

### Testes

Para garantir a qualidade e a estabilidade da aplicação, foram desenvolvidos testes unitários para os principais módulos.

# Enunciado

**Objetivo:** Desenvolver uma aplicação Python que se conecte com o ChatGPT e
outro LLM (como BERT ou RoBERTa) para gerar resultados factíveis e interessantes,
empregando padrões de projeto adequados.

**Descrição do Projeto:**

**1. Conexão com APIs:** Implemente uma interface que se conecte
simultaneamente com a API do ChatGPT e com a API de outro LLM
escolhido. Utilize o padrão **Factory** para a criação de objetos de conexão
com APIs de forma abstrata e flexível.

**2. Interface de usuário:** Desenvolva uma interface de linha de comando (CLI)
que permita ao usuário enviar perguntas aos modelos. Utilize o padrão
**Command** para encapsular a solicitação como um objeto, permitindo
parametrizar clientes com diferentes solicitações.

**3. Processamento de resposta:** Implemente um sistema que avalie as
respostas dos modelos utilizando o padrão **Strategy** para definir uma
família de algoritmos, encapsulá-los como objetos e torná-los
intercambiáveis. Isso permite a comparação das respostas com base em
diferentes critérios de avaliação.

**4. Apresentação dos resultados:** Apresente as respostas selecionadas ao
usuário com uma explicação baseada nos critérios de escolha. Use o
padrão **Observer** para notificar e atualizar automaticamente o cliente sobre
mudanças na resposta escolhida.

**Critérios de avaliação:**

- **Padrões de projeto:** Implementação adequada dos padrões Factory,
Command, Strategy e Observer.
- **Qualidade do código:** Organização, clareza e documentação.
- **Robustez da aplicação:** Manejo eficaz de erros e exceções.
- **Usabilidade:** Intuitividade e clareza da interface de usuário.

**Entrega e Formato:**

- **Código fonte:** Código-fonte completo em um repositório Git.
- **Documentação:** Um README.md detalhando configuração, execução e
descrição das funcionalidades.
- **Demonstração em vídeo:** Vídeo demonstrativo da aplicação em uso.
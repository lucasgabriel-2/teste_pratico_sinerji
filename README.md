# Teste Prático Sinerji - LLM connector

## Sobre

[Enunciado do projeto](./enunciado.md)

### Participante

| Participante                                                                   |
|-------------------------------------------------------------------------|
| [Lucas Gabriel Sousa Carmargo Paiva](https://github.com/lucasgabriel-2) |

## Configuração do ambiente de desenvolvimento local

### Pré-requisitos

- Python 3.11 ou superior
- `venv` para gerenciamento de ambientes virtuais
- Dependências listadas em `requirements.txt`

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1. **Clone o repositório**

   ```bash
   git clone https://github.com/lucasgabriel-2/teste_pratico_sinerji.git
   cd teste_pratico_sinerji
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv sinerji-env
   source sinerji-env/bin/activate   # No Windows, use `sinerji-env\Scripts\activate`
   ```

3. **Instale as dependências**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt 
   ```

4. **Configure as variáveis de ambiente**

   Crie um arquivo `.env` na raiz do projeto e copie o conteúdo do arquivo `.env.example`, ajustando os valores conforme necessário.
   Caso necessário, consulte a documentação para criar suas API Keys:
   - [Documentação - Google](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br&lang=python)
   - [Documentação - OPENAI](https://platform.openai.com/docs/quickstart)

5. **Execute a aplicação**

   ```bash
   python3 app/main.py
   ```

## Apresentação 

<video src='./assets/gravacao.mp4'></video>

[Arquivo de apresentação](./assets/gravacao.mp4)


## Referências

[1] Design Patterns. Refactoring.guru. Disponível em: <https://refactoring.guru/design-patterns>. Acesso em: 12 ago. 2024.
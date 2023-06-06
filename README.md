# python-chat :speech_balloon:

Este projeto tem como objetivo criar um chat que integre várias inteligências artificiais, proporcionando uma experiência interativa e personalizada para os usuários.

## Objetivos do Projeto :dart:

O objetivo principal deste projeto é desenvolver um chat em Python que utilize diversas inteligências artificiais para responder às perguntas dos usuários. As inteligências artificiais podem variar desde chatbots simples até assistentes virtuais mais avançados. A ideia é criar um ambiente onde os usuários possam se comunicar e receber respostas relevantes com base nas diferentes inteligências artificiais disponíveis.

## Configuração do Ambiente de Desenvolvimento :gear:

Recomenda-se a utilização de um ambiente virtual (venv) para isolar as dependências do projeto e manter uma configuração limpa. Siga os passos abaixo para configurar o ambiente virtual:

1. Certifique-se de ter o Python instalado em sua máquina. Você pode fazer o download em [python.org](https://www.python.org).

2. Abra um terminal e navegue até o diretório raiz do projeto.

3. Crie o ambiente virtual executando o seguinte comando:
    ```bash
    python -m venv env
    ```

4. Ative o ambiente virtual com o comando adequado para o seu sistema operacional:
    - Windows:
        ```bash
        env\Scripts\activate
        ```
    - macOS e Linux:
        ```bash
        source env/bin/activate
        ```

Agora que o ambiente virtual está configurado, você pode prosseguir com a instalação dos pacotes necessários.

## Instalação dos Pacotes :package:

As dependências do projeto estão listadas no arquivo "requirements.txt". Para instalá-las, siga os passos abaixo:

1. Certifique-se de que o ambiente virtual esteja ativado.

2. No terminal, execute o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

Isso instalará todas as dependências necessárias para o projeto.

## Atualização do arquivo requirements.txt :arrow_up:

Caso você inclua novas dependências no projeto, é importante manter o arquivo "requirements.txt" atualizado. Para fazer isso, siga os passos abaixo:

1. Certifique-se de que o ambiente virtual esteja ativado.

2. No terminal, execute o seguinte comando para atualizar o arquivo "requirements.txt":
   ```bash
   pip freeze > requirements.txt
   ```

Isso irá sobrescrever o arquivo "requirements.txt" com as versões mais recentes de todas as dependências instaladas no ambiente virtual. Certifique-se de executar este comando sempre que adicionar ou remover uma dependência do projeto.

Lembre-se de compartilhar o arquivo "requirements.txt" atualizado junto com o código-fonte do projeto para que outros desenvolvedores possam instalar as mesmas dependências e garantir a compatibilidade.

## Utilização :computer:

Para executar o chat, utilize o seguinte comando:
```bash
python view\initial_dialog.py
```
# GitFlow

O GitFlow é um modelo de fluxo de trabalho popular baseado no Git, que define uma estrutura clara para o desenvolvimento colaborativo de software. Ele define um conjunto de regras e convenções para gerenciar as branches e as versões de um projeto.

## Branches :twisted_rightwards_arrows:

O GitFlow define diferentes tipos de branches para organizar o trabalho colaborativo. Aqui estão algumas das principais branches utilizadas:

- **Main**: A branch Main contém o código fonte da versão estável do projeto. Ela é atualizada apenas quando uma nova versão é lançada.

- **Develop**: A branch Develop é a principal branch de desenvolvimento. Ela é usada para integrar as alterações de diferentes branches de feature e preparar a próxima versão estável do projeto.

- **Feature**: As branches de Feature são criadas a partir da branch Develop. Elas são usadas para desenvolver novas funcionalidades ou fazer alterações específicas no código. Cada feature deve ser criada em uma branch separada, facilitando a colaboração e o gerenciamento de alterações. Recomenda-se criar a branch feature a partir de uma issue do GitHub

## Issues :pencil: 

No GitFlow, é recomendado o uso de issues para rastrear ideias, bugs e tarefas do projeto. As issues podem ser abertas e atribuídas a diferentes colaboradores, permitindo um melhor acompanhamento do progresso e da resolução de problemas.

## Pull Requests :arrows_clockwise:

O GitFlow enfatiza o uso de pull requests (PRs) para facilitar a revisão e a integração de código. Após concluir o trabalho em uma branch de feature, um colaborador pode abrir um PR para mesclar as alterações na branch Develop. Isso permite que outros membros da equipe revisem o código, forneçam feedback e garantam a qualidade antes da integração.

Além disso, apenas a branch Develop deve ser mesclada na branch Main. Isso garante que apenas as versões estáveis e revisadas sejam incluídas na branch Main.

# Contribuição :handshake:
Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.

1. Crie uma branch para suas alterações:
    ```bash
    git checkout -b minha-feature
    ```
1. Faça as alterações desejadas e commit-as:
    ```bash
   git commit -m 'Adicionando minha feature'
   ```
1. Faça um push para a branch:
    ```bash
    git push origin minha-feature
    ```
1. Abra um pull request no repositório original
## Licença :memo:
Este projeto está licenciado sob a MIT License.

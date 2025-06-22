# https://dse01.pythonanywhere.com/

# DSE Segurança Eletrônica e Serviços LTDA

Este repositório contém o código-fonte de um site institucional profissional desenvolvido para a DSE Segurança Eletrônica e Serviços LTDA, empresa especializada em segurança eletrônica, serviços elétricos e manutenção predial em Fortaleza, Ceará.

## Visão Geral do Projeto

O objetivo principal deste projeto é fornecer uma plataforma online robusta e elegante para a DSE, apresentando seus serviços de forma clara e acessível, além de facilitar o contato com potenciais clientes.

## Funcionalidades Principais

  * **Páginas Institucionais:** Home, Sobre Nós, Serviços e Contato.
  * **Catálogo de Serviços Detalhado:** Exibição de diversos serviços com descrições completas, integrando imagens e vídeos para uma experiência visual rica.
  * **Formulário de Contato Funcional:** Permite que visitantes enviem mensagens diretamente para a empresa via e-mail (integrado com Flask-Mail).
  * **Pesquisa Interna:** Um mecanismo de busca simples para facilitar a localização de serviços específicos no site.
  * **Design Responsivo:** O layout se adapta perfeitamente a diferentes tamanhos de tela (desktops, tablets e smartphones), garantindo uma excelente experiência de usuário em qualquer dispositivo.
  * **Alternância de Tema:** Opção de alternar entre um tema escuro (padrão, com detalhes dourados) e um tema claro, personalizável pelo usuário.
  * **Botão "Voltar ao Topo":** Facilita a navegação em páginas longas.
  * **Integração com Redes Sociais:** Links diretos para WhatsApp e Instagram da empresa.
  * **Otimização para SEO:** Estrutura HTML semântica, URLs amigáveis e configuração para verificação no Google Search Console.

## Tecnologias Utilizadas

  * **Backend:**
      * **Python:** Linguagem de programação principal.
      * **Flask:** Microframework web para o desenvolvimento do servidor e rotas.
      * **Jinja2:** Motor de templates para renderização dinâmica das páginas HTML.
      * **Flask-Mail:** Extensão para integração com serviços de envio de e-mail (SMTP).
      * **Gunicorn:** Servidor WSGI utilizado para deploy em ambiente de produção.
  * **Frontend:**
      * **HTML5:** Estrutura semântica das páginas.
      * **CSS3:** Estilização e design, com um tema escuro e detalhes dourados.
      * **Bootstrap 5.3:** Framework CSS para agilizar o desenvolvimento responsivo e componentes UI.
      * **JavaScript:** Para interatividade no lado do cliente (ex: alternância de tema, lazy loading).
      * **Font Awesome:** Biblioteca de ícones.

## Deploy

Este site está atualmente hospedado e em funcionamento na plataforma **PythonAnywhere** sob um plano gratuito.

## Como Executar Localmente

Para rodar este projeto em sua máquina local:

1.  **Clone o repositório:**
    ```bash
    git clone git@github.com:RenatoSilva192/DSE_SITE.git
    cd nome_da_sua_pasta_do_projeto
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o aplicativo Flask:**
    ```bash
    flask run
    ```
5.  Acesse `http://127.0.0.1:5000` no seu navegador.

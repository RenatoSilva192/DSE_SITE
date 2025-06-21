# dse_website/app.py
from flask import Flask, render_template, request, jsonify, url_for
from datetime import datetime # Para o ano do copyright
from flask_mail import Mail, Message # Adicionado Mail e Message

app = Flask(__name__)

# --- CONFIGURAÇÕES DO FLASK-MAIL ---
# Você pode colocar estas configurações diretamente aqui ou em um arquivo config.py separado
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Ex: 'smtp.gmail.com' para Gmail, 'smtp-mail.outlook.com' para Outlook
app.config['MAIL_PORT'] = 587 # Porta padrão para TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'dsecontato01@gmail.com' # SEU E-MAIL
app.config['MAIL_PASSWORD'] = 'dsecontato01@2025' # SUA SENHA OU SENHA DE APP
app.config['MAIL_DEFAULT_SENDER'] = 'dsecontato01@gmail.com' # O e-mail que aparecerá como remetente

mail = Mail(app) # Inicializa o Flask-Mail com seu app

# --- FIM DAS CONFIGURAÇÕES FLASK-MAIL ---

# Dados dos serviços (COMPLETO)
SERVICES_DATA = [
    {
        "id": "eletricista-predial-residencial",
        "title": "Eletricista Predial e Residencial",
        "description": "Instalação, manutenção e reparo de sistemas elétricos em edifícios e residências, garantindo segurança e conformidade com as normas técnicas. Inclui desde a instalação de tomadas e interruptores até a montagem de quadros de distribuição e correção de falhas.",
        "image": "image7.webp.jpeg"
    },
    {
        "id": "eletricista-industrial",
        "title": "Eletricista Industrial",
        "description": "Serviços especializados em instalações elétricas de grande porte para indústrias, incluindo montagem de painéis de comando, manutenção de máquinas e equipamentos, e implementação de sistemas de automação industrial, visando eficiência e segurança operacional.",
        "image": None
    },
    {
        "id": "instalacao-de-antenas",
        "title": "Instalação de Antenas",
        "description": "Instalação e direcionamento de antenas para TV digital, parabólicas e sistemas de comunicação, garantindo a melhor qualidade de sinal para residências e empresas.",
        "image": None
    },
    {
        "id": "instalacao-de-alarmes",
        "title": "Instalação de Alarmes",
        "description": "Implementação de sistemas de alarme robustos e personalizados para proteger propriedades contra invasões e acessos não autorizados, com sensores de movimento, abertura e pânico.",
        "image": "image2.webp.jpeg"
    },
    {
        "id": "instalacao-cftv",
        "title": "Instalação de Câmeras de Segurança (CFTV)",
        "description": "Projeto e instalação de sistemas de Circuito Fechado de Televisão (CFTV), permitindo o monitoramento de ambientes internos e externos, com gravação e acesso remoto para maior segurança e controle.",
        "image": "image5.webp.jpeg"
    },
    {
        "id": "instalacao-de-alarmes-residenciais-prediais",
        "title": "Instalação de Alarmes Residenciais e Prediais",
        "description": "Foco na segurança de residências e edifícios, com sistemas de alarme customizados que incluem sensores de portas/janelas, detectores de presença e integração com centrais de monitoramento.",
        "image": None
    },
    {
        "id": "instalacao-de-interfones",
        "title": "Instalação de Interfones",
        "description": "Instalação e manutenção de sistemas de interfonia para condomínios, empresas e residências, facilitando a comunicação e o controle de acesso de visitantes.",
        "image": None
    },
    {
        "id": "automacao-de-portoes",
        "title": "Automação de Portões",
        "description": "Automação de portões residenciais, comerciais e industriais, oferecendo conveniência, segurança e durabilidade, com opções de motores e controles remotos.",
        "image": None
    },
    {
        "id": "projeto-eletrico",
        "title": "Projeto Elétrico",
        "description": "Elaboração de projetos elétricos completos e detalhados para novas construções ou reformas, garantindo que a instalação seja segura, eficiente e em conformidade com as normas da ABNT.",
        "image": None
    },
    {
        "id": "instalacao-de-fio-terra",
        "title": "Instalação de Fio Terra",
        "description": "Implementação de sistemas de aterramento elétrico (fio terra) para proteção de pessoas e equipamentos contra choques elétricos e surtos de energia, essencial para a segurança de qualquer instalação.",
        "image": "image7.webp.jpeg" # Reutiliza imagem
    },
    {
        "id": "alpinismo-industrial-fortaleza",
        "title": "Alpinismo Industrial em Fortaleza",
        "description": "Serviços especializados de acesso por corda para trabalhos em altura em ambientes industriais, como inspeções, manutenção e reparos em estruturas elevadas e de difícil acesso.",
        "video": "altura.mp4",
        "image": "image4.webp.jpeg"
    },
    {
        "id": "pintura-predial-fortaleza",
        "title": "Pintura Predial em Fortaleza",
        "description": "Pintura de fachadas e áreas externas de edifícios, utilizando técnicas de alpinismo industrial quando necessário, garantindo acabamento de alta qualidade e durabilidade.",
        "video": "pintura.mp4",
        "image": "image1.webp.jpeg"
    },
    {
        "id": "manutencao-predial-fortaleza",
        "title": "Manutenção Predial em Fortaleza",
        "description": "Serviços de manutenção preventiva e corretiva para edifícios, incluindo reparos estruturais, hidráulicos, elétricos e de acabamento, visando a conservação e funcionalidade do imóvel.",
        "image": "image1.webp.jpeg" # Pode reutilizar imagens de altura
    },
    {
        "id": "seguranca-eletronica-fortaleza",
        "title": "Segurança Eletrônica em Fortaleza",
        "description": "Soluções integradas de segurança eletrônica para residências, condomínios e empresas, englobando instalação e manutenção de sistemas de alarme, câmeras de CFTV, controle de acesso e cercas elétricas.",
        "images": ["image2.webp.jpeg", "image5.webp.jpeg", "image3.webp.jpeg"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', services=SERVICES_DATA, now=datetime.now())

@app.route('/sobre')
def about():
    return render_template('about.html', now=datetime.now())

@app.route('/servicos')
def services():
    return render_template('services.html', services=SERVICES_DATA, now=datetime.now())

@app.route('/servico/<service_id>')
def service_detail(service_id):
    service = next((s for s in SERVICES_DATA if s["id"] == service_id), None)
    if service:
        return render_template('service_detail.html', service=service, now=datetime.now())
    return "Serviço não encontrado", 404

@app.route('/contato', methods=['GET', 'POST']) # Adicione 'POST' aqui
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone') # Use .get() para campos opcionais
        message_text = request.form['message']

        # Cria a mensagem de e-mail
        msg = Message("Nova Mensagem do Site DSE Segurança",
                      sender=app.config['MAIL_DEFAULT_SENDER'],
                      recipients=['seu_email_de_destino@gmail.com']) # Para onde o e-mail será enviado

        msg.body = f"""
        Você recebeu uma nova mensagem do seu site DSE Segurança:

        Nome: {name}
        E-mail: {email}
        Telefone: {phone if phone else 'Não fornecido'}
        ----------------------------------
        Mensagem:
        {message_text}
        """

        try:
            mail.send(msg)
            flash('Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.', 'success')
            return redirect(url_for('contact')) # Redireciona para evitar reenvio do form
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}") # Para depuração
            flash('Ocorreu um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.', 'error')
            return redirect(url_for('contact')) # Mantém na página de contato

    return render_template('contact.html', now=datetime.now())

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = [s for s in SERVICES_DATA if query in s['title'].lower() or (s['description'] and query in s['description'].lower())]
    return render_template('search_results.html', query=query, results=results, now=datetime.now())



if __name__ == '__main__':
    app.run(debug=True)
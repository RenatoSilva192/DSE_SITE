# dse_website/app.py
from flask import Flask, render_template, request, jsonify, url_for
from datetime import datetime # Para o ano do copyright

app = Flask(__name__)

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

@app.route('/contato')
def contact():
    return render_template('contact.html', now=datetime.now())

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = [s for s in SERVICES_DATA if query in s['title'].lower() or (s['description'] and query in s['description'].lower())]
    return render_template('search_results.html', query=query, results=results, now=datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
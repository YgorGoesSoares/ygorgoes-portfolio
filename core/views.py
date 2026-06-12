from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Contact

CERTIFICATIONS = [
    {'title': 'Análise de Sistemas e Prototipagem Web', 'org': 'FIAP',
     'year': '2022', 'icon': '📐', 'desc_key': 'cert_desc_fiap1',
     'link': '/static/pdf/fiap-05776D64.pdf'},
    {'title': 'Empreendedorismo Digital e Gestão de TI', 'org': 'FIAP',
     'year': '2023', 'icon': '🚀', 'desc_key': 'cert_desc_fiap2',
     'link': '/static/pdf/fiap-335C228A.pdf'},
    {'title': 'Desenvolvimento de Aplicativos Móveis', 'org': 'FIAP',
     'year': '2023', 'icon': '📱', 'desc_key': 'cert_desc_fiap3',
     'link': 'https://www.linkedin.com/in/ygor-goes/details/certifications/0ECABA11/'},
    {'title': 'Análise e Design Web 2.0', 'org': 'FIAP',
     'year': '2022', 'icon': '🎨', 'desc_key': 'cert_desc_fiap4',
     'link': 'https://www.linkedin.com/in/ygor-goes/details/certifications/335C228A/'},
    {'title': 'Formação Django: Aplicações Python', 'org': 'Alura',
     'year': '2025', 'icon': '🐍', 'desc_key': 'cert_desc_django1',
     'link': 'https://cursos.alura.com.br/certificate/4692e524-0c39-4382-94f3-5bc31d2df715'},
    {'title': 'Django: Autenticação OAuth2.0', 'org': 'Alura',
     'year': '2024', 'icon': '🐍', 'desc_key': 'cert_desc_django2',
     'link': 'https://cursos.alura.com.br/certificate/aec89af7-a3fa-48b0-b448-bda9328e6007'},
    {'title': 'Django: CRUD e S3', 'org': 'Alura',
     'year': '2025', 'icon': '🐍', 'desc_key': 'cert_desc_django3',
     'link': 'https://cursos.alura.com.br/certificate/e657acc7-83c9-494a-a675-df6f622948d9'},
    {'title': 'Spring Boot 3: API Rest', 'org': 'Alura',
     'year': '2023', 'icon': '☕', 'desc_key': 'cert_desc_spring',
     'link': 'https://cursos.alura.com.br/certificate/f63b09a9-9905-495b-9db8-53aba49d0496'},
    {'title': 'Java OO e Polimorfismo', 'org': 'Alura',
     'year': '2023', 'icon': '☕', 'desc_key': 'cert_desc_javaoo',
     'link': 'https://cursos.alura.com.br/certificate/064813a0-a6c3-4d5b-9349-84c9c2202061'},
    {'title': 'Certificação Java SE 7 Programmer I', 'org': 'Alura',
     'year': '2023', 'icon': '☕', 'desc_key': 'cert_desc_java7',
     'link': 'https://cursos.alura.com.br/certificate/efda0e01-e809-4736-93be-d93dc8163dbc'},
    {'title': 'Python: Orientação a Objetos', 'org': 'Alura',
     'year': '2024', 'icon': '🐍', 'desc_key': 'cert_desc_python',
     'link': 'https://cursos.alura.com.br/certificate/16bf1363-6797-4f8b-9323-e492c2cc1992'},
    {'title': 'Microsserviços na Prática', 'org': 'Alura',
     'year': '2024', 'icon': '⚙️', 'desc_key': 'cert_desc_ms1',
     'link': 'https://cursos.alura.com.br/certificate/b33bf391-fb81-413d-8653-ab23da347ffd'},
    {'title': 'Microsserviços: Padrões de Projeto', 'org': 'Alura',
     'year': '2024', 'icon': '⚙️', 'desc_key': 'cert_desc_ms2',
     'link': 'https://cursos.alura.com.br/certificate/17cc0de3-1ced-4daa-97de-f8421536f20c'},
    {'title': 'Microsserviços: Conceitos', 'org': 'Alura',
     'year': '2024', 'icon': '⚙️', 'desc_key': 'cert_desc_ms3',
     'link': 'https://cursos.alura.com.br/certificate/14c40e01-cefe-47a7-b316-954aea49d962'},
    {'title': 'SQLite: Instruções SQL', 'org': 'Alura',
     'year': '2025', 'icon': '📊', 'desc_key': 'cert_desc_sql',
     'link': 'https://cursos.alura.com.br/certificate/c6eeee31-cb45-48a7-9ac8-8872e9127823'},
    {'title': 'Pandas: Análise de Dados', 'org': 'Alura',
     'year': '2024', 'icon': '📊', 'desc_key': 'cert_desc_pandas',
     'link': 'https://cursos.alura.com.br/certificate/aa747166-1bac-4407-bfd6-9d56485dad7e'},
    {'title': 'NumPy', 'org': 'Alura',
     'year': '2024', 'icon': '📊', 'desc_key': 'cert_desc_numpy',
     'link': 'https://cursos.alura.com.br/certificate/fe2c036a-3746-41aa-a41d-f4020d891f3b'},
    {'title': 'Python para Data Science', 'org': 'Alura',
     'year': '2024', 'icon': '📊', 'desc_key': 'cert_desc_datascience',
     'link': 'https://cursos.alura.com.br/certificate/38037154-aec9-4c8c-8157-7b732d858e02'},
    {'title': 'HTML, CSS & Flexbox', 'org': 'Alura',
     'year': '2023', 'icon': '🌐', 'desc_key': 'cert_desc_html',
     'link': 'https://cursos.alura.com.br/certificate/e80282c2-7160-4790-a973-592b3817565b'},
    {'title': 'Git e GitHub', 'org': 'Alura',
     'year': '2023', 'icon': '🔀', 'desc_key': 'cert_desc_git',
     'link': 'https://cursos.alura.com.br/certificate/febbc89c-be05-4829-884e-150f288e3ec9'},
    {'title': 'Lógica com JavaScript', 'org': 'Alura',
     'year': '2024', 'icon': '🌐', 'desc_key': 'cert_desc_js',
     'link': 'https://cursos.alura.com.br/certificate/449173af-350c-4ab8-8139-923cd30e570b'},
    {'title': 'Voluntário Telefônica Vivo 2025', 'org': 'Vivo',
     'year': '2025', 'icon': '💜', 'desc_key': 'cert_desc_volunteer',
     'link': '/static/pdf/vivo-voluntario-2026.pdf'},
]

TEXTS = {
    'pt': {
        'nav_about': 'Sobre',
        'nav_projects': 'Projetos',
        'nav_network': 'Redes',
        'nav_certs': 'Certificações',
        'nav_contact': 'Contato',
        'footer': 'Full Stack Developer & Telecom Analyst',
        'hero_badge': 'Analista Telecom Jr & Full Stack @ Vivo (Telefônica)',
        'hero_title': 'Olá, sou',
        'hero_highlight': 'Ygor Goes',
        'hero_sub': 'Construo aplicações web escaláveis e automatizo redes com Django, Python e Java. Atualmente na Engenharia de Redes da Vivo (Telefônica Brasil).',
        'hero_cta_projects': 'Ver projetos',
        'hero_cta_contact': 'Entrar em contato',
        'hero_cta_more': 'Mais sobre mim',
        'about_label': 'Trajetória',
        'about_title': 'Sobre mim',
        'about_sub': 'Do administrativo à engenharia de redes — minha história em tecnologia',
        'about_p1': 'Sou desenvolvedor full stack e analista de telecom na <strong>Engenharia de Redes da Vivo (Telefônica Brasil)</strong>, multinacional do grupo Telefónica Espanha. Atuo com desenvolvimento de portais web, automação de redes e integração de sistemas.',
        'about_p2': 'Trabalho diariamente com <strong>Django, Flask e Python</strong> no back-end, Vue.js no front, e consumo de <strong>pacotes NSO (Cisco)</strong> para configuração de roteadores Cisco, Nokia e Huawei. Também orquestro containers com Docker e Kubernetes.',
        'about_p3': 'Antes da Vivo, fui estagiário no time de Engenharia de Vídeo, desenvolvendo um portal Django + PostgreSQL para gestão de dados de transmissão IPTV, autenticação OAuth2.0, CRUDs e logs administrativos com Auditlog.',
        'about_p4': 'Sou formado em <strong>Análise e Desenvolvimento de Sistemas pela FIAP</strong>, com certificações em Java SE 7, Spring Boot, Django e microsserviços. Tenho inglês avançado para leitura e conversação intermediária.',
        'skills_title': 'Tecnologias & Ferramentas',
        'timeline_title': 'Minha jornada',
        'timeline_2025': 'Promovido a Analista Telecom Jr. Atuação em automação de redes com NSO, portais Django, orquestração Docker/K8s e desenvolvimento full stack na Engenharia de Redes.',
        'timeline_2024': 'Estágio no time de Engenharia de Vídeo. Desenvolvimento de portal Django + PostgreSQL para gestão de dados IPTV, autenticação OAuth2.0, ETL e conformidade de dados.',
        'timeline_2023': 'Conclusão do Tecnólogo em Análise e Desenvolvimento de Sistemas na FIAP. Certificações em Java, Spring Boot e microsserviços. Voluntariado na idwall e BRQ Digital.',
        'timeline_2022': 'Início da faculdade na FIAP. Experiência em atendimento ao cliente na Elo7, desenvolvendo habilidades de comunicação e resolução de problemas.',
        'timeline_2019': 'Primeira experiência profissional como estagiário administrativo na Microlins. Início do contato com o mundo corporativo.',
        'projects_label': 'Portfólio',
        'projects_title': 'Projetos',
        'projects_sub': 'Trabalhos pessoais e acadêmicos que desenvolvi',
        'proj_catalog': 'Sistema de gerenciamento de produtos e categorias com autenticação JWT, autorização por roles, documentação Swagger e testes unitários.',
        'proj_sec': 'Implementação prática de autenticação com Spring Security, JWT, UserDetails e TokenService. Exemplo didático de segurança em APIs REST.',
        'proj_events': 'API para gerenciamento de eventos e cidades com autenticação JWT, regras de acesso ADMIN/CLIENT, Spring Data JPA e testes.',
        'proj_news': 'API REST de notícias com CRUD completo, autenticação JWT, arquitetura MVC, Swagger e persistência MySQL via Hibernate.',
        'net_label': 'Telecom',
        'net_title': 'Automação de Redes',
        'net_sub': 'Experiência em telecomunicações e infraestrutura de rede',
        'net_nso': 'Consumo de pacotes NSO (Network Services Orchestrator) da Cisco para automação de provisionamento e configuração de equipamentos.',
        'net_iptv': 'Recepção via satélite, compressão de vídeo/áudio, multiplexação, criptografia e transmissão IPTV/OTT.',
        'net_routers': 'Configuração e automação de roteadores Cisco, Nokia e Huawei integrados a sistemas web Django.',
        'net_django': 'Portais web Django para gestão de equipamentos de rede, IPs, multicast, logs de alterações e autenticação.',
        'certs_label': 'Credenciais',
        'certs_title': 'Certificações',
        'certs_sub': '22 certificações entre FIAP, Alura e Vivo',
        'cert_concluded': 'Concluído',
        'cert_verify': 'Verificar',
        'cert_flip': 'Clique para detalhes',
        'cert_desc_fiap1': 'Qualificação profissional com foco em análise de sistemas, levantamento de requisitos e prototipagem de interfaces web.',
        'cert_desc_fiap2': 'Formação em empreendedorismo digital, gestão de tecnologia da informação e inovação corporativa.',
        'cert_desc_fiap3': 'Desenvolvimento de aplicativos móveis com conceitos de UI/UX, integração com APIs e boas práticas mobile.',
        'cert_desc_fiap4': 'Design e análise de interfaces web 2.0, usabilidade, arquitetura da informação e experiência do usuário.',
        'cert_desc_spring': 'Criação de APIs REST com Spring Boot 3, Spring MVC, validações e boas práticas de desenvolvimento Java.',
        'cert_desc_javaoo': 'Programação orientada a objetos com Java, encapsulamento, herança, polimorfismo e boas práticas.',
        'cert_desc_java7': 'Preparação para certificação Java SE 7 abordando tipos de dados, operadores, laços, arrays e orientação a objetos.',
        'cert_desc_django1': 'Formação completa em Django: models, views, templates, formulários, autenticação, deploy e boas práticas.',
        'cert_desc_django2': 'Implementação de autenticação OAuth2.0 em Django, integração com provedores externos e segurança.',
        'cert_desc_django3': 'CRUD completo com Django, upload e persistência de arquivos no Amazon S3, boas práticas de armazenamento.',
        'cert_desc_python': 'Orientação a objetos em Python: classes, herança, métodos especiais e consumo de APIs externas.',
        'cert_desc_ms1': 'Implementação prática de microsserviços, comunicação entre serviços, API Gateway e estratégias de deploy.',
        'cert_desc_ms2': 'Padrões de projeto para microsserviços: service discovery, circuit breaker, event-driven e configuração distribuída.',
        'cert_desc_ms3': 'Conceitos fundamentais de arquitetura de microsserviços, vantagens, desafios e casos de uso.',
        'cert_desc_sql': 'Comandos SQL: SELECT, JOIN, subqueries, agregações e boas práticas de consultas em SQLite.',
        'cert_desc_pandas': 'Manipulação e análise de dados com Pandas: DataFrames, limpeza, transformação e visualização.',
        'cert_desc_numpy': 'Computação numérica com NumPy: arrays multidimensionais, operações vetorizadas e álgebra linear.',
        'cert_desc_datascience': 'Fundamentos de Python para Data Science: análise exploratória, funções, estruturas de dados e tratamento de exceções.',
        'cert_desc_html': 'Desenvolvimento web com HTML5, CSS3, Flexbox, design responsivo e estruturação de páginas.',
        'cert_desc_git': 'Controle de versão com Git: repositórios, commits, branches, merge e colaboração no GitHub.',
        'cert_desc_js': 'Lógica de programação com JavaScript: variáveis, funções, loops, arrays e manipulação do DOM.',
        'cert_desc_volunteer': 'Participação no programa de voluntariado da Telefônica Vivo, contribuindo com tecnologia para projetos sociais.',
        'contact_label': 'Contato',
        'contact_title': 'Vamos conversar?',
        'contact_sub': 'Disponível para projetos via UpWork',
        'contact_upwork': '📢 Estou disponível para novos projetos via <strong>UpWork</strong>. Se você precisa de um desenvolvedor Django, automação de redes ou aplicações web completas, entre em contato!',
        'form_name': 'Seu nome',
        'form_email': 'Seu email',
        'form_subject': 'Assunto',
        'form_message': 'Sua mensagem',
        'form_send': 'Enviar mensagem',
        'form_sent_ok': 'Mensagem enviada com sucesso! Entrarei em contato em breve.',
        'client_title': 'Portal do Cliente',
        'client_sub': 'Acompanhe o cronograma e desenvolvimento do seu projeto',
        'client_email': 'Email cadastrado',
        'client_password': 'Senha de acesso',
        'client_button': 'Entrar no portal',
        'client_error': 'Credenciais inválidas. Este portal é apenas para clientes com projeto ativo.',
        'client_footer': 'Esqueceu sua senha? Entre em contato pelo email de cadastro.',
    },
    'en': {
        'nav_about': 'About',
        'nav_projects': 'Projects',
        'nav_network': 'Networks',
        'nav_certs': 'Certifications',
        'nav_contact': 'Contact',
        'footer': 'Full Stack Developer & Telecom Analyst',
        'hero_badge': 'Telecom Jr Analyst & Full Stack @ Vivo (Telefônica)',
        'hero_title': "Hi, I'm",
        'hero_highlight': 'Ygor Goes',
        'hero_sub': 'I build scalable web applications and automate networks with Django, Python and Java. Currently at Network Engineering at Vivo (Telefônica Brasil).',
        'hero_cta_projects': 'View projects',
        'hero_cta_contact': 'Get in touch',
        'hero_cta_more': 'More about me',
        'about_label': 'Journey',
        'about_title': 'About me',
        'about_sub': "From admin to network engineering — my story in tech",
        'about_p1': "I'm a full stack developer and telecom analyst at <strong>Vivo (Telefônica Brasil)</strong>, part of the Telefónica Spain group. I work on web portals, network automation and system integration.",
        'about_p2': 'I work daily with <strong>Django, Flask and Python</strong> on the back-end, Vue.js on the front-end, and consume <strong>NSO packages (Cisco)</strong> for configuring Cisco, Nokia and Huawei routers. I also orchestrate containers with Docker and Kubernetes.',
        'about_p3': "Before Vivo, I was an intern in the Video Engineering team, developing a Django + PostgreSQL portal for IPTV transmission data management, OAuth2.0 authentication, CRUDs and Auditlog.",
        'about_p4': "I hold a degree in <strong>Systems Analysis and Development from FIAP</strong>, with certifications in Java SE 7, Spring Boot, Django and microservices. I have advanced English reading skills and intermediate conversation.",
        'skills_title': 'Technologies & Tools',
        'timeline_title': 'My journey',
        'timeline_2025': 'Promoted to Telecom Jr Analyst. Working on NSO network automation, Django portals, Docker/K8s orchestration and full stack development in Network Engineering.',
        'timeline_2024': 'Internship in Video Engineering team. Developed Django + PostgreSQL portal for IPTV data management, OAuth2.0 authentication, ETL and data compliance.',
        'timeline_2023': 'Graduated in Systems Analysis and Development from FIAP. Certifications in Java, Spring Boot and microservices. Volunteering at idwall and BRQ Digital.',
        'timeline_2022': 'Started college at FIAP. Customer service experience at Elo7, developing communication and problem-solving skills.',
        'timeline_2019': 'First professional experience as administrative intern at Microlins. First contact with the corporate world.',
        'projects_label': 'Portfolio',
        'projects_title': 'Projects',
        'projects_sub': 'Personal and academic work I have developed',
        'proj_catalog': 'Product and category management system with JWT authentication, role-based authorization, Swagger documentation and unit tests.',
        'proj_sec': 'Practical authentication implementation with Spring Security, JWT, UserDetails and TokenService. Educational REST API security example.',
        'proj_events': 'Event and city management API with JWT authentication, ADMIN/CLIENT access rules, Spring Data JPA and tests.',
        'proj_news': 'News REST API with full CRUD, JWT authentication, MVC architecture, Swagger and MySQL persistence via Hibernate.',
        'net_label': 'Telecom',
        'net_title': 'Network Automation',
        'net_sub': 'Telecommunications and network infrastructure experience',
        'net_nso': 'Consumption of Cisco NSO (Network Services Orchestrator) packages for automated provisioning and equipment configuration.',
        'net_iptv': 'Satellite reception, video/audio compression, multiplexing, encryption and IPTV/OTT transmission.',
        'net_routers': 'Configuration and automation of Cisco, Nokia and Huawei routers integrated with Django web systems.',
        'net_django': 'Django web portals for network equipment management, IPs, multicast, change logs and authentication.',
        'certs_label': 'Credentials',
        'certs_title': 'Certifications',
        'certs_sub': '22 certifications from FIAP, Alura and Vivo',
        'cert_concluded': 'Completed',
        'cert_verify': 'Verify',
        'cert_flip': 'Click for details',
        'cert_desc_fiap1': 'Professional qualification in systems analysis, requirements gathering and web prototyping.',
        'cert_desc_fiap2': 'Training in digital entrepreneurship, IT management and corporate innovation.',
        'cert_desc_fiap3': 'Mobile app development with UI/UX concepts, API integration and mobile best practices.',
        'cert_desc_fiap4': 'Web 2.0 interface design and analysis, usability, information architecture and UX.',
        'cert_desc_spring': 'REST API development with Spring Boot 3, Spring MVC, validations and Java best practices.',
        'cert_desc_javaoo': 'Object-oriented programming with Java, encapsulation, inheritance, polymorphism.',
        'cert_desc_java7': 'Java SE 7 certification preparation covering data types, operators, loops, arrays and OOP.',
        'cert_desc_django1': 'Complete Django training: models, views, templates, forms, authentication, deploy.',
        'cert_desc_django2': 'OAuth2.0 authentication implementation in Django, external provider integration.',
        'cert_desc_django3': 'Full CRUD with Django, file upload and persistence on Amazon S3.',
        'cert_desc_python': 'Object-oriented Python: classes, inheritance, special methods and external API consumption.',
        'cert_desc_ms1': 'Practical microservices implementation, service communication, API Gateway and deploy strategies.',
        'cert_desc_ms2': 'Microservices design patterns: service discovery, circuit breaker, event-driven architecture.',
        'cert_desc_ms3': 'Fundamental microservices architecture concepts, advantages, challenges and use cases.',
        'cert_desc_sql': 'SQL commands: SELECT, JOIN, subqueries, aggregations and query best practices in SQLite.',
        'cert_desc_pandas': 'Data manipulation and analysis with Pandas: DataFrames, cleaning, transformation.',
        'cert_desc_numpy': 'Numerical computing with NumPy: multidimensional arrays, vectorized operations.',
        'cert_desc_datascience': 'Python fundamentals for Data Science: exploratory analysis, data structures, exceptions.',
        'cert_desc_html': 'Web development with HTML5, CSS3, Flexbox, responsive design and page structuring.',
        'cert_desc_git': 'Version control with Git: repositories, commits, branches, merge and GitHub collaboration.',
        'cert_desc_js': 'Programming logic with JavaScript: variables, functions, loops, arrays and DOM manipulation.',
        'cert_desc_volunteer': 'Participation in the Telefônica Vivo volunteering program, contributing technology to social projects.',
        'contact_label': 'Contact',
        'contact_title': "Let's talk?",
        'contact_sub': 'Available for projects via UpWork',
        'contact_upwork': '📢 I\'m available for new projects on <strong>UpWork</strong>. If you need a Django developer, network automation or full web applications, get in touch!',
        'form_name': 'Your name',
        'form_email': 'Your email',
        'form_subject': 'Subject',
        'form_message': 'Your message',
        'form_send': 'Send message',
        'form_sent_ok': 'Message sent successfully! I will get back to you soon.',
        'client_title': 'Client Portal',
        'client_sub': 'Track your project schedule and development progress',
        'client_email': 'Registered email',
        'client_password': 'Access password',
        'client_button': 'Access portal',
        'client_error': 'Invalid credentials. This portal is for active clients only.',
        'client_footer': 'Forgot your password? Contact us through your registered email.',
    }
}

def get_lang(request):
    lang = request.GET.get('lang', '')
    if not lang:
        lang = request.session.get('lang', 'pt')
    else:
        request.session['lang'] = lang
    return lang

def home(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    return render(request, 'home.html', {'texts': texts, 'lang': lang})

def sobre(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    return render(request, 'sobre.html', {'texts': texts, 'lang': lang})

def projetos(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    return render(request, 'projetos.html', {'texts': texts, 'lang': lang})

def network(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    return render(request, 'network.html', {'texts': texts, 'lang': lang})

def certificacoes(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    certs_with_desc = [{'desc': texts.get(c['desc_key'], ''), **c} for c in CERTIFICATIONS]
    return render(request, 'certificacoes.html', {'texts': texts, 'lang': lang, 'certs': certs_with_desc})

def contato(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    sent = False
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        sent = True
    return render(request, 'contato.html', {'texts': texts, 'lang': lang, 'sent': sent})

def client_login(request):
    lang = get_lang(request)
    texts = TEXTS.get(lang, TEXTS['pt'])
    error = False
    if request.method == 'POST':
        error = True
    return render(request, 'client_login.html', {'texts': texts, 'lang': lang, 'error': error})

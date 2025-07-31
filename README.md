# Desafio OpenWeather 🌦️
Desafio técnico para integração com a API da OpenWeather.

---

## 📋 Descrição

Este projeto consulta dados meteorológicos da OpenWeather API com base na cidade, estado e país e fornece uma resposta com informações climáticas como temperatura, umidade, vento e outros dados relevantes. 

É possível utilizá-lo como base para aplicações mais robustas com previsão do tempo em tempo real.

---

## 🚀 Funcionalidades

- Consulta de clima atual por cidade
- Suporte a múltiplos idiomas (ex: pt-BR)
- Retorno estruturado com dados meteorológicos essenciais
- Integração com a OpenWeather One Call API 3.0
- Tratamento de erros (ex: cidade inválida, falhas na API)
- Logs de requisição com `structlog`
- Integração com Celery para tarefas assíncronas (ex:
histórico de buscas)
- Uso de cache para otimização de recursos e tempo de resposta

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+
- Django 5.2.4+
- Celery 5.5.3+
- Redis 6.2.0+
- OpenWeather API
- structlog
- Docker

---

## ⚙️ Instalação

### Pré-requisitos

- Docker
- Makefile
- Virtualenv (opcional, mas recomendado)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/Wolfterro/desafio-openweather.git
cd desafio-openweather
```

2. Crie um arquivo `.env` com base no `.env.example` ou use os valores abaixo

```env
DEBUG=true
SECRET_KEY=AI@DvIZLq*rglcVADhoa9PlUp5xleXaT&qtJ3mbthL*43ZSfNes@QtAt3feI5Kbie

# DB Settings
DB_NAME=desafio_openweather_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Redis Settings
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=pWMpRhE2cFLukJq9NOawk944e2CYw6SW

# OpenWeather Settings
OW_API_KEY=<INSIRA SUA API_KEY AQUI>
OW_BASE_URL=https://api.openweathermap.org
```

3. Rode a aplicação usando Docker e Makefile:

```bash
$ make run
```

4. (Opcional) Caso queira ter acesso ao painel de administração, execute o comando abaixo para gerar um superuser:

```bash
$ make createsuperuser
```

5. (Opcional) Caso queira acesso ao shell, use o comando abaixo:

```bash
$ make shell
```

---

## 🧪 Uso

Acesse:

```
http://localhost:8000/swagger
```

ou

```
http://localhost:8000/redoc
```

A documentação da API está disponível no modelo OpenAPI via Swagger e Redoc.

Para acesso ao painel de administração para consulta de logs, acesse:

```
http://localhost:8000/admin
```

Exemplo de output:

```bash
================================================================================ test session starts =================================================================================
platform linux -- Python 3.12.11, pytest-8.4.1, pluggy-1.6.0
django: version: 5.2.4, settings: desafio_openweather.settings (from ini)
rootdir: /code
configfile: pytest.ini
plugins: mock-3.14.1, django-4.11.1
collected 7 items                                                                                                                                                                    

apps/weather/tests/models/test_weather_entry_model.py ..                                                                                                                       [ 28%]
apps/weather/tests/test_weather_api.py ...                                                                                                                                     [ 71%]
apps/weather/tests/test_weather_service.py ..                                                                                                                                  [100%]

================================================================================= 7 passed in 0.56s ==================================================================================
```


---

## ✅ Testes

Para rodar os testes:

```bash
$ make test
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🌐 Links úteis

- [OpenWeather API Docs](https://openweathermap.org/api)
- [Django Documentation](https://docs.djangoproject.com/)
- [Celery Documentation](https://docs.celeryq.dev/)
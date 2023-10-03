# Testes Funcionais com Python, Playwright e Cucumber

Este projeto contém testes funcionais automatizados para o site [blogdoagi.com.br](https://blogdoagi.com.br/). Os testes são escritos em Python, utilizando Playwright e Cucumber.

## Pré-requisitos
- Python 3.11: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Playwright Python: [https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)
- Behave: [https://behave.readthedocs.io/en/stable/install.html](https://behave.readthedocs.io/en/stable/install.html)
- Allure-behave [https://docs.qameta.io/allure/](https://docs.qameta.io/allure/)


## Configuração do Ambiente Virtual
1. Abra o terminal na pasta raiz do projeto.
2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

## Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

## Instale os navegadores necessários:
pip install pytest-playwright

## Instale o Allure para gerar o report
pip install allure-behave

## Executando os Testes
```bash
behave
```

## Estrutura de Diretórios

features/: Contém os arquivos de feature escritos em Cucumber.
pages/: Contém os Page Objects.
steps/: Contém os passos dos cenários Cucumber.
tests/: Contém os testes de unidade Python.
venv/: O ambiente virtual para as dependências do projeto.
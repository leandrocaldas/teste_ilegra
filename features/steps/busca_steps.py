# busca_step.py
from behave import given, when, then
from pages.search_page import SearchPage
from playwright.sync_api import expect

@given('que estou na página inicial "{base_url}"')
def step_open_blog_page(context, base_url):
    """
    Abre a página inicial do site.

    Args:
        context (Context): O contexto do Behave.
        base_url (str): A URL da página inicial.

    Raises:
        AssertionError: Se a página não for carregada corretamente.
    """
    if not hasattr(context, 'page'):
        context.page = context.browser.new_page()
    if context.page.url != base_url:
        context.page.goto(base_url)
    context.search_page = SearchPage(context.page)

@when('eu busco por "{query}"')
def step_fill_search_query(context, query):
    """
    Preenche a barra de pesquisa com o termo especificado e clica no botão de busca.

    Args:
        context (Context): O contexto do Behave.
        query (str): O termo de pesquisa.
    """
    context.search_page.perform_search(query)

@then('aparece escrito "{query}" em Resultados da busca por:')
def step_verify_search_results(context, query):
    """
    Verifica se o termo de pesquisa aparece no cabeçalho de resultados.

    Args:
        context (Context): O contexto do Behave.
        query (str): O termo de pesquisa.

    Raises:
        AssertionError: Se o termo não for encontrado no cabeçalho.
    """
    search_header = context.search_page.get_header()
    expect(search_header).to_contain_text(query)

@then('aparece escrito "{query}" no header:')
def step_verify_search_results_not_found(context, query):
    """
    Verifica se o termo de pesquisa aparece no cabeçalho de resultados não encontrados.

    Args:
        context (Context): O contexto do Behave.
        query (str): O termo de pesquisa.

    Raises:
        AssertionError: Se o termo não for encontrado no cabeçalho de resultados não encontrados.
    """
    header_not_found = context.search_page.get_header_not_found()
    expect(header_not_found).to_contain_text(query)

@then('eu encontro "{query}" no titulo, no sub-titulo ou na noticia')
def step_verify_query_find(context, query, max_check=5):
    """
    Verifica se o termo de pesquisa aparece no título, no subtítulo ou no texto da notícia.

    Args:
        context (Context): O contexto do Behave.
        query (str): O termo de pesquisa.
        max_check (int): O número máximo de títulos a serem verificados.
    """
    titles, sub_titles = context.search_page.get_title_and_subtitle()
    if titles.count() > max_check:
        titles_count = max_check
    else:
        titles_count = titles.count()

    # Verificar título e subtítulo
    for i in range(titles_count):
        title_text = titles.nth(i).inner_text().lower()
        sub_title_text = sub_titles.nth(i).inner_text().lower()
        if query.lower() in title_text or query.lower() in sub_title_text:
            continue  # Se encontrado, não precisa verificar o texto da notícia
        else: 
            entry_text = context.search_page.get_news_content(i)
            context.page.go_back()
            if query.lower() in entry_text:
                continue  # Se encontrado, esta ok
            else:
                # Se não encontrado em nenhum lugar, gerar uma exceção
                assert False, f"Não encontrado {query} nem no título, no sumário ou no texto da notícia"

@then('aparece a mensagem: "{not_found_msg}"')
def step_serach_not_found(context, not_found_msg):
    """
    Verifica se a mensagem de não encontrado é exibida corretamente.

    Args:
        context (Context): O contexto do Behave.
        not_found_msg (str): A mensagem de não encontrado.

    Raises:
        AssertionError: Se a mensagem não for encontrada.
    """
    result_not_found = context.search_page.get_result_not_found()
    assert not_found_msg in result_not_found, "O texto de item não encontrado não confere"

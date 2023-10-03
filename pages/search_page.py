from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.news_page import NewsPage

class SearchPage(BasePage):
    """Página de pesquisa do site."""

    MAGNIFIER_BUTTON = "#search-open"
    SEARCH_INPUT = "Pesquisar por:"
    SEARCH_BUTTON = "Pesquisar"
    RESULT_SEARCH_HEADER = '//*[@id="primary"]/header/h1/span'
    RESULT_SEARCH_TITLE = '.entry-title'
    RESULT_SEARCH_SUMMARY = '.entry-summary'
    RESULT_NOT_FOUND = '//*[@class="entry-content"]/p'

    def __init__(self, page: Page):
        """
        Inicializa a página de pesquisa.

        Args:
            page (Page): A instância da página do Playwright.
        """
        super().__init__(page)
        self.magnifier_button = page.locator(self.MAGNIFIER_BUTTON)
        self.search_input = page.get_by_role("searchbox", name=self.SEARCH_INPUT)
        self.search_button = page.get_by_role("button", name=self.SEARCH_BUTTON, exact=True)
        self.result_search_header = page.locator(self.RESULT_SEARCH_HEADER)
        self.result_search_title = page.locator(self.RESULT_SEARCH_TITLE)
        self.result_search_summary = page.locator(self.RESULT_SEARCH_SUMMARY)
        self.result_not_found = page.locator(self.RESULT_NOT_FOUND)

    def perform_search(self, query):
        """
        Realiza uma pesquisa no site.

        Args:
            query (str): O termo de pesquisa.
        """
        self.magnifier_button.click()
        self.search_input.fill(query)
        self.search_button.click()
    
    def get_header(self):
        """Obtém o cabeçalho da pesquisa."""
        return self.result_search_header
    
    def get_header_not_found(self):
        """Obtém o cabeçalho de resultado não encontrado."""
        return self.result_search_title
    
    def get_title_and_subtitle(self):
        """Obtém o título e o subtítulo dos resultados."""
        return self.result_search_title, self.result_search_summary
    
    def get_news_content(self, title_index):
        """
        Obtém o conteúdo da notícia.

        Args:
            title_index (int): O índice do título da notícia a ser acessada.

        Returns:
            str: O conteúdo da notícia.
        """
        self.result_search_title.nth(title_index).click()
        return NewsPage(self.page).get_news_entry_content()
    
    def get_result_not_found(self):
        """Obtém a mensagem de resultado não encontrado."""
        return self.result_not_found.text_content()
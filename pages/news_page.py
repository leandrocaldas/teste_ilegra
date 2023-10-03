from playwright.sync_api import Page
from pages.base_page import BasePage

class NewsPage(BasePage):
    """Página de notícias do site."""

    NEWS_ENTRY_CONTENT = '//*[@id="entry-content"]'

    def __init__(self, page: Page):
        """
        Inicializa a página de notícias.

        Args:
            page (Page): A instância da página do Playwright.
        """
        super().__init__(page)
        self.news_entry_content = page.locator(self.NEWS_ENTRY_CONTENT)
    
    def get_news_entry_content(self):
        """
        Obtém o conteúdo da entrada de notícias.

        Returns:
            str: O conteúdo da entrada de notícias.
        """
        return self.news_entry_content.text_content().lower()

        
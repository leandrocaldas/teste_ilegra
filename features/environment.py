import subprocess
from playwright.sync_api import sync_playwright

def before_all(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_all(context):
    if hasattr(context, 'browser'):
        context.page.close()
    subprocess.run("allure generate reports -o allure_results", shell=True)
    subprocess.run("allure open allure_results", shell=True)

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.new_page()
    page.goto('https://web.whatsapp.com/send?phone=5538991801928')
    page.locator('xpath=/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]').click()
    page.fill('xpath=/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]', 'Teste 2')
    # page.locator('xpath=/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    browser.close()
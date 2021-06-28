from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://127.0.0.1:8020/OpenLex/default/index
    page.goto("http://127.0.0.1:8020/OpenLex/default/index")

    # Click text=Log In
    page.click("text=Log In")

    # Click text=Registrarse
    page.click("text=Registrarse")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/default/user/register?_next=/OpenLex/default/index"


    # Click input[name="first_name"]
    page.click("input[name=\"first_name\"]")

    # Fill input[name="first_name"]
    page.fill("input[name=\"first_name\"]", "Juan")

    # Click input[name="last_name"]
    page.click("input[name=\"last_name\"]")

    # Fill input[name="last_name"]
    page.fill("input[name=\"last_name\"]", "Perez")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "example@example.com")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "openlex1234")

    # Click input[name="password_two"]
    page.click("input[name=\"password_two\"]")

    # Fill input[name="password_two"]
    page.fill("input[name=\"password_two\"]", "openlex1234")

    # Click input:has-text("Registrarse")
    page.click("input:has-text(\"Registrarse\")")
    # assert page.url == "http://127.0.0.1:8020/OpenLex/dashboard/view#"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
from playwright.sync_api import sync_playwright, Playwright, ViewportSize
import os
def start():
    global page, browser, playwright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch_persistent_context(os.getcwd() + '\\playwright_data',headless=False)
    page = browser.pages[0]

def login():
    browser.clear_cookies()
    page.goto("https://www.reddit.com/login", timeout=0)
    # page.set_viewport_size(ViewportSize(width=1920, height=1080))
    page.wait_for_load_state()
    page.wait_for_timeout(5000)
    settings = {
        "reddit": 
        {
            "creds": 
            {
                "username": "",
                "password": ""
            }
        }
    }

    page.wait_for_selector("input#login-username")
    page.locator("input#login-username").fill(
        settings["reddit"]["creds"]["username"]
    )

    page.wait_for_selector("input#login-password")
    page.locator("input#login-password").fill(
        settings["reddit"]["creds"]["password"]
    )


    login_button_selector = "button.login:has-text('Log In')"
    page.wait_for_selector(login_button_selector)
    page.click(login_button_selector)
    page.wait_for_timeout(5000)
    
def run():
    post_url = 'https://www.reddit.com/r/RajasthanRoyals/comments/1bsw7nc/rajasthan_royals_headtohead_record_against_mumbai/'
    page.goto(post_url)
    page.wait_for_selector("xpath=/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/div[1]/div/main/shreddit-async-loader/comment-body-header/shreddit-async-loader[2]/comment-composer-host/faceplate-tracker[1]/button")
    page.locator("xpath=/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/div[1]/div/main/shreddit-async-loader/comment-body-header/shreddit-async-loader[2]/comment-composer-host/faceplate-tracker[1]/button").click()#.fill("Hello World")
    page.wait_for_timeout(5000)
    page.locator("xpath =/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/div[1]/div/main/shreddit-async-loader/comment-body-header/shreddit-async-loader[2]/comment-composer-host/faceplate-form/shreddit-composer/div").fill("Hello World")
    page.wait_for_timeout(3000)
    page.locator("xpath=/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/div[1]/div/main/shreddit-async-loader/comment-body-header/shreddit-async-loader[2]/comment-composer-host/faceplate-form/shreddit-composer/button[2]/span/span/span/span[1]").click()
    page.wait_for_timeout(3000)

start()
login()
run()
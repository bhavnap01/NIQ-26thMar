from playwright.sync_api import sync_playwright

#launch a browser and create a new page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)  #or p.firefox.launch()  or p.webkit.launch()
    page = browser.new_page()
    
    page.goto("https://demoselsite.azurewebsites.net/webform5.aspx")
    
    #access frame by name
    iframe = page.frame(name="iframe_a")  #or page.frame_locator(name="iframe_a")
    
    iframe.fill("#txtName", "Bhavna Pal")
    iframe.click("#btnSubmit")
    result = iframe.locator("#lblMessage")
    print(result.text_content())  #get the text content of the result label
    
    #capture a screenshot of the page
    page.screenshot(path="page_screenshot.png",full_page=True)
    
    #element screenshot
    page.locator("#form1 > div:nth-child(3) > a").screenshot(path="element_screenshot.png")
    
    #close the browser
    browser.close()
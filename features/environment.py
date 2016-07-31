from selenium import webdriver

def before_all(context):
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['version'] = 'latest'
    desired_capabilities['platform'] = 'WINDOWS'
    desired_capabilities['name'] = 'Testing Selenium with Behave'
    desired_capabilities['client_key'] = 'key'
    desired_capabilities['client_secret'] = 'secret'

    context.browser = webdriver.PhantomJS()

def after_all(context):
    context.browser.quit()

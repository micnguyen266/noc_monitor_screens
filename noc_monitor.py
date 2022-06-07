# noc_local_config.py file handles all credentials locally (also in .gitignore)
# config_template.py is a template for passing credentials

# from selenium.webdriver.common.keys import Keys
import noc_local_config
import time
import autoit
from selenium import webdriver
import os
# import tryagain


# Kills all existing Chrome Browsers and VLC players
# Windows
def kill_all():
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im chromedriver.exe /f")
    os.system("taskkill /im vlc.exe /f")


# MacOS
# os.system("killall -9 'Google Chrome'")
# os.system("killall -9 'VLC'")

# Point the path where you saved the ChromeDriver
# Windows
chromedriver = executable_path = r'C:\Users\nocteam8\PycharmProjects\noc_monitor\chromedriver.exe'
# chromedriver = executable_path = r'C:\Users\Michael Nguyen\PycharmProjects\testlab\chromedriver.exe'

# MacOS
# chromedriver = "/Users/micnguyen/PycharmProjects/noc_monitor/chromedriver"
options = webdriver.ChromeOptions()

# This removes the "Chrome is being controlled by automated test software" notification on the browser
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# This disables Chrome's "Save Password" popup
options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})

# Additional arguments
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--content-shell-hide-toolbar")

# Opens Windows in App Mode. Disables Address Bar and Chrome Buttons
options.add_argument("--app=http://www.google.com")


#######################################################################
# Monitors will start opening from the top left corner then clockwise #
#######################################################################


# Monitor 1: Metricly - [NOC][Venue][ELB][Ext/Int - Site] - login
def monitor1():
    driver1.get('https://app.metricly.com/#/dashboards/d4600fd0-bf0d-40f5-aaa0-5bddab9b4cb0')
    time.sleep(2)
    print("Attempting to sign into Monitor 1")
    emailElem = driver1.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver1.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver1.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver1.implicitly_wait(5)
    dashBoardSettings = driver1.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver1.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver1.implicitly_wait(5)
    if driver1.find_elements_by_xpath('//*[@title="[NOC][Venue][ELB][Ext/Int - Site] - login "]'):
        var = {
            print("Monitor 1 Loaded Successfully")
        }
    else:
        monitor1_loop()
    driver1.set_window_size(1550, 899)
    driver1.set_window_position(-7, -29)
    driver1.execute_script("document.body.style.zoom='77%'")


# Will Try Total of 3 times for Monitor 1
def monitor1_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor1()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 1 Did Not Load Successfully")
        break


# Monitor 2a/b/c/d: 4 smaller screens into 1 screen
# Monitor 2a: Cable (00-0)
def monitor2a():
    time.sleep(2)
    print("Opening Monitor 2a")

    def vlc1():
        autoit.run(
            'C:/Program Files/VideoLAN/VLC/vlc.exe dshow:// :dshow-vdev="Video (00-0 Pro Capture Dual HDMI)" :dshow-adev="Audio (00-0 Pro Capture Dual HDMI)" --aspect-ratio 16:9 --volume=0')
        time.sleep(2)
        autoit.send("^h")
        time.sleep(2)
        autoit.win_move("", 1530, -29, 779, 467)

    vlc1()


# Monitor 2b: Youtube
# def monitor2b():
#     driver2b.get('https://www.youtube.com/watch?v=nE_XAauwu1I&t')
#     time.sleep(2)
#     print("Opening Monitor 2b")
#     time.sleep(2)
#     driver2b.implicitly_wait(5)
#     autoit.send("t")
#     time.sleep(10)
#     skipAd = driver2b.find_element_by_xpath('//span[@class="ytp-ad-skip-button-icon"]')
#     if skipAd.is_displayed():
#         var = {
#             skipAd.click()
#         }
#     else:
#         var = {
#             print("No Skip Ad")
#         }
#     driver2b.implicitly_wait(5)
#     time.sleep(10)
#
#     def skipTrail_main():
#         while True:
#             try:
#                 if skipTrial.is_displayed():
#                     skipTrial = driver2b.find_element_by_xpath(
#                         '/html/body/ytd-app/ytd-popup-container/paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string')
#                     skipTrial.click()
#                     break
#             except:
#                 print("No Skip Trial")
#                 break
#             else:
#                 continue
#
#     skipTrail_main()
#     driver2b.implicitly_wait(5)
#     if driver2b.find_elements_by_xpath('//a[@href="/channel/UCZNk2huvU7zJhi0gQJ1xZMQ"]'):
#         var = {
#             print("Monitor 2b Loaded Successfully")
#         }
#     else:
#         monitor2b_loop()
#     driver2b.set_window_size(779, 467)
#     driver2b.set_window_position(2297, -29)

# Monitor 2b: Windy Weather Map
def monitor2b():
    driver2b.get('https://www.windy.com/-Rain-thunder-rain?rain,15.066,-26.982,3')
    time.sleep(2)
    print("Opening Monitor 2b")
    time.sleep(2)
    driver2b.implicitly_wait(5)
    if driver2b.find_element_by_id("login"):
        var = {
            print("Monitor 2b Loaded Successfully")
        }
    else:
        monitor2b_loop()
    driver2b.set_window_size(779, 467)
    driver2b.set_window_position(2297, -29)
    driver2b.execute_script("document.body.style.zoom='100%'")


# Will Try Total of 3 times for Monitor 2b
def monitor2b_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor2b()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 2b Did Not Load Successfully")
        break


# Monitor 2c: Metricly Region Hot Map
def monitor2c():
    driver2c.get('https://app.metricly.com/#/dashboards/615adfa5-ed4c-4f2e-8b32-f94147479686')
    time.sleep(2)
    print("Attempting to sign into Monitor 2c")
    emailElem = driver2c.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver2c.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver2c.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver2c.implicitly_wait(5)
    dashBoardSettings = driver2c.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver2c.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver2c.implicitly_wait(5)
    if driver2c.find_elements_by_xpath('//*[@title="Region Heat Map"]'):
        var = {
            print("Monitor 2c Loaded Successfully")
        }
    else:
        monitor2c_loop()
    driver2c.set_window_size(779, 467)
    driver2c.set_window_position(1530, 403)
    driver2c.execute_script("document.body.style.zoom='100%'")


# Will Try Total of 3 times for Monitor 2c
def monitor2c_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor2c()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 2c Did Not Load Successfully")
        break


# Monitor 2d: Cable (00-1)
def monitor2d():
    time.sleep(2)
    print("Opening Monitor 2d")

    def vlc2():
        autoit.run(
            'C:/Program Files/VideoLAN/VLC/vlc.exe dshow:// :dshow-vdev="Video (00-1 Pro Capture Dual HDMI)" :dshow-adev="Audio (00-1 Pro Capture Dual HDMI)" --aspect-ratio 16:9 --volume=0')
        time.sleep(2)
        autoit.send("^h")
        time.sleep(2)
        autoit.win_move("", 2297, 402, 781, 468)

    vlc2()


# Monitor 3: NOC Slack Account for OpsGenie
# def monitor3():
#     driver3.get('https://yourcompany.slack.com')
#     time.sleep(2)
#     print("Attempting to sign into Monitor 3")
#     oktaElem = driver3.find_element_by_id('index_saml_sign_in_with_saml')
#     oktaElem.click()
#     driver3.implicitly_wait(10)
#     emailElem = driver3.find_element_by_id('okta-signin-username')
#     emailElem.send_keys(noc_local_config.slack_username)
#     pElem = driver3.find_element_by_id('okta-signin-password')
#     pElem.send_keys(noc_local_config.slack_password)
#     signInElem = driver3.find_element_by_id('okta-signin-submit')
#     signInElem.click()
#     print("Please accept DUO push notification...")
#     time.sleep(5)
#     driver3.implicitly_wait(5)
#     jumpToElem = driver3.find_element_by_class_name('p-channel_sidebar__jumper_keys')
#     jumpToElem.click()
#     searchBar = driver3.find_element_by_id('undefined')
#     searchBar.send_keys('alerts-opsgenielog')
#     driver3.implicitly_wait(5)
#     time.sleep(1)
#     # Simulates "Enter" Key
#     searchBar.send_keys(Keys.ENTER)
#     time.sleep(5)
#     driver3.implicitly_wait(5)
#     if driver3.find_elements_by_xpath('//*[text()="alerts-opsgenielog"]'):
#         var = {
#             print("Monitor 3 Loaded Successfully")
#         }
#     else:
#           monitor3_loop()
#     driver3.set_window_size(1549, 899)
#     driver3.set_window_position(3065, -29)

# # Will Try Total of 3 times for Monitor 3
# def monitor3_loop():
#     for i in range(3):
#         for attempt in range(3):
#             try:
#                 monitor3()
#             except:
#                 print("Trying again...")
#             else:
#                 break
#         else:
#             print("Check failed...Monitor 3 Did Not Load Successfully")
#         break

# Monitor 4: AlertSite Dashboard
def monitor4():
    driver4.get(
        'https://yourmonitoringsite.com')
    time.sleep(2)
    print("Attempting to sign into Monitor 4")
    emailElem = driver4.find_element_by_id('id_email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver4.find_element_by_id('id_password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver4.find_element_by_xpath("//input[@type='submit' and @value='Sign In']")
    signInElem.click()
    time.sleep(2)
    driver4.implicitly_wait(5)
    if driver4.find_elements_by_xpath('//a[@href="#/app/2/monitor/dashboard/as-dashboard"]'):
        var = {
            print("Monitor 4 Loaded Successfully")
        }
    else:
        monitor4_loop()
    driver4.set_window_size(1565, 899)
    driver4.set_window_position(4600, -29)


# Will Try Total of 3 times for Monitor 4
def monitor4_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor4()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 4 Did Not Load Successfully")
        break


# Monitor 5: Metricly - [NOC][ELB][Ext/Int - Site] - update
def monitor5():
    driver5.get('https://app.metricly.com/#/dashboards/')
    time.sleep(2)
    print("Attempting to sign into Monitor 5")
    emailElem = driver5.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver5.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver5.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver5.implicitly_wait(5)
    dashBoardSettings = driver5.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver5.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver5.implicitly_wait(5)
    if driver5.find_elements_by_xpath('//*[@title="[NOC][ELB][Ext/Int - Site] - update"]'):
        var = {
            print("Monitor 5 Loaded Successfully")
        }
    else:
        monitor5_loop()
    driver5.set_window_size(1550, 900)
    driver5.set_window_position(-7, 835)
    driver5.execute_script("document.body.style.zoom='77%'")


# Will Try Total of 3 times for Monitor 5
def monitor5_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor5()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 5 Did Not Load Successfully")
        break


# Monitor 6: Metricly - [NOC][RabbitMQ] Dashboard
def monitor6():
    driver6.get('https://app.metricly.com/#/dashboards/')
    time.sleep(2)
    print("Attempting to sign into Monitor 6")
    emailElem = driver6.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver6.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver6.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver6.implicitly_wait(5)
    dashBoardSettings = driver6.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver6.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver6.implicitly_wait(5)
    if driver6.find_elements_by_xpath('//*[@title="[NOC][RabbitMQ] Dashboard"]'):
        var = {
            print("Monitor 6 Loaded Successfully")
        }
    else:
        monitor6_loop()
    driver6.set_window_size(1548, 899)
    driver6.set_window_position(1530, 835)
    driver6.execute_script("document.body.style.zoom='85%'")


# Will Try Total of 3 times for Monitor 6
def monitor6_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor6()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 6 Did Not Load Successfully")
        break


# Monitor 7: Metricly - [NOC][ELB][Int - API]
def monitor7():
    driver7.get('https://app.metricly.com/#/dashboards/')
    time.sleep(2)
    print("Attempting to sign into Monitor 7")
    emailElem = driver7.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver7.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver7.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver7.implicitly_wait(5)
    dashBoardSettings = driver7.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver7.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver7.implicitly_wait(5)
    if driver7.find_elements_by_xpath('//*[@title="[NOC][Venue][ELB][Int - API]"]'):
        var = {
            print("Monitor 7 Loaded Successfully")
        }
    else:
        monitor7_loop()
    driver7.set_window_size(1549, 900)
    driver7.set_window_position(3065, 835)
    driver7.execute_script("document.body.style.zoom='77%'")


# Will Try Total of 3 times for Monitor 7
def monitor7_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor7()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 7 Did Not Load Successfully")
        break


# Monitor 8: Metricly - [NOC][ELB][Ext/Int - Site]
def monitor8():
    driver8.get('https://app.metricly.com/#/dashboards/')
    time.sleep(2)
    print("Attempting to sign into Monitor 8")
    emailElem = driver8.find_element_by_id('email')
    emailElem.send_keys(noc_local_config.metricly_username)
    pElem = driver8.find_element_by_id('password')
    pElem.send_keys(noc_local_config.metricly_password)
    signInElem = driver8.find_element_by_id('ember6')
    signInElem.click()
    time.sleep(2)
    driver8.implicitly_wait(5)
    dashBoardSettings = driver8.find_element_by_xpath(
        '//*[@class="ember-basic-dropdown-trigger ria-dropdown-trigger ember-view"]')
    dashBoardSettings.click()
    time.sleep(1)
    hideNavBar = driver8.find_element_by_xpath('/html/body/div[1]/div/div/div[6]/md-switch')
    hideNavBar.click()
    dashBoardSettings.click()
    driver8.implicitly_wait(5)
    if driver8.find_elements_by_xpath('//*[@title="[NOC][Venue][ELB][Ext/Int - Site]"]'):
        var = {
            print("Monitor 8 Loaded Successfully")
        }
    else:
        monitor8_loop()
    driver8.set_window_size(1549, 900)
    driver8.set_window_position(4600, 835)
    driver8.execute_script("document.body.style.zoom='77%'")


# Will Try Total of 3 times for Monitor 8
def monitor8_loop():
    for i in range(3):
        for attempt in range(3):
            try:
                monitor8()
            except:
                print("Trying again...")
            else:
                break
        else:
            print("Check failed...Monitor 8 Did Not Load Successfully")
        break


# Kill_all function will kill all chrome, chromedriver, vlc tasks. Then one-by-one a chrome window will open up and run its own function for each monitor.
# Comment out the driver and monitor if not using.
kill_all()
driver1 = webdriver.Chrome(chromedriver, options=options)
monitor1()
monitor2a()
driver2b = webdriver.Chrome(chromedriver, options=options)
monitor2b()
driver2c = webdriver.Chrome(chromedriver, options=options)
monitor2c()
monitor2d()
# driver3 = webdriver.Chrome(chromedriver,options=options)
# monitor3()
driver4 = webdriver.Chrome(chromedriver, options=options)
monitor4()
driver5 = webdriver.Chrome(chromedriver, options=options)
monitor5()
driver6 = webdriver.Chrome(chromedriver, options=options)
monitor6()
driver7 = webdriver.Chrome(chromedriver, options=options)
monitor7()
driver8 = webdriver.Chrome(chromedriver, options=options)
monitor8()


# This function will try opening a monitor 3 more times if its failing. Everything will stop if one monitor completely fails.
# Commented out for now until this is working.
# def unstable():
#     monitor1()
#     # monitor2a()
#     monitor2b()
#     monitor2c()
#     # monitor2d()
#     # monitor3()
#     monitor4()
#     monitor5()
#     monitor6()
#     monitor7()
#     monitor8()
#
#
# result = tryagain.call(unstable, max_attempts=3)


def mouseClicks():
    print("Doing Mouse Clicks...")
    # Monitor 1
    autoit.mouse_click(x=750, y=30)
    time.sleep(1)
    # Monitor 2b
    autoit.mouse_click_drag(x1=2380, y1=235, x2=2610, y2=410)
    time.sleep(1)
    # Monitor 2c
    autoit.mouse_click_drag(x1=2275, y1=550, x2=2290, y2=660)
    time.sleep(1)
    # Monitor 2d
    autoit.mouse_click(x=2500, y=460)
    time.sleep(1)
    # Monitor 2a
    autoit.mouse_click(x=1850, y=30)
    time.sleep(1)
    # Monitor 2d
    autoit.mouse_click(x=2500, y=30)
    time.sleep(1)
    # Monitor 4
    autoit.mouse_click(x=5300, y=75)
    # Monitor 3
    autoit.mouse_click(x=3500, y=30)
    time.sleep(1)
    print("Mouse Clicks Done...")


mouseClicks()
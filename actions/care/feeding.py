from utils.randomTime import sleep as short_sleep
from selenium.webdriver.common.by import By

def feed_horse(driver):
    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']//table/tbody/tr[2]/td/form//div/div/div/span/span[2][contains(text(), Varoitus']")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'3')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[4]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass


    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'5')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[6]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'6')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[7]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'7')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[8]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'8')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[9]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'9')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[10]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'10')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[11]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'11')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[12]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'12')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[13]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'13')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[14]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'14')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[15]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    try:
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'15')]")
        hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[16]")
        hoito.click()
        short_sleep()
        driver.find_element(By.XPATH,
            "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
        short_sleep()
        hoito = driver.find_element(By.ID, "feed-button")
        hoito.click()
    except:
        pass

    # try:
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'16')]")
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[17]")
    #     hoito.click()
    #     short_sleep()
    #     driver.find_element(By.XPATH,
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     short_sleep()
    #     hoito = driver.find_element(By.ID, "feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'17')]")
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[18]")
    #     hoito.click()
    #     short_sleep()
    #     driver.find_element(By.XPATH,
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     short_sleep()
    #     hoito = driver.find_element(By.ID, "feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'18')]")
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[19]")
    #     hoito.click()
    #     short_sleep()
    #     driver.find_element(By.XPATH,
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     short_sleep()
    #     hoito = driver.find_element(By.ID, "feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'19')]")
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[20]")
    #     hoito.click()
    #     short_sleep()
    #     driver.find_element(By.XPATH,
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     short_sleep()
    #     hoito = driver.find_element(By.ID, "feed-button")
    #     hoito.click()
    # except:
    #     pass
    #
    # try:
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/span[2]/strong[contains(text(),'20')]")
    #     hoito = driver.find_element(By.XPATH, "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/div[@id='haySlider']/ol/li[21]")
    #     hoito.click()
    #     short_sleep()
    #     driver.find_element(By.XPATH,
    #         "/html/body/div[@id='container']/main[@id='content']/section/section/div[@id='console']/div[@id='sortable']/div[@id='col-left']/div[2]/div[1]/div[1]//div[1]/div[1]/div[@id='care-tab-feed']/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td/div[@id='oatsSlider']/ol/li[4]").click()
    #     short_sleep()
    #     hoito = driver.find_element(By.ID, "feed-button")
    #     hoito.click()
    # except:
    #     pass

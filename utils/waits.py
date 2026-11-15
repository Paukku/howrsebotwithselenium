"""Explicit-wait helpers for Selenium interactions."""

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.randomTime import sleep


def wait_clickable(driver, locator, timeout=10):
    """Wait until the element is clickable and return it.

    Raises TimeoutException if it does not become clickable in time.
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def click_when_ready(driver, locator, timeout=10, use_js=False, pause=sleep):
    """Wait for the element, click it, then pause.

    use_js=True clicks via JavaScript, which ignores overlays that would
    block a normal click. Raises TimeoutException if the element is not
    clickable in time.
    """
    element = wait_clickable(driver, locator, timeout)
    if use_js:
        driver.execute_script("arguments[0].click();", element)
    else:
        element.click()
    if pause:
        pause()


def try_click(driver, locator, timeout=3, **kwargs):
    """Like click_when_ready, but return False instead of raising on timeout."""
    try:
        click_when_ready(driver, locator, timeout, **kwargs)
    except TimeoutException:
        return False
    return True
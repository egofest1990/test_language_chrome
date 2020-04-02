import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_from_form_control(browser):
    browser.get(link)
    # удалите внизу решетку, чтобы было проще
    # time.sleep(30)
    browser.find_element_by_css_selector("button.btn-add-to-basket")

    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button, "Кнопка btn-add-to-basket не работает"

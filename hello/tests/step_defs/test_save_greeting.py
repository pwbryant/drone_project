# coding=utf-8
import time
import socket
from pytest_django.live_server_helper import LiveServer

"""Hello feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from splinter import Browser


@pytest.fixture(scope='session')
def splinter_webdriver():
    return 'remote'


@pytest.fixture(scope='session')
def browser(splinter_webdriver, splinter_remote_url):
    browser = Browser(
        driver_name=splinter_webdriver,
        url=splinter_remote_url,
        browser='firefox'
    )
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def test_server() -> LiveServer:
    addr = socket.gethostbyname(socket.gethostname())
    server = LiveServer(addr)
    yield server
    server.stop()

@scenario('../features/greetings.feature', 'Create a greeting')
def test_create_a_greeting():
    """Create a greeting."""
    pass


@given('I am on the grettings page')
def i_am_on_the_grettings_page(browser, test_server, transactional_db):
    """I am on the grettings page."""
    server = test_server
    browser.visit(f'{server}/greetings')


@when('I enter a greeing in the input')
def i_enter_a_greeing_in_the_input(browser):
    """I enter a greeing in the input."""
    input_ = browser.find_by_id('id_greeting')
    input_.fill('Jambo')


@when('I press the save button')
def i_press_the_save_button(browser):
    """I press the save button."""
    browser.find_by_value('Add Greeting').click()


@then('I should see the new message displayed below')
def i_should_see_the_new_message_displayed_below(browser):
    """I should not see the new message displayed below."""
    result = browser.find_by_tag('p').last.text
    assert result == 'Jambo'

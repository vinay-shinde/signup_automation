# signup_steps.py
from behave import given, when, then
from selenium import webdriver
from pages.signup_page import SignupPage
from pages.signin_page import SigninPage

@given("the user is on the signup page")
def step_user_on_signup_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    context.signup_page = SignupPage(context.driver)

@when("the user enters valid sign-up details")
def step_enter_signup_details(context):
    context.signup_page.enter_signup_details("Test", "User", "testuser@example.com", "Password123")

@when("the user submits the form")
def step_submit_signup_form(context):
    context.signup_page.click_create_account()

@then("the account is created successfully")
def step_account_created_success(context):
    success_message = context.signup_page.find_element(("css selector", ".success-msg")).text
    assert "Thank you for registering" in success_message
    context.driver.quit()

@given("the user is on the signin page")
def step_user_on_signin_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    context.signin_page = SigninPage(context.driver)

@when("the user enters valid credentials")
def step_enter_signin_details(context):
    context.signin_page.enter_signin_details("testuser@example.com", "Password123")

@when("the user submits the signin form")
def step_submit_signin_form(context):
    context.signin_page.click_signin_button()

@then("the user is redirected to the account dashboard")
def step_user_on_dashboard(context):
    assert "dashboard" in context.driver.current_url
    context.driver.quit()

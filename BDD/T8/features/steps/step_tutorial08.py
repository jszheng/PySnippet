# file:features/steps/step_tutorial08.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, greater_than

@given('I start a new game')
def step_impl(context):
    context.duck_count = 0
    context.red_button_pressed = 0

@when('I press the big red button')
def step_impl(context):
    context.red_button_pressed += 1

@when('I duck')
def step_impl(context):
    context.duck_count += 1

@when('I do the same thing as before')
def step_impl(context):
    context.execute_steps(u"""
        when I press the big {button_color} button
         and I duck
    """.format(button_color="red"))

@then('I reach the next level')
def step_impl(context):
    assert_that(context.duck_count, greater_than(0))
    assert_that(context.red_button_pressed, greater_than(0))

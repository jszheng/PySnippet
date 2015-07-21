# file:features/steps/step_tutorial06.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from testutil import NamedNumber
from company_model import CompanyModel

@given('a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel()
    for row in context.table:
        context.model.add_user(row["name"], deparment=row["department"])

@when('we count the number of people in each department')
def step_impl(context):
    context.model.count_persons_per_department()

@then('we will find {count} people in "{department}"')
def step_impl(context, count, department):
    count_ = NamedNumber.from_string(count)
    assert_that(count_, equal_to(context.model.get_headcount_for(department)))

@then('we will find one person in "{department}"')
def step_impl(context, department):
    assert_that(1, equal_to(context.model.get_headcount_for(department)))

from behave.model import Scenario
from behave.runner import Context

from tests.acceptance.environment import after_scenario as base_after_scenario
from tests.acceptance.environment import before_all as base_before_all
from tests.acceptance.environment import before_scenario as base_before_scenario


def before_all(context: Context):
    base_before_all(context)


def before_scenario(context: Context, scenario: Scenario):
    base_before_scenario(context, scenario)


def after_scenario(context: Context, scenario: Scenario):
    base_after_scenario(context, scenario)

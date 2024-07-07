from behave.model import Scenario
from behave.runner import Context

import tests.acceptance.features.hotel.custom_environment as hotel_environment
from src.di.containers import ApplicationContainer
from src.env import load_by_environment


def before_all(_: Context):
    load_by_environment("test")


def before_scenario(context: Context, scenario: Scenario):
    context.container = ApplicationContainer()
    if "hotel" in context.tags:
        hotel_environment.before_scenario(context, scenario)


def after_scenario(context: Context, _: Scenario):
    context.container.shutdown_resources()

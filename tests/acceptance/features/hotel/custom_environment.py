from behave.model import Scenario
from behave.runner import Context
from sqlalchemy import text
from sqlalchemy.orm import Session


def before_scenario(context: Context, scenario: Scenario):
    db: Session = context.container.database_package.db_session()
    db.execute(text("TRUNCATE hotel"))
    db.commit()

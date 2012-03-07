"""Setup the croner application"""
import logging

from croner.config.environment import load_environment
from croner.model.meta import Session, Base, fixture

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup croner here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(bind=Session.bind)
    fixture(Session)
    Session.commit()

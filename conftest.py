import pandas as pd
import glob
import pytest
from utils.context import Context
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    """
    Accepting custom user arguments
    """
    parser.addoption("--env", action="store", default="qa1" ,help= "Provide the environment")

    parser.addoption("--loglevel",
        action="store",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (DEBUG, INFO, WARNING, etc.)"
    )

def pytest_configure(config):
    env = config.getoption("--env")
    log_level = config.getoption("--loglevel")
    Context(env=env, log_level=log_level)


def pytest_collection_modifyitems(config, items):

    marker = config.getoption("-m", "regression")
    apps = config.getoption("-k")
    test_df = pd.DataFrame()
    if apps:
        app_list = [a.strip() for a in apps.split(",")]
        test_df = pd.concat([pd.read_csv(f"enablement/{a}.csv") for a in app_list])
    else:
        path = "enablement/*.csv"
        path_list = glob.glob(path)
        if path_list:
            test_df = pd.concat([pd.read_csv(p) for p in path_list])

    if marker:
        if marker not in test_df.columns:
            raise Exception("Marker not found in csv files provided under enablement")

        tests = test_df[test_df[marker] == "true"]["tests"].unique().tolist()

        filtered_item = []
        for item in items:
            item = item.split('/')[-1]
            if item in tests:
                filtered_item.append(item)
        items[:] = filtered_item

    else:
        return


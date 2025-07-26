import glob
import pandas as pd
from utils.context import Context
import os

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
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = f"{script_dir}/enablement/*.csv"
        path_list = glob.glob(path)
        if path_list:
            test_df = pd.concat([pd.read_csv(p) for p in path_list])

    if marker:
        if marker not in test_df.columns:
            raise Exception("Marker not found in csv files provided under enablement")

        exec_df = test_df[test_df[marker] == "true"]
        exec_df["combined"] = exec_df['modules'] + '::' + exec_df['tests']

        filtered_item = []
        for item in items:

            module_name = str(item.module.__name__).split(".")[-1]
            test_name = item.name
            full_name = f"{module_name}::{test_name}"

            if full_name in exec_df["combined"].values:
                filtered_item.append(item)
        items[:] = filtered_item

    else:
        return


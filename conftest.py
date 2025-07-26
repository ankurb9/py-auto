import glob
import pandas as pd
from utils.context import Context
import os
from pytest import Config, Item

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


def pytest_collection_modifyitems(session, config: Config, items):

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

        test_df = test_df.astype(str)
        exec_df = test_df[test_df[marker].str.lower() == "true"]
        exec_df['modules'] = exec_df['modules'].str.replace(".py", "")
        exec_df["combined"] = exec_df['modules'] + '::' + exec_df['tests']

        filtered_items = []
        discarded_items = []

        for item in items:

            module_name = str(item.module.__name__).split(".")[-1]
            test_name = str(item.name).split("[")[0]

            if module_name in exec_df["modules"].values and test_name in exec_df["tests"].values:
                item.add_marker(marker)


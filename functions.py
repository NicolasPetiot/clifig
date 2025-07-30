from params import DEFAULT_PKL
from logger import log as logger
from init_matplotlib import mpl, plt

import pickle
import pandas as pd
from pathlib import Path
def load(pkl = DEFAULT_PKL):
    """
    Command used to load the (fig, ax) tuple
    """
    logger.debug("Running `load`")

    file = open(pkl, mode = "rb")
    fig, ax = pickle.load(file)
    file.close()
    return fig, ax

def save(fig, ax, pkl = DEFAULT_PKL):
    """
    Command used to save the (fig, ax) tuple
    """
    logger.debug("Running `save`")

    file = open(pkl, mode = "wb")
    pickle.dump((fig, ax), file=file)
    file.close()

def init(pkl = DEFAULT_PKL):
    """
    Command used to initialize the (fig, ax) tuple
    """
    logger.debug("Running `init`")

    fig, ax = plt.subplots()
    save(fig, ax, pkl=pkl)

def load_data(data:Path):
    logger.debug("Running `load_data`")

    return pd.read_csv(data)

def show_fig(fig):
    logger.debug("Running `show`")

    plt.show()
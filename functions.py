from params import DEFAULT_PKL
from logger import log as logger
from init_matplotlib import mpl, plt

import pickle
import pandas as pd
from pathlib import Path
from glob import glob
from shutil import move, copy2

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

def create_backup(file:Path):
    logger.debug("Creating backup")

    if not file.exists():
        raise FileNotFoundError(f"No such file: {file}")
    
    filename = file.name
    dirname = file.parents[0]

    pattern = f"#{file}*#"
    Nbackup = len(glob(pattern))
    logger.debug(f"Found {Nbackup} existing backup")

    backupname = dirname / f"#{filename}.{Nbackup + 1}#"
    copy2(src = file, dst = backupname)
    logger.debug(f"Backup made in file {backupname}")

def load_backup(file:Path):
    logger.debug("Loading backup")

    if not file.exists():
        raise FileNotFoundError(f"No such file: {file}")
    
    filename = file.name
    dirname = file.parents[0]

    pattern = f"#{file}*#"
    Nbackup = len(glob(pattern))
    logger.debug(f"Found {Nbackup} existing backup")

    backupname = dirname / f"#{filename}.{Nbackup + 1}#"
    move(src=backupname, dst=file)
    logger.debug(f"Used {backupname} as backup")




from params import DEFAULT_PKL
from logger import log as logger
from init_matplotlib import plt

import pickle
import pandas as pd
from pathlib import Path
from glob import glob
from shutil import move, copy2
from os import remove

def load(pkl = DEFAULT_PKL):
    """
    Command used to load the (fig, ax) tuple
    """
    logger.debug(f"Running `load` with pkl={pkl}")

    file = open(pkl, mode = "rb")
    fig, ax = pickle.load(file)
    file.close()
    return fig, ax

def save(fig, ax, pkl = DEFAULT_PKL, backup = True):
    """
    Command used to save the (fig, ax) tuple
    """
    logger.debug(f"Running `save` with pkl = {pkl} and backup = {backup}")

    if backup:
        create_backup(pkl)

    file = open(pkl, mode = "wb")
    pickle.dump((fig, ax), file=file)
    file.close()

def init(pkl = DEFAULT_PKL):
    """
    Command used to initialize the (fig, ax) tuple
    """
    logger.debug(f"Running `init` with pkl = {pkl}")

    # Reinitialize backups:
    filename = pkl.name
    dirname = pkl.parents[0]
    pattern = str(dirname / f"#{filename}*#")
    for backup in glob(pattern):
        remove(backup)

    # Initialize PKL
    fig, ax = plt.subplots()
    save(fig, ax, pkl=pkl, backup=False)

def load_data(data:Path):
    logger.debug(f"Running `load_data` with data = {data}")

    return pd.read_csv(data)

def show_fig(fig):
    logger.debug("Running `show`")

    plt.show()

def create_backup(file:Path):
    logger.debug(f"Creating backup from {file}")

    if not file.exists():
        logger.error(f"No such file: {file}")
        return
    
    filename = file.name
    dirname = file.parents[0]
    pattern = str(dirname / f"#{filename}*#")

    Nbackup = len(glob(pattern))
    logger.debug(f"Found {Nbackup} existing backup")

    backupname = dirname / f"#{filename}.{Nbackup + 1}#"
    copy2(src = file, dst = backupname)
    logger.debug(f"Backup made in file {backupname}")

def load_backup(file:Path):
    logger.debug(f"Loading backup of file {file}")

    if not file.exists():
        logger.error(f"No such file: {file}")
        return
    
    filename = file.name
    dirname = file.parents[0]
    pattern = str(dirname / f"#{filename}*#")

    Nbackup = len(glob(pattern))
    logger.debug(f"Found {Nbackup} existing backup")
    if Nbackup == 0:
        logger.error("Found no existing backup")
        return

    backupname = dirname / f"#{filename}.{Nbackup}#"
    move(src=backupname, dst=file)
    logger.debug(f"Used {backupname} as backup")
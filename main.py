from logger import log as logger
from functions import init, load, load_data, save, show_fig, load_backup
from params import DEFAULT_PKL

import click
from pathlib import Path

@click.group
def cli():
    logger.debug("Running `cli`")


@cli.command
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def new(pkl:Path):
    logger.debug("Running `new`")
    init(pkl)

@cli.command
@click.option("-d", "--data", type = Path, help="File that contains data to plot")
@click.option("--x", type = str, help="X column for plot", default = "x")
@click.option("--y", type = str, help="Y column for plot", default = "y")
@click.option("--fmt", type = str, help="Matplotlib plot format", default = "ko")
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def plot(data:Path, pkl:Path, x:str, y:str, fmt:str):
    logger.debug("Running `plot`")

    ### Loading ###
    if not pkl.exists():
        init(pkl)

    fig, ax = load(pkl)
    df = load_data(data)

    ### Plot ###
    ax.plot(df[x], df[y], fmt)

    save(fig, ax, pkl, backup=True)
    
@cli.command
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def show(pkl):
    logger.debug("Running `show`")

    fig, _ = load(pkl)
    show_fig(fig)

@cli.command
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def undo(pkl):
    load_backup(pkl)



if __name__ == "__main__":
    cli()
    
from .logger import log as logger
from .functions import init, load, load_data, save, show_fig, load_backup
from .params import DEFAULT_PKL

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
@click.argument("data", type = Path)
@click.option("-x", type = str, help="X column for plot", default = None)
@click.option("-y", type = str, help="Y column for plot", default = None)
@click.option("--fmt", type = str, help="Matplotlib plot format", default = "-")
@click.option("--query", type = str, help="Query string to apply for the DataFrame", default = None)
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def plot(data:Path, x:str, y:str, fmt:str, query:str, pkl:Path):
    logger.debug("Running `plot`")

    ### Loading ###
    if not pkl.exists():
        init(pkl)

    fig, ax = load(pkl)
    df = load_data(data)
    if query is not None:
        df = df.query(query)

    ### Plot ###
    cols = df.columns
    x = cols[0] if x is None else x
    y = cols[1] if y is None else y
    ax.plot(df[x], df[y], fmt)

    save(fig, ax, pkl, backup=True)

@cli.command
@click.option("--xlabel", type=str, help = "String used as xlabel", default = None)
@click.option("--ylabel", type=str, help = "String used as ylabel", default = None)
@click.option("--xlim", type=(float, float), help = "Tuple used as xlim", default = None)
@click.option("--ylim", type=(float, float), help = "Tuple used as ylim", default = None)
@click.option("-p", "--pkl", type = Path, help = "Path to figure PKL", default = DEFAULT_PKL)
def set(xlabel:str, ylabel:str, xlim:str, ylim:str, pkl:Path):
    ### Loading ###
    if not pkl.exists():
        init(pkl)
    fig, ax = load(pkl)

    if xlabel is not None:
        ax.set_xlabel(xlabel)

    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if xlim is not None:
        ax.set_xlim(xlim)

    if ylim is not None:
        ax.set_ylim(ylim)

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
    
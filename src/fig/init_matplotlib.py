from .params import MPL_BACKEND, FONT_SIZE, FIG_SIZE
from .logger import log as logger

import matplotlib as mpl
mpl.use(MPL_BACKEND)
logger.debug(f"Set matplotlib backend to '{MPL_BACKEND}'")

import matplotlib.pyplot as plt
plt.rcParams.update({
    "figure.figsize": FIG_SIZE,
    "font.size": FONT_SIZE
})
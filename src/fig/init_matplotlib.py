from .params import MPL_BACKEND
from .logger import log as logger

import matplotlib as mpl
mpl.use(MPL_BACKEND)
logger.debug(f"Set matplotlib backend to '{MPL_BACKEND}'")

import matplotlib.pyplot as plt
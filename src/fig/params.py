# Matplotlib Params:
MPL_BACKEND = "TkAgg"

# Cache Params:

from pathlib import Path
PKL_DIR = Path(__file__).parents[0]
DEFAULT_PKL = PKL_DIR / "fig.pkl"

# Logging parameters:
LOG_LVL = "debug"
LOG_FMT = "[%(asctime)s %(levelname)s] %(message)s"
DATE_FMT = "%Y-%m-%d %H:%M:%S"

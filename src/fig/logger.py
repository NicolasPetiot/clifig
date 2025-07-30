from .params import LOG_LVL, LOG_FMT, DATE_FMT

import logging

log = logging.getLogger(__name__)
match LOG_LVL.lower():
    case "debug":
        log.setLevel(logging.DEBUG)
    
    case "info":
        log.setLevel(logging.INFO)

    case "error":
        log.setLevel(logging.ERROR)

    case "critical":
        log.setLevel(logging.CRITICAL)

    case _:
        raise ValueError(f"{LOG_LVL} not recognized")

formatter = logging.Formatter(
    fmt=LOG_FMT,
    datefmt=DATE_FMT
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)
log.propagate = False

log.debug("Logger initialized")
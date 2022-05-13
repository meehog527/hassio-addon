import logging
import logging.config
import yaml
import os

APP_ROOT = "btmqttgw"
SUPPRESSION_ENABLED = False

def make_path(name):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, name)
    return filename

def setup():
    with open(make_path("logger.yaml"), "rt") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)


def get(name=None):
    if name:
        logger_name = "{}.{}".format(APP_ROOT, name)
    else:
        logger_name = APP_ROOT
    return logging.getLogger(logger_name)


def enable_debug_formatter():
    logging.getLogger().handlers[0].setFormatter(
        logging.getLogger("dummy_debug").handlers[0].formatter
    )


def reset():
    app_level = get().getEffectiveLevel()

    root = logging.getLogger()
    map(root.removeHandler, root.handlers[:])
    map(root.removeFilter, root.filters[:])

    setup()
    get().setLevel(app_level)
    if app_level <= logging.DEBUG:
        enable_debug_formatter()


def suppress_update_failures(suppress):
    global SUPPRESSION_ENABLED
    SUPPRESSION_ENABLED = suppress


def log_exception(logger, message, *args, **kwargs):
    if not (kwargs.pop('suppress', False) and SUPPRESSION_ENABLED):
        if logger.isEnabledFor(logging.DEBUG):
            logger.exception(message, *args, **kwargs)
        elif logger.isEnabledFor(logging.WARNING):
            logger.warning(message, *args, **kwargs)

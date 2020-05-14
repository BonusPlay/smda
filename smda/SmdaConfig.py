import os
import logging


class SmdaConfig(object):

    # note to self: always change this in setup.py as well!
    VERSION = "1.2.10"
    CONFIG_FILE_PATH = str(os.path.abspath(__file__))
    PROJECT_ROOT = str(os.path.abspath(os.sep.join([CONFIG_FILE_PATH, "..", ".."])))

    ### An (optional) WinAPI database as generated by ApiScout (https://github.com/danielplohmann/apiscout)
    API_COLLECTION_FILES = {}
    ### global logging-config setup
    # Only do basicConfig if no handlers have been configured
    LOG_PATH = "./"
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = "%(asctime)-15s: %(name)-32s - %(message)s"

    ### SMDA disassembler config
    # maximum time in seconds for disassembly to complete
    TIMEOUT = 300
    # maximum number of bytes to allocate while loading
    MAX_IMAGE_SIZE = 100 * 1024 * 1024
    # improve disassembly by resolving references through data flows
    USE_ALIGNMENT = True
    USE_SYMBOLS_AS_CANDIDATES = True
    RESOLVE_REGISTER_CALLS = True
    HIGH_ACCURACY = True
    RESOLVE_TAILCALLS = False
    # optional metadata generation options
    CALCULATE_SCC = False
    # confidence score to use for filtering functions before including them in the output
    CONFIDENCE_THRESHOLD = 0.0

    def __init__(self, log_level=logging.INFO):
        if len(logging._handlerList) == 0:
            logging.basicConfig(level=log_level, format=self.LOG_FORMAT)

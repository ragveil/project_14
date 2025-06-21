import os

from config import ROOT_DIR

PATH_TO_DATA = os.path.join(ROOT_DIR, "data/")  # pragma: no cover
PATH_TO_JSON = os.path.join(PATH_TO_DATA, "products.json")  # pragma: no cover
PATH_TO_TEST_JSON = os.path.join(ROOT_DIR, "tests/", "data/", "test_products.json")  # pragma: no cover

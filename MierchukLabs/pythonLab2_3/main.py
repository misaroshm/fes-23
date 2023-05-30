from config import Config
from hive import Hive

"""Runs a Hive instance."""

hive: Hive = Hive(Config())

hive.run()
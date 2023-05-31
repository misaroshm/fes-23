from searchregion import Playground
from agents import Hive


if __name__ == "__main__":
    playground = Playground()
    hive = Hive(playground)
    hive.initialize_all()
    hive.run()

from .container import Container
from .config import load_config
from .modules.injected import injected_function,InjectedClass
from os import path

if __name__ == "__main__":
  container = Container()
  cfg = load_config(path.join(path.dirname(path.abspath(__file__)), 'config.json'))
  container.config.from_value(cfg)
  container.wire(modules=[".modules.injected"])

  print('in function:')
  injected_function()

  print()
  print('in class:')
  InjectedClass()
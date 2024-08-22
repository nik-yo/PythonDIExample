from dependency_injector.wiring import Provide, inject
from ..container import Container
from ..config import Config

@inject
def injected_function(config: Config = Provide[Container.config]):
  print(config.some_config.some_key)

class InjectedClass:
  @inject
  def __init__(self, config: Config = Provide[Container.config]):
    print(config.some_config.some_key)

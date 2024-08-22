from ..config import Config

def injected_function(config: Config = Config().load()):
  print(config.some_config.some_key)

class InjectedClass(Config):
  def __init__(self):
    self.config = super().load()
    print(self.config.some_config.some_key)
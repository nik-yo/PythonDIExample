from .modules.injected import injected_function,InjectedClass

if __name__ == "__main__":
  print('in function:')
  injected_function()

  print()
  print('in class:')
  InjectedClass()
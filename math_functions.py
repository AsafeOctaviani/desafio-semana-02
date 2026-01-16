def add(n,porcentagem,formatted=False):
  aumento = n # Corrigido: 'aumento:0' para 'aumento = 0'

  n=n*porcentagem/100
  aumento+=n
  return aumento if formatted == False else coin(aumento)

def subtract(n,porcentagem,formatted=False):
  diminui = n # Corrigido: 'aumento:0' para 'aumento = 0'

  n=n*porcentagem/100
  diminui-=n
  return diminui if formatted == False else coin(diminui)


def double(n,formatted=False):

  n*=2
  return n if formatted == False else coin(n)


def half(n,formatted=False):
  n/=2
  return n if formatted == False else coin(n)

def coin(value=0,sign="$",formatted=False):
  return f"{sign}{value:.2f}"


def resume(value=50,percent=25,formatted=False):
  print("-=-"*15)
  print("RESUME".center(45))
  print("-=-"*15)

  print(f"The price is: \t\t\t\t{value}")
  print(f"{value} plus {percent}%: \t\t\t\t{add(value,percent,formatted)}")
  print(f"{value} minus {percent}%: \t\t\t{subtract(value,percent,formatted)}")
  print(f"double {value}: \t\t\t\t{double(value,formatted)}")
  print(f"half {value}: \t\t\t\t{half(value,formatted)}")
  # print(f"The sum of {value} plus {percent}% is equals {add(value,percent,formatted)}")
  # print(f"The subtract of {value} minus {percent}% is equals {subtract(value,percent,formatted)}")
  # print(f"The double of {value} is equals {double(value,formatted)}")
  # print(f"The half of {value} is equals {half(value,formatted)}")


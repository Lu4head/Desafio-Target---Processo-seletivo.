def verificafibonacci(num):
  a , b = 0 , 1
  count = 0

  while b < num:
    a , b = b , a + b
    count = count + 1
  
  if b == num:
    return True, count+2

  elif num == 0:
    return True, 1
  
  else:
    return False, None


num = int(input("Digite um número inteiro: "))
e_fibonacci , posicao = verificafibonacci(num)
if e_fibonacci:
  print("Seu número pertence à sequência de Fibonacci e está na posicão: ",posicao);
else:
  print("Seu número não pertence à sequência de Fibonacci");
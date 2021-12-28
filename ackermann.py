def ack(m, n):
    if m < 0:
        print("A função de Ackermann não está definida para valores de m menores que 0.")
        return None
    
    elif (m > 0) and ( n < 0):
        print("A dunção de Ackermann não está definida para valores de n menores do 0.")
        return None

    elif m == 0:
        return n + 1
    
    elif (m > 0) and (n == 0):
        temp_a = ack(m-1, 1)
        return temp_a
    
    elif (m > 0) and (n > 0):
        temp_b = ack(m-1, ack(m, n-1))
        return temp_b
    
    else:
        print("Esse valor não é contemplado da definição da função.")
        return None

a = ack(3, 4)
print(a)
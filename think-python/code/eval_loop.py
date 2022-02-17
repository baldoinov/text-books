def eval_loop():

    user_input = None

    while True:
        last_input = user_input
        user_input = str(input("Insert something: "))

        if user_input == 'done':
            break

        print(f"Evaluated {user_input} → {eval(user_input)}\n")

    print(f"The last evaluation was {last_input} → {eval(last_input)}")


eval_loop()

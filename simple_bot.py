def welcome():
    print("Привіт! Я простий бот.")
    print("Напиши 'привіт', 'допомога' або 'вийти'.")

def respond(command):
    if command == "привіт":
        return "Вітаю! Як справи?"
    elif command == "допомога":
        return "Я можу вітатися і завершувати роботу."
    elif command == "вийти":
        return "Бувай!"
    else:
        return "Не розумію цю команду."

def chat():
    welcome()
    while True:
        user_input = input("Ти: ").lower()
        reply = respond(user_input)
        print("Бот:", reply)
        if user_input == "вийти":
            break

if __name__ == "__main__":
    chat()

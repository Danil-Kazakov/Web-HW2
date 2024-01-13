from Bot import AbstractBot, AddBot, SearchBot, EditBot, RemoveBot, SaveBot, LoadBot, CongratulateBot, ViewBot, ExitBot


if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    
    choice = {
        "add": AddBot(),
        "search": SearchBot(),
        "edit": EditBot(),
        "remove": RemoveBot(),
        "save": SaveBot(),
        "load": LoadBot(),
        "congratulate": CongratulateBot(),
        "view": ViewBot(),
        "exit": ExitBot(),
    }

    commands = list(choice.keys())  # Retrieve available commands
    
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()

        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                print(format_str.format(command))
            continue
        
        if action in choice:
            selected_bot = choice[action]
            selected_bot.handle()
            if action in ['add', 'remove', 'edit']:
                selected_bot.book.save("auto_save")
        elif action == 'exit':
            break
        else:
            print("Incorrect action!")




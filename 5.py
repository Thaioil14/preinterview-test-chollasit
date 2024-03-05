class BrowserHistory:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def input_url(self, url):
        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index = len(self.history) - 1

    def go_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            return self.history[self.current_index]
        else:
            return "No website to previous"

    def go_next(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            return self.history[self.current_index]
        else:
            return "No website to go"

    def current_page(self):
        if self.current_index >= 0:
            return "Now you on " + self.history[self.current_index]
        else:
            return "No website visited yet"

    def show_all_history(self):
        if self.history:
            return self.history
        else:
            return "No website visited yet"

history = BrowserHistory()
x = input().lower()
while x != "exit":
    if x[:5] == "input":
        input_split = x.split()
        history.input_url(input_split[1])
    elif x == "prev":
        print(history.go_previous())
    elif x == "next":
        print(history.go_next())
    elif x == "current":
        print(history.current_page())
    elif x == "all":
        print(history.show_all_history())
    else:
        print("Error!!! check your command")
    x = input().lower()


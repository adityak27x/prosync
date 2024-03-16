import eel
from src.login.login import check_login
from src.stats import leetcode
from src.askgemini import askgenai

eel.init('web')


@eel.expose
def Leetcode():
    return leetcode.Leetcode("kaamimi")

@eel.expose
def login(username, password):
    if check_login(username, password):
        return True
    else:
        return False


@eel.expose
def redirect_to_home():
    eel.show('home.html')

@eel.expose
def askgemini(question):
    return askgenai.processQuestion(question)


if __name__ == "__main__":
    eel.start('signin.html', size=(700, 500))
    print(Leetcode())

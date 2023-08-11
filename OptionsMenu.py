import sys
try:
	from PyInquirer import prompt
except:
	pass
from examples import custom_style_2
def options_menu():
    exit_loop = False

    while not exit_loop:
        options = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Select module',
                'choices': [
                    '1) AV test engine',
                    '2) MalwareBuilder',
                    '3) Exit'
                ]
            }
        ]
        answers = prompt(options,style=custom_style_2)

        if answers['option'] == '1) AV test engine':
            av_menu()
        elif answers['option'] == '2) MalwareBuilder':
            print("Selected MalwareBuilder")
        elif answers['option'] == '3) Exit':
            sys.exit("Exiting the program")

def av_menu():
    exit_loop2 = False
    while not exit_loop2:
        options = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Select AV test type',
                'choices': [
                    '1) Worm',
                    '2) Trojan',
                    '3) Rootkit',
                    '4) CryptoMining',
                    '5) Ransomware',
                    '6) Spyware',
                    '7) Go back'
                ]
            }
        ]
        answers = prompt(options,style = custom_style_2)

        if answers['option'] == '1) Worm':
          executeWorm()
        elif answers['option'] == '2) Trojan':
            executeTrojan()
        elif answers['option'] == '3) Rootkit':
            executeRootkit()
        elif answers['option'] == '4) CryptoMining':
            executeCryptoMining()
        elif answers['option'] == '5) Ransomware':
            executeRansomware()
        elif answers['option'] == '6) Spyware':
            executeSpyware()
        elif answers['option'] == '7) Go back':
            exit_loop2 = True

# def mb_menu():
#     MBoptions = {
#         '1': ('Trojan', executeTrojan),
#         '2': ('Rootkit', executeRootkit),
#         '3': ('CryptoMining', executeCryptoMining),
#         '4': ('Ransomeware', executeRansomware),
#         '5': ('Spyware', executeSpyware)
#     }
#     # Add menu logic here similar to av_menu()

def executeWorm():
    print('Executing Worm')

def executeTrojan():
    print('Executing Trojan')

def executeRootkit():
    print('Executing Rootkit')

def executeCryptoMining():
    print('Executing CryptoMining')

def executeRansomware():
    print('Executing Ransomeware')

def executeSpyware():
    print('Executing Spyware')

if __name__ == "__main__":
    options_menu()

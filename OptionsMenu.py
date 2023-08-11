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
            mb_menu()
        elif answers['option'] == '3) Exit':
            sys.exit("Exiting the program")

def av_menu():
    exit_loop2 = False
    AVToptions = {
        '1': ('Worm', executeWorm),
        '2': ('Trojan', executeTrojan),
        '3': ('Rootkit', executeRootkit),
        '4': ('CryptoMining', executeCryptoMining),
        '5': ('Ransomeware', executeRansomware),
        '6': ('Spyware', executeSpyware)
    }

    while not exit_loop2:
        options = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Select AV test type',
                'choices': [f'{key}) {value[0]}' for key, value in AVToptions.items()]
            }
        ]
        answers = prompt(options)

        selected_option = answers['option']
        if selected_option in AVToptions:
            function_to_execute = AVToptions[selected_option][1]
            function_to_execute()

def mb_menu():
    MBoptions = {
        '1': ('Trojan', executeTrojan),
        '2': ('Rootkit', executeRootkit),
        '3': ('CryptoMining', executeCryptoMining),
        '4': ('Ransomeware', executeRansomware),
        '5': ('Spyware', executeSpyware)
    }

    # Add menu logic here similar to av_menu()

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

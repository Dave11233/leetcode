cmds = {

    'reset': 'reset what',
    'reset board': 'board fault',
    'board add': 'where to add',
    'board delete': 'no board at all',
    'reboot backplane': 'impossible',
    'backplane abort': 'install first'

}

while True:
    try:
        cmd = input()
        if cmd in cmds:
            print(cmds[cmd])
        else:
            print("unknown command")
    except EOFError:
        break

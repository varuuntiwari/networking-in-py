import socket

PORT = 9909

SERVER_POINTS = 0
CLIENT_POINTS = 0


def initConnection(ip):
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((ip, PORT))
    msg = cli.recv(4096)
    print(msg.decode("UTF-8"))
    printRules()
    cliGame(cli)
    cli.close()
    

def acceptConnection():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('0.0.0.0', PORT))
    serv.listen(1)
    print('Waiting for connection...')
    while True:
        clisock, cliaddr = serv.accept()
        print(f"Connected with {cliaddr[0]} on port {cliaddr[1]}")
        clisock.send(bytes("You are now connected with the server", "UTF-8"))
        printRules()
        servGame(clisock)
        clisock.close()

def printRules():
    print("Enter your choice as a number given below and wait for other player's response")
    print("1. Rock\n2.Paper\n3.Scissors\n4.Lizard\n5.Spock\n6. Exit\n7. Show rules again")

def cliGame(sock):
    while True:
        opt = int(input(": "))
        if opt == 6:
            break
        else:
            sock.send(bytes(MappingNums(opt), "UTF-8"))
            score = sock.recv(1024).decode("UTF-8")
            print(score)

def printScore():
    global SERVER_POINTS
    global CLIENT_POINTS
    return f'''\n
                   ------------\n
                SERVER   |   CLIENT\n
                     {SERVER_POINTS}   |   {CLIENT_POINTS}\n
                   ------------
            '''

def servGame(sock):
    global SERVER_POINTS
    global CLIENT_POINTS
    while True:
        opt = int(input(": "))
        if opt == 6:
            break
        print("Waiting for other player's response...")
        resp = sock.recv(1024)
        resp = resp.decode("UTF-8")

        res = logicGame(MappingNums(opt), resp)
        if res == 1:
            SERVER_POINTS += 1
        elif res == 0:
            CLIENT_POINTS += 1

        score = printScore()
        print(score)
        sock.send(bytes(score, "UTF-8"))

def MappingNums(x):
    switch = {
        1:  "Rock",
        2:  "Paper",
        3:  "Scissors",
        4:  "Lizard",
        5:  "Spock"
    }
    return switch.get(x, "Invalid")

def logicGame(serv, cli):
    weaknesses = {"Rock" : ["Paper, Spock"],
            "Paper" : ["Scissors", "Lizard"],
            "Scissors" : ["Rock", "Spock"],
            "Lizard" : ["Rock", "Scissors"],
            "Spock" : ["Lizard", "Paper"]
            }
    cli_weaknesses = weaknesses[cli]
    if serv == cli:
        return 2
    elif serv == "Invalid" or cli == "Invalid":
        raise ValueError("Value out of options given")
    for weakness in cli_weaknesses:
        if serv == weakness:
            return 1
    return 0

    

def welcomeGame():
    print('''Welcome to the game of Rock Paper Scissors Lizard Spock, a variation of the classic version
as given in the TV series 'The Big Bang Theory'. The rules for playing are simple, given below in the words
of Sheldon Cooper:
\t"Scissors cuts Paper,
\t Paper covers Rock,
\t Rock crushes Lizard,
\t Lizard poisons Spock,
\t Spock smashes Scissors,
\t Scissors decapitates Lizard,
\t Lizard eats Paper,
\t Paper disproves Spock,
\t Spock vaporizes Rock,
\t (and as it always has) Rock crushes Scissors."
\nNOTICE: This game uses the port 9909 for playing, change it in the code if is occupied!\n''')

def main():
    welcomeGame()
    if input('Do you want to initialize connection?(y/n): ') == 'y':
        print('Make sure the other player is in the same internal network')
        ip = input("Enter the other player's IP address: ")
        initConnection(ip)
    else:
        acceptConnection()
    print("Thankyou for playing!")

if __name__ == "__main__":
    main()
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


#These two functions help me to create My data_structure

def line_data(s):
    lines, line = [], ''
    for i in s:
        if i == ".":
            lines.append(line)
            line = ""
        else:
            line  = line + i
    return lines

def split_game(s):
    split, game = [], ''
    for i in range(0, len(s)):
        if s[i] == ',' or s[i] == '.':
            split.append(game)
            game = ''
        else:
            if not game and s[i] == ' ': #To remove space before the game!!
                None
            else:
                game = game + s[i]
    if game:
        split.append(game)
    return split

#-------------------------------------------------------

def create_data_structure(string_input):
    network = {}
    data = line_data(string_input)
    for i in data:
        if i.find('is connected to') != -1:
            user = i[0:i.find('is connected to')-1] #using [] method to capte the username
            connect = i[i.find('is connected to')+16:]
            connected = connect.replace(',', ' ').split()
            network.update({user: [connected]})
        if i.find('likes to play') != -1:
            user = i[0:i.find('likes to play')-1]
            game = i[i.find('likes to play')+14:]
            game_play = split_game(game)
            network[user].append(game_play)
    return network


def get_connections(network, user):
    if user in network:
        return network[user][0]
    return None


def get_games_liked(network,user):
    if user in network:
        return network[user][1]
    return None


def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B in get_connections(network, user_A):
        return network
    network[user_A][0].append(user_B)
    return network


def add_new_user(network, user, games):
    if user in network:
        return network
    network.update({user: [[], games]})
    return network
		

def get_secondary_connections(network, user):
    secondary_connections = []
    if user not in network:
        return None
    for i in network[user][0]:
        for user in network[i][0]:
            if user not in secondary_connections:
                secondary_connections.append(user)
    return secondary_connections


def count_common_connections(network, user_A, user_B):
    count = 0
    if user_A not in network or user_B not in network:
        return False
    user_A_connections = get_connections(network, user_A)
    user_B_connections = get_connections(network, user_B)
    for user in user_A_connections:
        if user in user_B_connections:
            count = count + 1
    return count


def find_path_to_friend(network, user_A, user_B, Check_Test=None):
    if Check_Test == None:
        Check_Test = []
    if user_A not in network or user_B not in network:
        return None
    path = [user_A]
    connections = get_connections(network, user_A)
    Check_Test.append(user_A)
    if user_B in connections:
        return path + [user_B]
    else:
        for user in connections:
            if user not in Check_Test:
                newpath = find_path_to_friend(network, user, user_B, Check_Test)
                if newpath:
                    return path + newpath
    return None

    
#RalphProgrammer ==> rallralph.haver@gmail.com / +50938325242 || Coding Coding Coding

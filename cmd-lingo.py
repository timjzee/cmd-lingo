import random

with open("invar_freqs3.csv", "r") as f:
    words = [line.split(",")[0] for line in f]

n_letters = 0
while n_letters < 3:
    letters_input = input("Hoe veel letters? ")
    input_ok = True
    for i in letters_input:
        if ord(i) not in range(48, 58):
            input_ok = False
    if input_ok:
        n_letters = int(letters_input)

relevant_words = [w for w in words if len(w) == n_letters]

n_rounds = 0
while n_rounds < 1 or n_rounds > len(relevant_words) // 2:
    round_input = input("Hoe veel ronden? ")
    input_ok = True
    for i in round_input:
        if ord(i) not in range(48, 58):
            input_ok = False
    if input_ok:
        n_rounds = int(round_input)

n_loops = 2 * n_rounds

selected_words = random.sample(relevant_words, n_loops)

player1 = input("Naam speler 1: ")
player1 = "player1" if player1 == "" else player1

player2 = input("Naam speler 2: ")
player2 = "player2" if player2 in ["", player1] else player2

points = {player1: 0, player2: 0}
current_player = ""
for loop, word in enumerate(selected_words, 1):
    if loop == 1:
        current_player = random.sample([player1, player2], 1)[0]
    print("Speler '{}' is aan de beurt.\n".format(current_player))
    word_l = [letter for letter in word]
    word_frag = [word[0]] + ["." for letter in word[1:]]
    for guess in range(1, 6):
        print(str(guess) + ": " + " ".join(word_frag))
#        print("debug: " + word)
        word_guess_i = input("> ")
        word_guess = [letter for letter in word_guess_i.strip(" ")]
        guess_stat = []
        if word_guess_i.strip(" ") in relevant_words:
            if word_guess == word_l:
                points[current_player] += (60 - 10 * guess)
                guess_stat = ["V" for letter in word]
                break
            else:
                for num, letter in enumerate(word_guess, 0):
                    match_indices = []
                    for l_i, let in enumerate(word_l, 0):
                        if let == letter and l_i != num:
                            match_indices.append(l_i)
                    match_indices2 = []
                    for m_i in match_indices:
                        if word_guess[m_i] != letter:
                            match_indices2.append(m_i)
                    if letter != word_l[num] and len(match_indices2) == 0:
                        guess_stat.append("X")
                    elif letter == word_l[num]:
                        guess_stat.append("V")
                        word_frag[num] = letter
                    elif len(match_indices2) > 0:
                        guess_stat.append("?")
            print("   " + " ".join(word_guess))
            print("   " + " ".join(guess_stat))
        else:
            print("Dit woord voldoet niet aan de eisen.")
    if word_frag != word_l:
        print("Het woord was '{}'.".format(word))
    current_player = player1 if current_player != player1 else player2

print("{}'s points: {}".format(player1, points[player1]))
print("{}'s points: {}".format(player2, points[player2]))
if points[player1] > points[player2]:
    print(player1 + " wint!!!")
elif points[player1] == points[player2]:
    print("Gelijkspel!")
else:
    print(player2 + " wint!!!")

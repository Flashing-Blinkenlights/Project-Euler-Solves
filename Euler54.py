from treys import Card, Evaluator

evaluator = Evaluator()


def hand_from_str(hand_str):
    cards = [c.capitalize() for c in hand_str.split(" ")]
    return cards


with open("0054_poker.txt") as f:
    games = f.read().strip().split("\n")

p1_wins = 0

for i, game in enumerate(games):
    game_hands = hand_from_str(game)

    p1_hand = game_hands[:5]
    p2_hand = game_hands[5:]

    p1_score = evaluator.evaluate(list(map(Card.new, p1_hand)), [])
    p2_score = evaluator.evaluate(list(map(Card.new, p2_hand)), [])

    print(f"{i + 1}\t{p1_hand} vs {p2_hand}:\t P1 ", end="")

    if p1_score < p2_score:
        print("wins!")
        p1_wins += 1
    else:
        print("loses.")

print(p1_wins)

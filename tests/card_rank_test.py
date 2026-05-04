from treys import Evaluator, Card

hand = [Card.new('Qh'), Card.new('Th')]
board = [Card.new('2h'), Card.new('2s'), Card.new('Ah'), Card.new('Kh'), Card.new('Jh')]

evaluator = Evaluator()

rank = evaluator.evaluate(board, hand)
print(rank)

score_class = evaluator.get_rank_class(rank)
print(score_class)

print(f"Player 1 hand rank = {evaluator.class_to_string(score_class)}".format(rank))

hand_rank = evaluator.class_to_string(score_class).format(rank)
print(hand_rank)
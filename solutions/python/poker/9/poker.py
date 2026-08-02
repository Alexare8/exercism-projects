from collections import Counter
from enum import IntEnum
from functools import total_ordering


@total_ordering
class Card:
    """A playing card with a rank and a suit, and the ability to compare against other cards."""
    RANKS = {"10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    SUITS = {"H": 0, "C": 1, "D": 2, "S": 3}

    def __init__(self, raw_card: str) -> None:
        rank, suit = raw_card[:-1], raw_card[-1]
        self.print_rank = rank
        self.print_suit = suit
        self.suit = self.SUITS[suit]
        if rank in self.RANKS:
            self.rank = self.RANKS[rank]
        else:
            self.rank = int(rank)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.print_rank}{self.print_suit}"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank

    def __gt__(self, other) -> bool:
        return self.rank > other.rank

    @staticmethod
    def sort_key(card) -> int:
        return card.rank * 10 + card.suit


@total_ordering
class Hand:
    """A hand of cards fit to the highest possible poker hand."""
    class PokerHand(IntEnum):
        PAIR = 0
        TWOPAIR = 1
        THREEOFAKIND = 2
        ACELOWSTRAIGHT = 3
        STRAIGHT = 4
        FLUSH = 5
        FULLHOUSE = 6
        FOUROFAKIND = 7
        ACELOWSTRAIGHTFLUSH = 8
        STRAIGHTFLUSH = 9

    def __init__(self, cards: list[Card]) -> None:
        self.original = " ".join([str(card) for card in cards])
        sorted_cards = sorted(cards, reverse=True)
        self.ranks = Counter([card.rank for card in sorted_cards])
        self.cards = sorted(sorted_cards, key=lambda x: self.ranks[x.rank], reverse=True)
        self.flush = len({card.suit for card in cards}) == 1

        match sorted(self.ranks.values(), reverse=True):
            case [4,1]:
                self.hand_score = self.PokerHand.FOUROFAKIND
            case [3,2]:
                self.hand_score = self.PokerHand.FULLHOUSE
            case [3,1,1]:
                self.hand_score = self.PokerHand.THREEOFAKIND
            case [2,2,1]:
                self.hand_score = self.PokerHand.TWOPAIR
            case [2,1,1,1]:
                self.hand_score = self.PokerHand.PAIR
            case [1,1,1,1,1]:
                if self.ace_low_straight():
                    if not self.flush:
                        self.hand_score = self.PokerHand.ACELOWSTRAIGHT
                    else:
                        self.hand_score = self.PokerHand.ACELOWSTRAIGHTFLUSH
                elif self.straight():
                    if not self.flush:
                        self.hand_score = self.PokerHand.STRAIGHT
                    else:
                        self.hand_score = self.PokerHand.STRAIGHTFLUSH
                elif self.flush:
                    self.hand_score = self.PokerHand.FLUSH
                else:
                    self.hand_score = -1

    def __str__(self) -> str:
        return self.original

    def __eq__(self, other) -> bool:
        return self.cards == other.cards

    def __gt__(self, other: "Hand") -> bool:
        """Determine if a this hand is higher scoring than another."""
        if self.hand_score != other.hand_score:
            return self.hand_score > other.hand_score
        if self.hand_score in {self.PokerHand.ACELOWSTRAIGHT, self.PokerHand.ACELOWSTRAIGHTFLUSH}:
            return self.cards[-2].suit > other.cards[-2].suit # Compare the highest non-ace cards' suits
        return self.cards > other.cards

    def ace_low_straight(self) -> bool:
        """Check if hand is an ace low straight."""
        return set(self.ranks) == {2, 3, 4, 5, 14}

    def straight(self) -> bool:
        """Check if hand is a straight."""
        low_card_rank = self.cards[-1].rank
        rank_series = {rank - low_card_rank for rank in self.ranks}
        return rank_series == {0, 1, 2, 3, 4}


def best_hands(raw_hands: list[str]) -> list[str]:
    """Choose the best hand from a list of poker hands."""
    hands = []
    for hand in raw_hands:
        cards = [Card(card) for card in hand.split(" ")]
        hands.append(Hand(cards))

    highest_hands = [hands[0]]
    highest_hand = hands[0]
    for hand in hands[1:]:
        if hand == highest_hand:
            highest_hands.append(hand)
        elif hand > highest_hand:
            highest_hands = [hand]
            highest_hand = hand

    return [hand.original for hand in highest_hands]

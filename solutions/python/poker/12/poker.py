from collections import Counter
from enum import IntEnum, auto
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


@total_ordering
class Hand:
    """A hand of cards fit to the highest possible poker hand."""
    class PokerHand(IntEnum):
        HIGH_CARD = auto()
        PAIR = auto()
        TWOPAIR = auto()
        THREEOFAKIND = auto()
        STRAIGHT = auto()
        FLUSH = auto()
        FULLHOUSE = auto()
        FOUROFAKIND = auto()
        STRAIGHTFLUSH = auto()

    def __init__(self, cards: list[Card]) -> None:
        self.original = " ".join([str(card) for card in cards])
        sorted_cards = sorted(cards, reverse=True)
        self.ranks = Counter([card.rank for card in sorted_cards])
        self.cards = sorted(sorted_cards, key=lambda x: self.ranks[x.rank], reverse=True)
        self.flush = len({card.suit for card in self.cards}) == 1

        match sorted(self.ranks.values(), reverse=True):
            case [4,1]:
                self.score = self.PokerHand.FOUROFAKIND
            case [3,2]:
                self.score = self.PokerHand.FULLHOUSE
            case [3,1,1]:
                self.score = self.PokerHand.THREEOFAKIND
            case [2,2,1]:
                self.score = self.PokerHand.TWOPAIR
            case [2,1,1,1]:
                self.score = self.PokerHand.PAIR
            case [1,1,1,1,1]:
                if self.straight():
                    if not self.flush:
                        self.score = self.PokerHand.STRAIGHT
                    else:
                        self.score = self.PokerHand.STRAIGHTFLUSH
                    if self.ace_low_straight():
                        for card in self.cards:
                            if card.rank == 14:
                                card.rank = 1
                        self.cards = sorted(self.cards, reverse=True)
                elif self.flush:
                    self.score = self.PokerHand.FLUSH
                else:
                    self.score = self.PokerHand.HIGH_CARD

    def __str__(self) -> str:
        return self.original

    def __eq__(self, other) -> bool:
        return self.score == other.score and self.cards == other.cards

    def __gt__(self, other: "Hand") -> bool:
        """Determine if a this hand is higher scoring than another."""
        if self.score != other.score:
            return self.score > other.score
        return self.cards > other.cards

    def ace_low_straight(self) -> bool:
        """Check if hand is an ace low straight."""
        return set(self.ranks) == {2, 3, 4, 5, 14}

    def straight(self) -> bool:
        """Check if hand is a straight."""
        high_card_rank = self.cards[0].rank
        low_card_rank = self.cards[-1].rank
        return high_card_rank - low_card_rank == 4 or self.ace_low_straight()

def best_hands(raw_hands: list[str]) -> list[str]:
    """Choose the best hand from a list of poker hands."""
    hands = []
    for hand in raw_hands:
        cards = [Card(card) for card in hand.split(" ")]
        hands.append(Hand(cards))

    highest_hand = max(hands)
    return [hand.original for hand in hands if hand == highest_hand]

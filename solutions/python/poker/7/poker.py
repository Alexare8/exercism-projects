from collections import Counter
from enum import IntEnum
from functools import total_ordering
from typing import NamedTuple


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

    def __str__(self) -> str:
        return f"{self.print_rank}{self.print_suit}"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other) -> bool:
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False
        return self.suit > other.suit

    @staticmethod
    def sort_key(card) -> int:
        return card.rank * 10 + card.suit


class Parsed_Hand(NamedTuple):
    cards: list[Card]
    ranks: Counter
    flush: bool


class Hand:
    """A hand of cards fit to the highest possible poker hand."""
    def __init__(self, cards: list[Card]) -> None:
        self.original = " ".join([str(card) for card in cards])
        self.poker_hand = -1
        self.scored_cards = []
        self.unscored_cards = sorted(cards, key=Card.sort_key)
        self.ranks = Counter([card.rank for card in self.unscored_cards])
        self.suits = len({card.suit for card in self.unscored_cards}) == 1
        self.parsed_hand = Parsed_Hand(self.unscored_cards, self.ranks, self.suits)
        for poker_hand, value in POKER_HANDS.items():
            scored_cards, unscored_cards = poker_hand(self.parsed_hand)
            if scored_cards != []:
                self.poker_hand = value
                self.scored_cards = scored_cards
                self.unscored_cards = unscored_cards
                break

    def __str__(self) -> str:
        return self.original

    def greater_than_hand(self, other: "Hand") -> bool | None:
        """Determine if a this hand is higher scoring than another."""
        if self.poker_hand != other.poker_hand:
            return self.poker_hand > other.poker_hand
        if self.poker_hand in {PokerHand.ACELOWSTRAIGHT, PokerHand.ACELOWSTRAIGHTFLUSH}:
            return self.scored_cards[-2] > other.scored_cards[-2] # Compare the highest non-ace cards' suits
        scored_tie_break = tie_break(self.scored_cards, other.scored_cards)
        if scored_tie_break is not None:
            return scored_tie_break
        unscored_tie_break = tie_break(self.unscored_cards, other.unscored_cards)
        return unscored_tie_break


def tie_break(cards: list["Card"], other_cards: list["Card"]) ->  bool | None:
    """Break ties between poker hands of the same type."""
    sorted_cards = sorted(cards, key=Card.sort_key, reverse=True)
    sorted_other_cards = sorted(other_cards, key=Card.sort_key, reverse=True)
    for i, card in enumerate(sorted_cards):
        if card.rank != sorted_other_cards[i].rank:
            return card.rank > sorted_other_cards[i].rank
    return None


def common_rank(cards: list[Card], ranks: Counter, rank_count: int) -> tuple[list[Card], list[Card]]:
    """Separate the most common ranked cards from the rest and return both lists, if there are rank_count of them."""
    unmatched_cards = list(cards)
    matched_cards = []
    most_common_rank = ranks.most_common(1)[0]
    if most_common_rank[1] != rank_count:
        return ([], cards)
    for card in cards:
        if card.rank == most_common_rank[0]:
            matched_cards.append(card)
            unmatched_cards.remove(card)
    return (matched_cards, unmatched_cards)


def pair(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a pair."""
    return common_rank(hand.cards, hand.ranks, 2)


def two_pair(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if a hand is two pairs."""
    pair, remainder = common_rank(hand.cards, hand.ranks, 2)
    second_pair, remainder = common_rank(remainder, Counter([card.rank for card in remainder]), 2)
    if len(pair) == 2 and len(second_pair) == 2:
        return (pair + second_pair, remainder)
    return ([], hand.cards)


def three_ofa_kind(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a three of a kind."""
    return common_rank(hand.cards, hand.ranks, 3)


def ace_low_straight(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight."""
    if set(hand.ranks) == {2, 3, 4, 5, 14}:
        return (hand.cards, [])
    return ([], hand.cards)


def straight(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight."""
    low_card_rank = hand.cards[0].rank
    rank_series = {rank - low_card_rank for rank in hand.ranks}
    if rank_series == {0, 1, 2, 3, 4}:
        return (hand.cards, [])
    return ([], hand.cards)


def flush(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is a flush."""
    if hand.flush:
        return (hand.cards, [])
    return ([], hand.cards)


def full_house(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is a full house."""
    if list(hand.ranks.values()) == [3, 2]:
        return common_rank(hand.cards, hand.ranks, 3)
    return ([], hand.cards)


def four_ofa_kind(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is a four of a kind."""
    return common_rank(hand.cards, hand.ranks, 4)


def ace_low_straight_flush(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight flush."""
    if hand.flush and set(hand.ranks) == {2, 3, 4, 5, 14}:
        return (hand.cards, [])
    return ([], hand.cards)


def straight_flush(hand: Parsed_Hand) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight flush."""
    low_card_rank = hand.cards[0].rank
    rank_series = {rank - low_card_rank for rank in hand.ranks}
    if hand.flush and rank_series == {0, 1, 2, 3, 4}:
        return (hand.cards, [])
    return ([], hand.cards)

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

POKER_HANDS = {
    straight_flush: 9,
    ace_low_straight_flush: 8,
    four_ofa_kind: 7,
    full_house: 6,
    flush: 5,
    straight: 4,
    ace_low_straight: 3,
    three_ofa_kind: 2,
    two_pair: 1,
    pair: 0
}

def best_hands(raw_hands: list[str]) -> list[str]:
    """Choose the best hand from a list of poker hands."""
    hands = []
    for hand in raw_hands:
        cards = [Card(card) for card in hand.split(" ")]
        hands.append(Hand(cards))

    highest_hands = [hands[0]]
    highest_hand = hands[0]
    for hand in hands[1:]:
        compare = hand.greater_than_hand(highest_hand)
        if compare is None:
            highest_hands.append(hand)
        elif compare:
            highest_hands = [hand]
            highest_hand = hand

    return [hand.original for hand in highest_hands]

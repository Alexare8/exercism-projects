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


class Hand:
    """A hand of cards fit to the highest possible poker hand."""
    def __init__(self, cards: list[Card]) -> None:
        self.original = " ".join([str(card) for card in cards])
        self.poker_hand = -1
        self.scored_cards = []
        self.unscored_cards = sorted(cards, key=Card.sort_key)
        self.ranks = self.count_ranks()
        self.suits = self.count_suits()
        for poker_hand, value in POKER_HANDS.items():
            scored_cards, unscored_cards = poker_hand(self.unscored_cards, self.ranks, self.suits)
            if scored_cards != []:
                self.poker_hand = value
                self.scored_cards = scored_cards
                self.unscored_cards = unscored_cards
                break

    def __str__(self) -> str:
        return self.original

    def count_ranks(self) -> dict[int, int]:
        ranks = {}
        for card in self.unscored_cards:
            ranks[card.rank] = ranks.get(card.rank, 0) + 1
        return ranks

    def count_suits(self) -> dict[int, int]:
        suits = {}
        for card in self.unscored_cards:
            suits[card.suit] = suits.get(card.suit, 0) + 1
        return suits

    def greater_than_hand(self, other: "Hand") -> bool | None:
        """Determine if a this hand is higher scoring than another."""
        if self.poker_hand != other.poker_hand:
            return self.poker_hand > other.poker_hand
        if self.poker_hand in {3, 8}: #Ace low straights special tie break
            return self.scored_cards[-2] > other.scored_cards[-2] # Compare the highest non-ace cards' suits
        if self.poker_hand == 6: #Full House special tie break
            return full_house_tie_break(self.ranks, other.ranks)
        scored_tie_break = tie_break(self.scored_cards, other.scored_cards)
        if scored_tie_break is not None:
            return scored_tie_break
        unscored_tie_break = tie_break(self.unscored_cards, other.unscored_cards)
        return unscored_tie_break


def full_house_tie_break(cards_ranks: dict[int, int], other_cards_ranks: dict[int, int]) -> bool:
    """Break ties between full houses."""
    triple_rank = next(rank for rank in cards_ranks if cards_ranks[rank] == 3)
    triple_other_rank = next(rank for rank in other_cards_ranks if other_cards_ranks[rank] == 3)
    return triple_rank > triple_other_rank


def tie_break(cards: list["Card"], other_cards: list["Card"]) -> bool | None:
    """Break ties between poker hands of the same type."""
    sorted_cards = sorted(cards, key=Card.sort_key, reverse=True)
    sorted_other_cards = sorted(other_cards, key=Card.sort_key, reverse=True)
    for i, card in enumerate(sorted_cards):
        if card.rank != sorted_other_cards[i].rank:
            return card.rank > sorted_other_cards[i].rank
    return None


def pair(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a pair."""
    unscored_cards = list(cards)
    scored_cards = []
    for rank, rank_count in ranks.items():
        if rank_count == 2:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
    if len(scored_cards) == 2:
        return (scored_cards, unscored_cards)
    return ([], cards)


def two_pair(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is two pairs."""
    unscored_cards = list(cards)
    scored_cards = []
    for rank, rank_count in ranks.items():
        if rank_count == 2:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
    if len(scored_cards) == 4:
        return (scored_cards, unscored_cards)
    return ([], cards)


def three_ofa_kind(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a three of a kind."""
    unscored_cards = list(cards)
    scored_cards = []
    for rank, rank_count in ranks.items():
        if rank_count == 3:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
            return (scored_cards, unscored_cards)
    return ([], cards)


def ace_low_straight(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight."""
    if set(ranks) == {2, 3, 4, 5, 14}:
        return (cards, [])
    return ([], cards)


def straight(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight."""
    low_card_rank = cards[0].rank
    rank_series = {rank - low_card_rank for rank in ranks}
    if rank_series == {0, 1, 2, 3, 4}:
        return (cards, [])
    return ([], cards)


def flush(cards: list[Card], _: dict[int, int], suits: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a flush."""
    if suits[cards[0].suit] == 5:
        return (cards, [])
    return ([], cards)


def full_house(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a full house."""
    if len(ranks) == 2 and ranks[cards[0].rank] in {2, 3}:
        return (cards, [])
    return ([], cards)


def four_ofa_kind(cards: list[Card], ranks: dict[int, int], _: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a four of a kind."""
    unscored_cards = list(cards)
    if len(ranks) == 2 and ranks[cards[0].rank] in {1, 4}:
        for card in unscored_cards:
            if ranks[card.rank] == 1:
                unscored_cards.remove(card)
                return (unscored_cards, [card])
    return ([], unscored_cards)


def ace_low_straight_flush(cards: list[Card], ranks: dict[int, int], suits: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight flush."""
    if suits[cards[0].suit] == 5 and set(ranks) == {2, 3, 4, 5, 14}:
        return (cards, [])
    return ([], cards)


def straight_flush(cards: list[Card], ranks: dict[int, int], suits: dict[int, int]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight flush."""
    low_card_rank = cards[0].rank
    rank_series = {rank - low_card_rank for rank in ranks}
    if rank_series == {0, 1, 2, 3, 4} and suits[cards[0].suit] == 5:
        return (cards, [])
    return ([], cards)


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

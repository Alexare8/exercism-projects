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

    def __gt__(self, other) -> bool:
        if self.rank > other.rank:
            return True
        if self.rank < other.rank:
            return False
        if self.suit > other.suit:
            return True
        return False

    def __lt__(self, other) -> bool:
        if self.rank < other.rank:
            return True
        if self.rank > other.rank:
            return False
        if self.suit < other.suit:
            return True
        return False

    def __ge__(self, other) -> bool:
        return not self < other

    def __le__(self, other) -> bool:
        return not self > other

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
        for i, poker_hand in enumerate(POKER_HANDS):
            scored_cards, unscored_cards = poker_hand(cards)
            if scored_cards != []:
                self.poker_hand = i
                self.scored_cards = sorted(scored_cards, key=Card.sort_key)
                self.unscored_cards = sorted(unscored_cards, key=Card.sort_key)

    def __str__(self) -> str:
        return self.original

    def greater_than_hand(self, other: "Hand") -> bool | None:
        """Determine if a this hand is higher scoring than another."""
        if self.poker_hand != other.poker_hand:
            return self.poker_hand > other.poker_hand
        if self.poker_hand in {3, 8}: #Ace low straights special tie break
            return self.scored_cards[-2] > other.scored_cards[-2] # Compare the highest non-ace cards' suits
        if self.poker_hand == 6: #Full House special tie break
            return full_house_tie_break(self.scored_cards, other.scored_cards)
        scored_tie_break = tie_break(self.scored_cards, other.scored_cards)
        if scored_tie_break is not None:
            return scored_tie_break
        unscored_tie_break = tie_break(self.unscored_cards, other.unscored_cards)
        return unscored_tie_break


def full_house_tie_break(cards: list["Card"], other_cards: list["Card"]) -> bool:
    """Break ties between full houses."""
    ranks = [card.rank for card in cards]
    highest_rank = next(rank for rank in ranks if ranks.count(rank) == 3)
    other_ranks = [card.rank for card in other_cards]
    highest_other_rank = next(rank for rank in other_ranks if other_ranks.count(rank) == 3)
    return highest_rank > highest_other_rank



def tie_break(cards: list["Card"], other_cards: list["Card"]) -> bool | None:
    """Break ties between poker hands of the same type."""
    sorted_cards = sorted(cards, key=Card.sort_key)
    sorted_other_cards = sorted(other_cards, key=Card.sort_key)
    sorted_cards.reverse()
    sorted_other_cards.reverse()
    for i, card in enumerate(sorted_cards):
        if card.rank != sorted_other_cards[i].rank:
            return card.rank > sorted_other_cards[i].rank
    return None


def pair(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a pair."""
    unscored_cards = list(cards)
    scored_cards = []
    ranks = [card.rank for card in cards]
    for rank in set(ranks):
        if ranks.count(rank) == 2:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
    if len(scored_cards) == 2:
        return (scored_cards, unscored_cards)
    return ([], cards)


def two_pair(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is two pairs."""
    unscored_cards = list(cards)
    scored_cards = []
    ranks = [card.rank for card in cards]
    for rank in set(ranks):
        if ranks.count(rank) == 2:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
    if len(scored_cards) == 4:
        return (scored_cards, unscored_cards)
    return ([], cards)


def three_ofa_kind(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if a hand is a three of a kind."""
    unscored_cards = list(cards)
    scored_cards = []
    ranks = [card.rank for card in cards]
    for rank in set(ranks):
        if ranks.count(rank) == 3:
            for card in cards:
                if card.rank == rank:
                    scored_cards.append(card)
                    unscored_cards.remove(card)
            return (scored_cards, unscored_cards)
    return ([], cards)


def ace_low_straight(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight."""
    cards = sorted(cards, key=Card.sort_key)
    ranks = [card.rank for card in cards]
    if ranks == [2, 3, 4, 5, 14]:
        return (cards, [])
    return ([], cards)


def straight(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight."""
    cards = sorted(cards, key=Card.sort_key)
    low_card_rank = cards[0].rank
    rank_series = [card.rank - low_card_rank for card in cards]
    if rank_series == [0, 1, 2, 3, 4]:
        return (cards, [])
    return ([], cards)


def flush(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a flush."""
    suits = [card.suit for card in cards]
    if suits.count(suits[0]) == 5:
        return (cards, [])
    return ([], cards)


def full_house(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a full house."""
    ranks = [card.rank for card in cards]
    ranks_set = set(ranks)
    if len(ranks_set) == 2 and ranks.count(ranks[0]) in {2, 3}:
        return (cards, [])
    return ([], cards)


def four_ofa_kind(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a four of a kind."""
    ranks = [card.rank for card in cards]
    ranks_set = set(ranks)
    if len(ranks_set) == 2 and ranks.count(ranks[0]) in {1, 4}:
        for card in cards:
            if ranks.count(card.rank) == 1:
                cards.remove(card)
                return (cards, [card])
    return ([], cards)


def ace_low_straight_flush(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is an ace low straight flush."""
    suits = [card.suit for card in cards]
    if suits.count(suits[0]) == 5:
        cards = sorted(cards, key=Card.sort_key)
        ranks = [card.rank for card in cards]
        if ranks == [2, 3, 4, 5, 14]:
            return (cards, [])
    return ([], cards)


def straight_flush(cards: list[Card]) -> tuple[list[Card], list[Card]]:
    """Check if hand is a straight flush."""
    suits = [card.suit for card in cards]
    if suits.count(suits[0]) == 5:
        cards = sorted(cards, key=Card.sort_key)
        low_card_rank = cards[0].rank
        rank_series = [card.rank - low_card_rank for card in cards]
        if rank_series == [0, 1, 2, 3, 4]:
            return (cards, [])
    return ([], cards)


POKER_HANDS = (pair, two_pair, three_ofa_kind, ace_low_straight, straight, flush, full_house, four_ofa_kind, ace_low_straight_flush, straight_flush)


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

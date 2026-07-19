from functools import cached_property


class Allergies:
    """Interpret the allergy score of an individual."""
    ALLERGENS = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8, 'tomatoes': 16, 'chocolate': 32, 'pollen': 64, 'cats': 128}

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """Determine if a given allergy is present."""
        return bool(self.ALLERGENS[item] & self.score)

    @cached_property
    def lst(self) -> list[str]:
        """List all indicated allergies."""
        return [allergen for allergen in self.ALLERGENS if self.allergic_to(allergen)]

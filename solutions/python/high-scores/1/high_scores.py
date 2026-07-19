class HighScores:
    def __init__(self, scores: list[int]) -> int:
        self.scores = scores

    def latest(self) -> int:
        return self.scores[-1]

    def personal_best(self) -> list[int]:
        return sorted(self.scores, reverse=True)[0]

    def personal_top_three(self) -> list[int]:
        return sorted(self.scores, reverse=True)[:3]


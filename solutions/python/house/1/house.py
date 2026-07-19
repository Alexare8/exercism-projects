characters = ["the house that Jack built.", 
              "the malt that lay in ",
              "the rat that ate ",
              "the cat that killed ",
              "the dog that worried ",
              "the cow with the crumpled horn that tossed ",
              "the maiden all forlorn that milked ",
              "the man all tattered and torn that kissed ",
              "the priest all shaven and shorn that married ",
              "the rooster that crowed in the morn that woke ",
              "the farmer sowing his corn that kept ",
              "the horse and the hound and the horn that belonged to "
              ]


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Returns a series of verses form the nursury rhyme 'This is the House that Jack Built'"""
    def assemble_verse(verse_number: int) -> str:
        verse = ""
        for i in range(verse_number):
            verse = characters[i] + verse
        return "This is " + verse

    return [assemble_verse(verse_number) for verse_number in range(start_verse, end_verse + 1)]
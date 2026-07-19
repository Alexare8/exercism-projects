module MagicianInTraining exposing (..)

import Array exposing (Array)


type alias Deck =
    Array Int


getCard : Int -> Deck -> Maybe Int
getCard =
    Array.get


setCard : Int -> Int -> Deck -> Deck
setCard =
    Array.set


addCard : Int -> Deck -> Deck
addCard =
    Array.push


removeCard : Int -> Deck -> Deck
removeCard index deck =
    Array.append
        (Array.slice 0 index deck)
        (Array.slice (index + 1) (Array.length deck) deck)


evenCardCount : Deck -> Int
evenCardCount deck =
    let
        isEven num =
            modBy 2 num == 0
    in
    Array.length (Array.filter isEven deck)

module RolePlayingGame exposing (Player, castSpell, introduce, revive)

import Maybe

type alias Player =
    { name : Maybe String
    , level : Int
    , health : Int
    , mana : Maybe Int
    }


introduce : Player -> String
introduce { name } =
    Maybe.withDefault "Mighty Magician" name


revive : Player -> Maybe Player
revive player =
    let
        mana = if player.level >= 10 then
                Just 100
            else
                Nothing
    in
    if player.health == 0 then
        Just { player | health = 100, mana = mana }
    else
        Nothing


castSpell : Int -> Player -> ( Player, Int )
castSpell manaCost player =
    case player.mana of 
        Nothing ->
            ({ player | health = max (player.health - manaCost) 0 }, 0)
        Just mana ->
            let
                manaSpent = 
                    if manaCost > mana then
                        0
                    else
                        manaCost
                damage = manaSpent * 2
            in
            ({ player | mana = Just (mana - manaSpent) }, damage)

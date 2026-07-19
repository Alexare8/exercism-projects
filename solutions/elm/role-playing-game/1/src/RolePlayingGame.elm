module RolePlayingGame exposing (Player, castSpell, introduce, revive)


type alias Player =
    { name : Maybe String
    , level : Int
    , health : Int
    , mana : Maybe Int
    }


introduce : Player -> String
introduce { name } =
    case name of
        Nothing ->
            "Mighty Magician"

        Just someName ->
            someName


revive : Player -> Maybe Player
revive player =
    case player.health of
        0 ->
            case player.level >= 10 of
                True ->
                    Just { player | health = 100, mana = Just 100 }

                False ->
                    Just { player | health = 100 }

        _ ->
            Nothing


castSpell : Int -> Player -> ( Player, Int )
castSpell manaCost player =
    case player.mana of
        Nothing ->
            case player.health > manaCost of
                True ->
                    ( { player | health = player.health - manaCost }, 0 )

                False ->
                    ( { player | health = 0 }, 0 )

        Just manaPool ->
            case manaPool >= manaCost of
                True ->
                    ( { player | mana = Just (manaPool - manaCost) }, manaCost * 2 )

                False ->
                    ( player, 0 )

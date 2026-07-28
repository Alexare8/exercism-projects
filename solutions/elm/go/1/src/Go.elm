module Go exposing (..)

import GoSupport exposing (..)


applyRules : Game -> Rule -> NonValidatingRule -> Rule -> Rule -> Game
applyRules game oneStonePerPointRule captureRule libertyRule koRule =
    case oneStonePerPointRule game of
        Err msg_one ->
            { game | error = msg_one }

        Ok game_one_rule ->
            case libertyRule (captureRule game_one_rule) of
                Err msg_two ->
                    { game | error = msg_two }

                Ok game_three_rules ->
                    case koRule game_three_rules of
                        Err msg_three ->
                            { game | error = msg_three }

                        Ok game_four_rules ->
                            changePlayer game_four_rules

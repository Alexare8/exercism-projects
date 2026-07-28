module Go exposing (..)

import GoSupport exposing (..)


applyRules : Game -> Rule -> NonValidatingRule -> Rule -> Rule -> Game
applyRules game oneStonePerPointRule captureRule libertyRule koRule =
    case oneStonePerPointRule game of
        Err msgOne ->
            { game | error = msgOne }

        Ok gameOneRule ->
            case libertyRule (captureRule gameOneRule) of
                Err msgTwo ->
                    { game | error = msgTwo }

                Ok gameThreeRules ->
                    case koRule gameThreeRules of
                        Err msgThree ->
                            { game | error = msgThree }

                        Ok gameFourRules ->
                            changePlayer gameFourRules

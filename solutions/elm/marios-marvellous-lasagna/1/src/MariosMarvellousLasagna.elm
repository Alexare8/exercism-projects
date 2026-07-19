module MariosMarvellousLasagna exposing (remainingTimeInMinutes)

remainingTimeInMinutes : Int -> Int -> Int
remainingTimeInMinutes numLayers elapsedMinutes = 
    let
        expectedMinutesInOven = 40

        preparationTimeInMinutes : Int -> Int
        preparationTimeInMinutes layers = 
            layers * 2
    in
        (preparationTimeInMinutes numLayers)
        + expectedMinutesInOven 
        - elapsedMinutes


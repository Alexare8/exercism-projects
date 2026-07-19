module MariosMarvellousLasagna exposing (remainingTimeInMinutes)

remainingTimeInMinutes : Int -> Int -> Int
remainingTimeInMinutes numLayers elapsedMinutes = 
    let
        expectedMinutesInOven : Int
        expectedMinutesInOven = 40

        preparationTimeInMinutes : Int
        preparationTimeInMinutes = 
            numLayers * 2
    in
        preparationTimeInMinutes
        + expectedMinutesInOven 
        - elapsedMinutes


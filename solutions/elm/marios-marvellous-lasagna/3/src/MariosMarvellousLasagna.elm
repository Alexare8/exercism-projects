module MariosMarvellousLasagna exposing (remainingTimeInMinutes)

remainingTimeInMinutes : Int -> Int -> Int
remainingTimeInMinutes numLayers numMinutesSinceStart =
    let 
        expectedMinutesInOven = 40
        preparationTimeInMinutes = numLayers * 2
    in
        preparationTimeInMinutes + expectedMinutesInOven - numMinutesSinceStart
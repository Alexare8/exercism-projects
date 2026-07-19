module LuciansLusciousLasagna exposing (elapsedTimeInMinutes, expectedMinutesInOven, preparationTimeInMinutes)


expectedMinutesInOven : Int
expectedMinutesInOven =
    40


preparationTimeInMinutes : Int -> Int
preparationTimeInMinutes numLayers =
    2 * numLayers


elapsedTimeInMinutes : Int -> Int -> Int
elapsedTimeInMinutes numLayers timeInOven =
    (preparationTimeInMinutes numLayers) + timeInOven

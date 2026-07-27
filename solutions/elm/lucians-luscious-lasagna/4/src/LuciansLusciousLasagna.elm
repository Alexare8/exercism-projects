module LuciansLusciousLasagna exposing (elapsedTimeInMinutes, expectedMinutesInOven, preparationTimeInMinutes)

expectedMinutesInOven = 40
preparationTimeInMinutes numLayers = numLayers * 2
elapsedTimeInMinutes numLayers minutesInOven = minutesInOven + preparationTimeInMinutes numLayers
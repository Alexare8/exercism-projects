module SqueakyClean exposing (clean, clean1, clean2, clean3, clean4)

import Char
import List
import String


clean1 : String -> String
clean1 =
    String.replace " " "_"


clean2 : String -> String
clean2 str =
    String.replace
        "\t"
        "[CTRL]"
        (String.replace
            "\u{000D}"
            "[CTRL]"
            (String.replace "\n" "[CTRL]" (clean1 str))
        )


cap : String -> String
cap subString =
    case String.uncons subString of
        Just ( c, s ) ->
            String.cons (Char.toUpper c) s

        Nothing ->
            ""


clean3 : String -> String
clean3 str =
    case String.split "-" (clean2 str) of
        x :: xs ->
            String.concat (x :: List.map cap xs)

        _ ->
            ""


clean4 : String -> String
clean4 =
    clean3 >> String.filter (Char.isDigit >> not)


clean : String -> String
clean =
    clean4 >> String.filter (\chr -> chr < 'α' || chr > 'ω')

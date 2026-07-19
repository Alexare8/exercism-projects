module SqueakyClean exposing (clean, clean1, clean2, clean3, clean4)
import String
import Char exposing (toUpper, isDigit, toCode)
import List exposing (map)

clean1 : String -> String
clean1 str =
    String.replace " " "_" str


clean2 : String -> String
clean2 str =
    String.replace 
        "\t"
        "[CTRL]"
        (String.replace
            "\r"
            "[CTRL]"
            (String.replace "\n" "[CTRL]" (clean1 str)))


clean3 : String -> String
clean3 str =
    let
        cap : String -> String
        cap subString = 
            case String.uncons subString of
            Just (c, s) ->
                 String.cons (Char.toUpper c) s
            Nothing ->
                ""
    in
        case String.split "-" (clean2 str) of
            x :: xs ->
                String.concat ([x] ++ (List.map cap xs))
            _ ->
                ""


clean4 : String -> String
clean4 str =
    let
        isntDigit character = not (Char.isDigit character)
    in
        String.filter isntDigit (clean3 str)


clean : String -> String
clean str =
    String.filter (\c -> Char.toCode c < 0x03B1 || Char.toCode c > 0x03C9) (clean4 str)

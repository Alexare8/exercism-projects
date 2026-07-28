module Secrets exposing (clearBits, decrypt, flipBits, setBits, shiftBack)

import Bitwise


shiftBack : Int -> Int -> Int
shiftBack =
    Bitwise.shiftRightZfBy


setBits : Int -> Int -> Int
setBits =
    Bitwise.or


flipBits : Int -> Int -> Int
flipBits =
    Bitwise.xor


clearBits : Int -> Int -> Int
clearBits mask value =
    Bitwise.and (Bitwise.complement mask) value


decrypt : Int -> Int
decrypt secret =
    clearBits 17 (shiftBack 5 (flipBits 2009 (setBits 1996 secret)))

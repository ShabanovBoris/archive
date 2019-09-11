module Main where

import System.IO
import System.Environment (getArgs)
import Control.Monad

fun1 :: Int -> [String] -> [Double]
fun1 n _
    | n <= 0 = []
fun1 _ [] = []
fun1 n (x:xs) = a : fun1 (n - 1) xs
    where a = read x + 0.0
    
fun2 :: (Num i, Ord i) => i -> [Double] -> [Int]
fun2 n _
    | n <= 0 = []
fun2 _ [] = []
fun2 n (x:xs) = if (d == 0) && (x > 0) then truncate x : fun2 (n - 1) xs else fun2 (n - 1) xs
    where d = x - fromIntegral (truncate x)


fun3 :: (Num i, Ord i) => i -> [Int] -> [String]
fun3 n _
    | n <= 0 = []
fun3 _ [] = []
fun3 n (x:xs) = a : fun3 (n - 1) xs
    where a = show x


main = do
    [file1, file2] <- getArgs
    text1 <- readFile file1
    let lines1 = lines text1
        l2 = fun1 (length lines1) lines1
        l3 = map (sqrt) l2
        l4 = fun2 (length l3) l3
        l5 = fun3 (length l4) l4
    writeFile file2 (show l5)
    print(l4)
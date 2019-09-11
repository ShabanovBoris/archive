module Main where
 
import System.IO
import System.Environment (getArgs)
import Control.Monad
 
main = do
    [file1, file2] <- getArgs
    text1 <- readFile file1
    text2 <- readFile file2
    let lines1 = lines text1
        lines2 = lines text2
    forM_ (zip lines1 lines2) $ \ (l1, l2) -> do
        when (l1 /= l2 ) $ do
            putStrLn l1
            putStrLn l2
import System.IO      (hSetBuffering,stdout,BufferMode(NoBuffering))
import System.Random  (randomRIO)
import Control.Monad  (when)
 
bulls_and_cows :: Int -> Int -> Int
bulls_and_cows n1 n2 = length $ filter (`elem` s2) s1
           where s1=show n1
                 s2=show n2
 
bulls :: Int -> Int -> Int
bulls n1 n2 = length $ filter (uncurry (==)) z
           where z=zip (show n1) (show n2)
 
game :: Int -> IO ()
game n1 = do
  putStr "Enter 4-Number : "
  n2 <- readLn 
  result n1 n2 
  if (bulls n1 n2 == 4) then putStrLn "You won!" else (putStrLn "Try away!" >> game n1)
 
result :: Int -> Int -> IO ()
result n1 n2 = do
  putStrLn $ "Cows : " ++ show ((bulls_and_cows n1 n2) - (bulls n1 n2)) 
  putStrLn $ "Bulls : " ++ show (bulls n1 n2)
 
main = do
  hSetBuffering stdout NoBuffering
  n1 <- randomRIO(1111, 9999)
  print(n1)
  game n1
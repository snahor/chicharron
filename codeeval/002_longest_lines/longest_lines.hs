import System.Environment (getArgs)

import Data.List (sortBy)

compareByLengthDesc x y 
  | length x < length y = GT
  | length x > length y = LT
  | length x == length y = EQ

main = do
  args <- getArgs
  input <- readFile (args !! 0)
  let num:words = lines input
  mapM_ putStrLn $ take (read num :: Int) (sortBy compareByLengthDesc words)

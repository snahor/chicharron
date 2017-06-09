import System.Environment (getArgs)

import Data.List (intercalate)
import Data.List.Split (splitOn)

reverseWords = intercalate " " . reverse . splitOn " "

main = do
  args <- getArgs
  input <- readFile (args !! 0)
  mapM_ putStrLn $ map reverseWords (lines input)

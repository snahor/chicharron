import System.Environment (getArgs)
import Data.List (intercalate)

split = foldr splitter []
  where
    splitter ' ' acc = []:acc
    splitter c   []  = [[c]]
    splitter c   (xs:xss) = (c:xs):xss

reverseWords = intercalate " ". reverse . split

main = do
  args <- getArgs
  input <- readFile (args !! 0)
  mapM_ putStrLn $ map reverseWords (lines input)

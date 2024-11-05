module Main where

import Control.Monad (replicateM_)
import qualified Data.Set  as S

solve :: Int -> Int -> Maybe [Int]
solve n k = go S.empty [] [1 .. n]
  where
    go _ acc [] = Just $ reverse acc
    go used acc (x : xs)
        | x - k >= 1
            && (x - k) `S.notMember` used =
            go (S.insert (x - k) used) (x - k : acc) xs
        | x + k <= n
            && (x + k) `S.notMember` used =
            go (S.insert (x + k) used) (x + k : acc) xs
        | otherwise = Nothing

main :: IO ()
main = do
    cases <- readLn :: IO Int
    replicateM_ cases $ do
        [n, k] <- map read . words <$> getLine :: IO [Int]
        case solve n k of
            Just ps -> putStrLn $ unwords $ map show ps
            Nothing -> putStrLn "-1"

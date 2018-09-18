-- even fibb numbers
mfib = (map fib' [0..] !!)
    where fib' 0 = 1
          fib' 1 = 1
          fib' n = mfib (n - 1) + mfib (n - 2)

main :: IO()
main = putStrLn $ show $ sum $ [a | a <- map mfib [1..100], a < 4000000 && even a]
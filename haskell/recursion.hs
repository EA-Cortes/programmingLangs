isqrt :: Integral i => i -> i
isqrt = floor . sqrt . fromIntegral

isPrime n = ip n [2..(isqrt n)]
 where
  ip _ [] = True
  ip n (x:xs)
   | mod n x == 0 = False
   | otherwise = ip n xs


factorial n = go n 1
 where
 go n ret
  | n > 1 = go (n-1) (ret*n)
  | otherwise = ret

-- fibonacci 0 = 0
-- fibonacci 1 = 1
-- fibonacci n = ( fibonacci(n-1) + fibonacci(n-2) ) 


fibonacci n = go n 1
 where
  go n ret
   | n == 0 = 0
   | n == 1 = 1
   | n > 2 = fibonacci(n-1) +fibonacci(n-2)
   | otherwise = ret

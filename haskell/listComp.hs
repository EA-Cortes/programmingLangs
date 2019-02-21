filter1 n = ( odd n || mod n 5 == 4 ) || n > 50
resData = [x | x <- [1..100], filter1 x]

div5 n = (mod n 5 == 0)
multipleOf5 n = [x | x <- [1..n], div5 x]

div7or11 n = (mod n 7 == 0 || mod n 11 == 0)
multipleOf7Or11 n = [x | x <- [1..n], div7or11 x] 

div3And7 n = (mod n 3 == 0 && mod n 7 == 0)
multipleOf3And7 n = [x | x <- [1..n], div3And7 x] 
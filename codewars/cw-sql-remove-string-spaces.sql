-- CodeWars
-- 8th Kyu
-- Remove String Spaces
-- # write your SQL statement here: you are given a table 'nospace' with column 'x', return a table with column 'x' and your result in a column named 'res'.

select x  -- the original column
  , replace(x, ' ','') as res  --remove blank spaces, rename as res
from nospace;
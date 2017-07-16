tot = 0
a = 1, b = 1, c = 2, tmp = 0

while(c < 4000000) do
    tot += c if(c%2 == 0)
    
    tmp = c
    a = b
    b = c
    c=a+b
end

puts tot
i = 2520

def isDevisable(num)
    11.upto(20) do |j|
        return false if(num%j != 0)
    end
    return true
end

while true do
    break if(isDevisable(i))
    i+=2520
end

puts i

//232792560
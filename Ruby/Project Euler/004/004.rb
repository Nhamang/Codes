result = 0, found = false
maxPal = -1

def isPalindrome(test)
    return test.to_s == test.to_s.reverse
end

999.downto(99).each do |i|
    999.downto(99).each do |j|
        maxPal = (i*j) if(isPalindrome(i*j) && ((i*j) > maxPal)) 
    end
end
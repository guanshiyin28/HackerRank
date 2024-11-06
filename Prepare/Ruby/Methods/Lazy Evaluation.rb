def prime?(x)
    return false if x < 2
    
    checker = Math.sqrt(x).to_i # 4
    2.upto(checker).each {|i| return false if x % i == 0 }
    
    true
end

palindrom_array = -> (array_size) do
    2.upto(Float::INFINITY).lazy.select do |x| 
        prime?(x) && x.digits.join.to_i == x
    end.first(array_size.to_i)
end

N = gets
print palindrom_array.(N)

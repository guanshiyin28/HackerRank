def factorial(n)
    total = n
    for i in 1...n do
        total *= i
    end
    
    yield total
end

n = gets.to_i
factorial(n) do |num| 
    puts num
end

combination = ->(n) do
    ->(r) do
        return 1 if r == 0 || r == n
        return 0 if r > n || r < 0
        (1..r).reduce(1) { |product, i| product * (n - i + 1) / i }
    end
end

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)

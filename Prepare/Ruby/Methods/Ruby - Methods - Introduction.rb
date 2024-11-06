# Your code here
def prime?(num)
  return false if num <= 1
  (2..Math.sqrt(num).to_i).none? { |n| num % n == 0 }
end

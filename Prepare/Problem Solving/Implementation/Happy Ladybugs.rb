#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b)
    return "NO" if b.length == 1 and b[0] != "_"
    return "YES" if 0.upto(b.length-1).all? {|i| b[i] == b[i+1] or b[i-1]==b[i] }       
    return "YES" if b.chars.tally.all? { |i,j| i == "_" or j > 1 } and b.include?("_")  
    return "NO"
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

g = gets.strip.to_i

g.times do |g_itr|
    n = gets.strip.to_i

    b = gets.chomp

    result = happyLadybugs b

    fptr.write result
    fptr.write "\n"
end

fptr.close()

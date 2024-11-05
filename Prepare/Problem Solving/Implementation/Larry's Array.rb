#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(a)
    a_sorted = a.sort
    (a.length-2).times do |i|
        index = a.find_index(i+1)
        if (index - i) % 2 == 0
            a.insert(i, a.delete_at(index))   
        else
            a.insert(i,a.delete_at(index))
            a[i+1], a[i+2] = a[i+2], a[i+1]
        end            
    end
    return "YES" if a == a_sorted
    return "NO"
end


fptr = File.open(ENV['OUTPUT_PATH'], 'w')

t = gets.strip.to_i

t.times do |t_itr|
    n = gets.strip.to_i

    A = gets.rstrip.split.map(&:to_i)

    result = larrysArray A

    fptr.write result
    fptr.write "\n"
end

fptr.close()

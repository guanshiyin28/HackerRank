Fixnum = Integer
Bignum = Integer

def sum_terms(n)
    1.upto(n).inject(0) {|sum, n| sum + n**2 + 1} 
end

# Your code here
def serial_average(str)
    num1, num2, num3 = str.split("-")
    avg = ((num2.to_f+num3.to_f)/2).round(2)
    ans = "#{num1}-#{avg}"
    return ans
end

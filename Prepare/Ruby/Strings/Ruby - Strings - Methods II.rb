# Enter your code here
def strike(string)
    "<strike>#{string}</strike>"    
end

def mask_article(string, words_arr)
    words_arr.each do |word|
        string.gsub!(word, strike(word))
    end
    string
end

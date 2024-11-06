def rot13(secret_messages)
    secret_messages.map do |str|
        str.chars.map{|char| char.ord.between?(65,90) || char.ord.between?(97,122) ? cipher(char) : char }.join
    end
end

def cipher(char)
    13.times {char.next!}
    return char.size > 1 ? char[1] : char
end

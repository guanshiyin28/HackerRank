if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command = input().split()
        
        # Handle 'print' command separately
        if command[0] == "print":
            print(my_list)
        else:
            # Dynamically get the method from my_list using getattr
            method = getattr(my_list, command[0])
            
            # If the command has additional arguments, convert them to integers
            if len(command) > 1:
                # Convert arguments to integers
                args = list(map(int, command[1:]))
                # Unpack the arguments and pass to the method
                method(*args)
            else:
                method()  # Call the method with no arguments

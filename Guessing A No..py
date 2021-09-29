def Play_Game():
    class Error(Exception):
        """Base Class for other exceptions"""
        pass


    class vtse(Error):
        """Raised when the input value is too small"""
        pass


    class vtle(Error):
        """Raised when the input value is too small"""
        pass


    num = 0
    print('Guessing A Number')

    while True:
        try:
            i_num = float(input('enter a no.: '))
            if i_num < num:
                raise vtse
            elif i_num > num:
                raise vtle
            break
        except vtse:
            print('This value is too small, try again!')
        except vtle:
            print('This value is too large, try again!')

    print('You Guessed it correctly. •_•')

#MAIN
choice = int(input(""))
def check_vowel_const(character):
    '''
    Checks Weather Character is Vowel or Constant
    :param character: str
    :return: None
    '''
    if character in ['a', 'e', 'i', 'o', 'u']:
        print("Given Character is vowel")
    else:
        print("Given character is Constant")


if __name__ == '__main__':
    character = input("Enter a Character : ")
    check_vowel_const(character)



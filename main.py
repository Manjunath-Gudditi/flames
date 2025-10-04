def main():
    your_name = input("Enter Your Name: ")
    crush_name = input("Enter Crush Name: ")
    
    your_name_letters_dict = dict()
    for letter in your_name:
        your_name_letters_dict[letter] = your_name_letters_dict.get(letter, 0) + 1

    crush_name_letters_dict = dict()
    for letter in crush_name:
        crush_name_letters_dict[letter] = crush_name_letters_dict.get(letter, 0) + 1      
    
    # Strike off common letters
    for letter in your_name_letters_dict:
        if letter in crush_name_letters_dict:
            your_name_letters_dict[letter] = 0
            crush_name_letters_dict[letter] = 0
    
    # count total number of left over letters from both names
    count_of_left_over_letters = 0
    for letter in your_name_letters_dict:
        count_of_left_over_letters += your_name_letters_dict[letter]
    for letter in crush_name_letters_dict:
        count_of_left_over_letters += crush_name_letters_dict[letter]
        
    flames_list = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames_list) > 1:
        index_to_strike_off = count_of_left_over_letters % len(flames_list)
        if index_to_strike_off == 0:
            index_to_strike_off = len(flames_list) - 1
        else:
            index_to_strike_off -= 1
        flames_list.pop(index_to_strike_off)
    
    full_forms_dict = {
        'F': "Friends",
        'L': "Love",
        'A': "Affectionate",
        'M': "Marriage",
        'E': "Enemies",
        'S': "Siblings",
    }
    print('*'*21, full_forms_dict.get(flames_list[0]).center(21), '*'*21, sep="\n")
    
        
if __name__ == "__main__":
    main()
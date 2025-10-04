# flames
The game of FLAMES


## Game

Your Name: YOUR_NAME
Crush Name: CRUSH_NAME

1. Strike off all common letters from both names.
2. Count left over letters
3. Write FLAMES
    a. keep striking off letters from FLAMES with count obtained from step 2 until you left with 1 letter
4. Whatever letter left - will be the result 
    F = Friends
    L = Love
    A = Affectionate
    M = Marriage
    E = Enemies
    S = Siblings


## Algorithm
1. Take your_name
2. Take crush_name
3. Put letters of your_name with count in dict your_name_letters_dict
4. Put letters of crush_name with count in dict crush_name_letters_dict
5. Iterate over keys(letters) of your_name_letters_dict:
    a. if key(letter) present in crush_name_letters_dict:
        i. set that letter count to 0 in both dicts. # Striking off common letters.
6. Calculate sum of counts of all letters from both dicts # Counting left over letters. # count_of_left_over_letters
7. Create flames_list ['F', 'L', 'A', 'M', 'E', 'S']
8. while flames_list length is > 1:
    a. index_to_strike_off = count_of_left_over_letters % len(flames_list)
    b. if index_to_strike_off == 0: # adjust as python list is 0 indexed.
            index_to_strike_off = len(flames_list) # strike off last letter
       else:
            index_to_strike_off -= 1
    c. flames_list.pop(index_to_strike_off)
9. create full_forms_dict with keys as letters from flames_list - values their full forms # {'F': 'Friends', 'L': 'Love', ...}
10. Print result from left over letter of flames_list fetching full form from full_forms_dict # full_forms_dict.get(flames_list[0])
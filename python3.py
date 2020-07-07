para = ' silent man listen carefully.'
test_list = para.split()
print("The original list : " + str(test_list)) 

anagram_list=[]

for anagram in test_list:
    for anagram2 in test_list: 
        if sorted(anagram)==sorted(anagram2):
            if anagram!=anagram2:
              anagram_list.append(anagram)
print("The anagram list : " + str(anagram_list))  
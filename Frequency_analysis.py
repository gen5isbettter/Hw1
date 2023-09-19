import matplotlib.pyplot as plt
import pandas as pd


with open(r"C:\Users\ianki\Desktop\grad school\Cs578\ciphertext.txt") as f:
    ciphertext = f.read()
    print(ciphertext)

frequency = {}
def char_frequency(str1, dict):
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    return dict

def replace_chars(text, c_freq, reg_freq):
    for i in range(0,23):
        text = text.replace(c_freq[0].iloc[i].lower(), reg_freq["letters"].iloc[i])

    return text


print(char_frequency(ciphertext, frequency))
freq_presort = pd.DataFrame([frequency.keys(), frequency.values()])
freq_presort = freq_presort.T
sorted_freq = freq_presort.sort_values(by = [1], ascending= False)
sorted_freq=sorted_freq.reset_index(drop=True)

#Trim the characters (\n, spaces, hypens, semicolons, etc)

sorted_freq = sorted_freq.drop([0,20,24,26])
sorted_freq=sorted_freq.reset_index(drop=True)

#Get the frequency of each letter in the text

#part a
total = sorted_freq[1].sum()
percentage = []

for i in range(0,23):
    temp = sorted_freq[1].iloc[i]
    a = (temp / total)*100
    a = round(a,2)
    percentage.append(a)

sorted_freq['frequency'] = percentage

#Compare to an actual english letter frequency table

print("--------------Part a-----------------\n")
print(sorted_freq)

#part b
#Swap letters and hope to solve some of the words
#swap 1: H and L
#swap 2: D and S
#swap 3: N and R
#swap 4: L and C
#swap 5: O and I
#swap 6: F and N
#swap 7: L and U
#swap 8: B and Y
#swap 9: B and K
#swap 10: G and F
#swap 11: S and L
#swap 12: D and S
#swap 13: P and V
#swap 14: N and M
#swap 15: N and P
#swap 16: G and I
#swap 17: G and N
#swap 18: G and K

untouched_letters = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V", "K", "X", "Q", "J", "Z"]

letters = ["E", "T", "A", "N", "O", "R", "S", "I", "C", "L", "H", "D", "U", "P", "M", "G", "W", "F", "V", "Y", "K", "B", "X", "Q", "J", "Z"]
usage = [12.02, 9.10, 8.12, 7.68, 7.31, 6.95, 6.28, 6.02, 5.92, 4.32, 3.98, 2.88, 2.71, 2.61, 2.30, 2.11, 2.09, 2.03, 1.82, 1.49, 1.11, 0.69, 0.17, 0.11, 0.10, 0.07]

data = {
    "letters": letters,
    "usage": usage
}

english_letters = pd.DataFrame(data)

#Replace letters from the actual english letters onto the cipher text
ciphertext = ciphertext.lower()
decrypted_text = replace_chars(ciphertext,sorted_freq, english_letters)

print("--------------Part b-----------------\n")
print(decrypted_text)


#part c
part_c = {
    "cipher": sorted_freq[0],
    #removing the last 3 letters of the 'letters' list above since they were not used in the plaintext
    "plaintext": ["E", "T", "A", "N", "O", "R", "S", "I", "C", "L", "H", "D", "U", "P", "M", "G", "W", "F", "V", "Y", "K", "B", "X"]
}

compare_letters = pd.DataFrame(part_c)

print("--------------Part c-----------------\n")
print(compare_letters)

#part d

plaintext_freq = {}
char_frequency(decrypted_text, plaintext_freq)

freq_presort_2 = pd.DataFrame([frequency.keys(), frequency.values()])
freq_presort_2 = freq_presort_2.T
sorted_freq_2 = freq_presort_2.sort_values(by = [1], ascending= False)
sorted_freq_2=sorted_freq_2.reset_index(drop=True)

#Trim the characters (\n, spaces, hypens, semicolons, etc)

sorted_freq_2 = sorted_freq_2.drop([0,20,24,26])
sorted_freq_2=sorted_freq_2.reset_index(drop=True)

#Get the frequency of each letter in the text
total_2 = sorted_freq[1].sum()
percentage_pt = []

for i in range(0,23):
    temp = sorted_freq[1].iloc[i]
    b = (temp / total)*100
    b = round(b,2)
    percentage_pt.append(b)

sorted_freq_2['frequency'] = percentage_pt

print("--------------Part d-----------------\n")
print(sorted_freq_2)
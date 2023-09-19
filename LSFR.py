#start off with some binary text,and place that text in a list
start_state = [1,0,0,1,1,0,0,0,0,1]
lfsr = [1,0,0,1,1,0,0,0,0,1]

#at the 1st, 3rd, and 10th place in the list the bit will be xored and moved to the back of the list to replace the bit that is being sent out
#chosen poly- x^10 + x^3 + 1

#after a certain amount of runs, the machine stops (512 bits) in which the outputted bits are the final ciphertext
output = ""
period = 0

while True:
    feedback = lfsr[9] ^ lfsr[6]
    #shift bits in for loop
    for i in range(0,10):
        #traverse list backwards
        if 9-i != 0:
            lfsr[9-i] = lfsr[9-i-1]
        else:
            lfsr[0] = feedback
            output += str(lfsr[9])
    if (lfsr == start_state):
        period = len(output)
        break


print("------------Part b---------------")
print("Output bit stream: \n", output[0:511])

print("------------Part c---------------")
#Get period of the output text- 2^10 -1
print("period: ", period)

print("------------Part d---------------")
#encrypt P=`11101100000110111011010011111010` using the first 32 bits of the key stream generated above
P = [1,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0]
stream_key = output[0:32]
ciphertext = []
cipher = ""
for i in range(0,32):
    if int(stream_key[i]) != P[i]:
        ciphertext.append(1)
    else:
        ciphertext.append(0)

print("encrypted text:      ", ciphertext)
print("------------Part e---------------")
#Decrypt the message using the same key
plaintext = []

for i in range(0,32):
    if int(stream_key[i]) != ciphertext[i]:
        plaintext.append(1)
    else:
        plaintext.append(0)

print("original text:       ", P)
print("decrypted plaintext: ", plaintext)
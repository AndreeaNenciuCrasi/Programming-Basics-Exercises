# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -# > going.

# A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add -ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, replace ie with y and add -ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding -ing
# By default just add -ing
# Write the script which takes infinitive verbs and displays their present participle form in 
# separated lines.

x = input('Verb: ')
y = list(x)
consonant = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
vowel = ('a', 'e', 'i', 'o', 'u')

if y[len(y)-1] == "e" and x!=('be', 'see', 'flee', 'knee') and y[len(y)-2] != "i":
    del y[len(y)-1]
    y.append('ing')
    print(''.join(y))

elif y[len(y)-2] == "i" and y[len(y)-1] == "e":
    del y[len(y)-2]
    del y[len(y)-1]
    y.append('ying')
    print(''.join(y))

elif y[len(y)-1] in consonant and y[1] in vowel and y[0] in consonant:
    y.append(y[len(y)-1])
    y.append('ing')
    print(''.join(y))

else:
    y.append('ing')
    print(''.join(y))

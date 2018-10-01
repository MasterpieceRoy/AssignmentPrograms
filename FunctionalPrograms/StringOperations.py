'''
*********************************************************************************************
 Purpose: Generates the permutations of the number

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   20-09-18


**********************************************************************************************
'''
def permutations(string):
    if len(string) == 1:
        return string

    recursive_perms = []
    for i in string:
        for perm in permutations(string.replace(i, '', 1)):  # replaces the element with a blank one time
            recursive_perms.append(i+perm)  # adds the replaced string to the array

    return set(recursive_perms)


def perms_iter(word2):
    stack = list(word2)  # stores the word into a stack
    results = [stack.pop()]  # pops the element and stores it in results
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])  # add the word to the new_results array
        results = new_results
    return results


word1 = input("Enter a word")
new_word1 = set()

new_word1 = permutations(word1)
print(new_word1)
print(len(new_word1))

word2 = input("Enter a word")
new_word2 = set()
new_word2 = perms_iter(word2)
print(new_word2)
print(len(new_word2))

# for i in new_word1:
#     for j in new_word2:
if [i for i, j in zip(new_word1, new_word2) if i == j]:  # used to check if both the arrays are equal or not
    print("Both the arrays are equal")
else:
    print("Both the arrays are not the same")






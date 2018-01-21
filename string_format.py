"""
Write a Python Program to print the given string in the format specified in the sample
output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens

Sample Output:
WE, THE PEOPLE OF INDIA,
having solemnly resolved to constitute India into a SOVEREIGN, !
SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
and to secure to all its citizens:
"""

input_sentence = "WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens"
print ("input_sentence : " + input_sentence)

print ("\n\n")

formatted_sentence = input_sentence.replace("INDIA, ", "INDIA,\n").replace("SOVEREIGN, ", "SOVEREIGN, !\n").replace("REPUBLIC ", "REPUBLIC \n") + (":")
print ("Formatted sentence : " + formatted_sentence)


# LetterFrequency.py
# Name:
# Date:
# Assignment:
#
# This program counts letter frequencies in a message or file,
# writes them to a CSV file, and also shows a bar chart.

import os
import matplotlib.pyplot as plt

def countLetters(message, skipZeros=False):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26  # frequency list for each letter A-Z

    # Loop through each character in the message
    for letter in message:
        if letter in alpha:
            index = alpha.index(letter)
            freq[index] += 1

    # Create the output text in the format A,5\n
    output = ""
    for i in range(26):
        if skipZeros and freq[i] == 0:
            continue
        print(alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output += line

    writeToFile(output)
    makeChart(alpha, freq, skipZeros)

def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    with open("frq.csv", "w") as freqFile:
        freqFile.write(fileText)

def makeChart(alpha, freq, skipZeros=False):
    letters = []
    counts = []

    for i in range(26):
        if skipZeros and freq[i] == 0:
            continue
        letters.append(alpha[i])
        counts.append(freq[i])

    plt.bar(letters, counts)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.title("Letter Frequency")
    plt.show()

def main():
    choice = input("Type '1' to enter a message, or '2' to read from a file: ")

    if choice == "1":
        msg = input("Enter a message: ")
    elif choice == "2":
        filename = input("Enter filename (e.g. input.txt): ")
        with open(filename, "r") as f:
            msg = f.read()
    else:
        print("Invalid choice")
        return

    skipZeros = input("Skip letters with zero frequency? (y/n): ").lower() == "y"
    countLetters(msg, skipZeros)

if __name__ == "__main__":
    main()

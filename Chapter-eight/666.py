def count_letters(string , ltr):
    count = 0
    repeats = 0
    while repeats < len(string):
        str_index = string.find(ltr,repeats, repeats + 1)
        if string.find(ltr,repeats, repeats+1)>= 0:
            count+=1
        repeats += 1
    return count
print(count_letters("banana", "a"))


def analyze(str):
    s_without_punct = ""
    for letter in str:
        if letter not in string.punctuation:
            s_without_punct += letter
    mylist = s_without_punct.split()
    count = 0
    for i in mylist:
        if i.find("e")>=0:
            count+= 1
    numwords = len(mylist)
    percentage = count/numwords*100
    return 'Your test contains{0} words, of which {1} ({2}%) contain an "{3}" ".'.format(numwords, count,percentage)

speech = """"The distinguished surgeon Norman Bethune was a member of the Canadian Communist Party. In 1936 when the German and Italian fascist bandits invaded Spain, he went to the front and worked for the antifascist Spanish people. In order to help the Chinese people in their War of Resistance Against Japan, he came to China at the head of a medical team and arrived in Yenan in the spring of 1938. Soon after he went to the Shansi-Chahar-Hobei border area. Imbued with ardent internationalism and the great communist spirit, he served the army and the people of the Liberated Areas for nearly two years. He contracted blood poisoning while operating on wounded soldiers and died in Tanghsien, Hopei, on November 12, 1939.
"Comrade Norman Bethune, a member of the Communist Party of Canada, was around fifty when he was sent by the Communist Parties of Canada and the United States to China; he made light of travelling thousands of miles to help us in our War of Resistance Against Japan. He arrived in Yenan in the spring of last year, went to work in the Wutai Mountains, and to our great sorrow died a martyr at his post. What kind of spirit is this that makes a foreigner selflessly adopt the cause of the Chinese people's liberation as his own? It is the spirit of internationalism, the spirit of communism, from which every Chinese Communist must learn ...
Comrade Bethune's spirit, his utter devotion to others without any thought of self, was shown in his boundless sense of responsibility in his work, and his boundless warmheartedness towards all comrades and the people. Every Communist must learn from him. There are not a few people who are irresponsible in their work, preferring the light to the heavy, shoving the heavy loads on to others and choosing the easy ones for themselves. At every turn they think of themselves before others. When they make some small contribution, they swell with pride and brag about it for fear that others will not know. They feel no warmth toward comrades and the people but are cold, indifferent and apathetic. In fact such people are not Communists or at least cannot be counted as true Communists ...
We must learn the spirit of absolute selflessness from him. With this spirit everyone can be very useful to the people. A man's ability may be great or small, but if he has this spirit, he is already noble-minded and pure, a man of moral integrity and above vulgar interests, a man who is of value to the people."
"""""
"""
STATEMENT:
Given: string, list of words
Want:
- indices of substrings
- substring = concat of all given words, no overlapping
- words are same length

Strategy:
- matched_words, hashmap_words
- stopping = whether matched and length satisfy
- constant next chunk move (next slice)
- iterate until find first word
- iterate until all matched
    or iterate until word that's unmatched
    skip to there

Learned:
- for each index, loop through to see if it is 
possible starting

"""

def find_word_concat(str1, words):

    """
    Time: O(n * m * len)
    m = total # words
    len = length of word

    Space: O(m)
    O(m+n) if result is big
    """
    if len(words) ==0 or len(words[0]) == 0:
        return []
    
    word_freq = {}

    #prep hash
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
    results_indices = []
    words_count = len(words)
    word_length = len(words[0]) #stated in prompt

    #weird boundary as need concat all words
    for i in range((len(str1 - words_count * word_length)+1)):
        words_seen = {}

        for j in range(0, words_count):
            #get to next target
            next_word_idx = i+j * word_length

            #get next word
            word = str1[next_word_idx: next_word_idx + word_length]

            if word not in word_freq: #if not valid word, break
                break
            
            #add to seen
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            #skip process if already have enough of this word
            if words_seen[word] > word_freq.get(word, 0):
                break
            
            #if found all words
            if j+1 == words_count:
                results_indices.append(i)

    return results_indices

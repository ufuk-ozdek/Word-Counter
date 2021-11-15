import string

text = open('word_count_data.txt', encoding='utf-8-sig')
text = text.read()
text = text.translate(str.maketrans('','',string.punctuation))
text = text.lower()
text = text.split()


class word_counting:
    def __init__(self, text):
        self.text = text

    def mapper(self, text):
        keys_vals = []
        for word in text:
            temp = word + ' ' + str(1)
            keys_vals.append(temp)
        return keys_vals

    def reducer(self, keys_vals):
        data_pairs = list(dict.fromkeys(keys_vals))
        for item in data_pairs:
            count = keys_vals.count(item)
            print(item.split(" ")[0] + ":" + str(count))


s = word_counting(text)
y = s.mapper(text)
y.sort()
s.reducer(y)

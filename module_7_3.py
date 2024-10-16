# Домашнее задание по теме "Оператор "with"."
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words (self):
        all_words = {}
        punctuation_marks = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding = "utf-8") as file:
                words = file.read().lower()
                for char in punctuation_marks:
                    words = words.replace(char, ' ')
                words = words.split()
                all_words[file_name] = words
        return all_words

    def count(self, word):
        result = {}
        the_word_is_in_lowercase = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            result[file_name] = words.count(the_word_is_in_lowercase)
        return result

    def find(self, word):
        result = {}
        the_word_is_in_lowercase = word.lower()
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            positions = [i for i, wrd in enumerate(words) if wrd == the_word_is_in_lowercase]
            result[file_name] = positions[0] + 1
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
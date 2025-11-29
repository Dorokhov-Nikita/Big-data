import re
from src.core.job.mapper import Mapper


class VowelsConsMapper(Mapper):
    def map(self, record, emit):
        tokens = re.findall(r"[a-zA-Zа-яА-ЯіїєґІЇЄҐ]+(?:[`'’\-][a-zA-Zа-яА-ЯіїєґІЇЄҐ]+)*", record)
        for token in tokens:
            word = token.lower()
            vowels = sum(1 for c in word if c in "аеєиіїоуюяaeiou")
            consonants = sum(1 for c in word if c.isalpha() and c not in "аеєиіїоуюяaeiou")
            emit(len(word), (vowels, consonants, 1))
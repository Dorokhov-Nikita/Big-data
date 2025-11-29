from src.core.job.mapper import Mapper
import re


class WordCountMapper(Mapper):
    def map(self, record, emit):
        tokens = re.findall(r"[a-zA-Zа-яА-ЯіїєґІЇЄҐ]+(?:[`'’\-][a-zA-Zа-яА-ЯіїєґІЇЄҐ]+)*", record)
        for token in tokens:
            word = token.lower()
            if not word.isdigit():
                emit(word, 1)

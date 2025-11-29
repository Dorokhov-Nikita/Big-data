import re
from src.core.job.mapper import Mapper


class LongWordsMapper(Mapper):
    def map(self, record, emit):
        tokens = re.findall(r"[a-zA-Zа-яА-ЯіїєґІЇЄҐ]+(?:[`'’\-][a-zA-Zа-яА-ЯіїєґІЇЄҐ]+)*", record)
        for token in tokens:
            if len(token) > 5:
                emit(token.lower(), 1)
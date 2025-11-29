from src.core.job.reducer import Reducer


class VowelsConsReducer(Reducer):
    def reduce(self, key, values, emit):
        total_v = sum(v for v, _, _ in values)
        total_c = sum(c for _, c, _ in values)
        total_words = sum(n for _, _, n in values)

        if total_words == 0:
            return

        perc_v = total_v / (total_v + total_c) * 100
        perc_c = total_c / (total_v + total_c) * 100

        emit(key, f"{perc_v:.1f}% vowels, {perc_c:.1f}% consonants")
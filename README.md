python -m src.cli.main run --workers 3 --reducers 2 --input data/input --output data/output_clean --job src.student_jobs.word_count.mapper_clean:WordCountMapper,src.student_jobs.word_count.reducer_clean:WordCountReducer


python -m src.cli.main run --workers 3 --reducers 2 --input data/input --output data/output_length --job src.student_jobs.word_count.mapper_length:LongWordsMapper,src.student_jobs.word_count.reducer_length:LongWordsReducer


python -m src.cli.main run --workers 3 --reducers 2 --input data/input --output data/output_vc --job src.student_jobs.word_count.mapper_vc:VowelsConsMapper,src.student_jobs.word_count.reducer_vc:VowelsConsReducer



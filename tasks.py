# import pandas as pd
# from celery_config import celery_app
# import logging
# import os
# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)
#
# def process_chunk(dataframe):
#     return dataframe.groupby(['Song', 'Date']).agg({'Plays': 'sum'}).reset_index()
#
#
# @celery_app.task
# def process_csv(input_file, output_dir):
#     logger.debug(f"Processing file: {input_file}")
#     logger.debug(f"Processing id: {process_csv.request.id}")
#
#     # Read csv per chunks
#     dataframe = pd.read_csv(input_file)
#
#     # Group chunks by dates
#     final_df = process_chunk(dataframe)
#
#     # Save the result to a new file
#     output_file = f"{output_dir}/processed.csv"
#     final_df.to_csv(output_file, index=False)
#
#     logger.debug(f"Processing complete, result saved to: {output_file}")
#
#     return output_file

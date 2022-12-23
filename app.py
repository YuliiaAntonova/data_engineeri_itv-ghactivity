from util import get_spark_session
from process import transform
from read import from_files
import os


def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
    src_file_format = os.environ.get("SRC_FILE_FORMAT")
    spark = get_spark_session(env, 'GitHub Activity - Getting Started')
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)
    df_transformed = transform(df)
    df.printSchema()
    df_transformed. \
        select('repo.*', 'created_at', 'year', 'month', 'day'). \
        show()


if __name__ == '__main__':
    main()

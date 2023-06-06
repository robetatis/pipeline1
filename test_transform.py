import unittest
from transform import Transformation
from pyspark.sql import SparkSession


class TransformTest(unittest.TestCase):

    def test_run(self):

        spark = SparkSession \
            .builder \
            .appName('test Transform') \
            .enableHiveSupport() \
            .getOrCreate()

        x = [
                (1, 'Jenkins', 'Future', 2),
                (2, 'CMS', None, 100),
                (3, 'XXXX', 'Future', None)
        ]

        df = spark.createDataFrame(x, schema='course_id int , course_name string, author_name string, no_reviews int')

        stage_transform = Transformation()
        df_transformed = stage_transform.run(df)
        actual_author_name = df_transformed.filter("course_id='2'").select('author_name').collect()[0].author_name
        actual_no_reviews = df_transformed.filter("course_id='3'").select('no_reviews').collect()[0].no_reviews

        self.assertEqual('Unknown', actual_author_name)
        self.assertEqual(0, actual_no_reviews)

if __name__ == '__main__':
    unittest.main()

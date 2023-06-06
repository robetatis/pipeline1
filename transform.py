import logging.config

class Transformation:

    logging.config.fileConfig('resources/configs/logging.conf')
    logger = logging.getLogger('transform')

    def run(self, df):
        self.logger.info('transforming')
        df1 = df.na.fill('Unknown', ['author_name'])
        df2 = df1.na.fill(0, ['no_reviews'])
        # df.na.drop()
        return df2

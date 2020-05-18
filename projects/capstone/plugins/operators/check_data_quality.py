from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 postgres_conn_id="",
                 quality_checks=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.postgres_conn_id=postgres_conn_id
        self.quality_checks=quality_checks
        
    def execute(self, context):
        postgres_hook = PostgresHook(self.postgres_conn_id)
        for check in self.quality_checks:
            sql = check.get('quality_check_sql_stmt')
            expected = check.get('expected')
 
            records = postgres_hook.get_records(sql)[0]
            fail_count = 0
            failed = []
            if expected != records[0]:
                fail_count += 1
                failed.append(sql)
 
        if fail_count:
            raise ValueError(f"Data quality checks failed: {failed}")
        else:
            logging.info(f"All data quality checks passed!")

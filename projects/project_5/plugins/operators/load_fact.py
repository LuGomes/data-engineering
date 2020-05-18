from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    
    @apply_defaults
    def __init__(self,
                 postgres_conn_id="",
                 table="",
                 sql_statement="",
                 append=False,
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.postgres_conn_id=postgres_conn_id
        self.table = table
        self.sql_statement=sql_statement
        self.append = append

    def execute(self, context):
        self.log.info("Loading data into fact table")
        redshift = PostgresHook(self.postgres_conn_id)
        if self.append:
            sql_statement = f"INSERT INTO {self.table} {self.sql_statement}"
            redshift.run(sql_statement)
        else:
            sql_statement = f"DELETE FROM {self.table}"
            redshift.run(sql_statement)
            sql_statement = f"INSERT INTO {self.table} {self.sql_statement}"
            redshift.run(sql_statement)

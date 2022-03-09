#Importing modules
from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import DummyOperator

## Create deafult argument. Basically a python dictionary contains all arguments
default_args= {
  'owner':'Prabhat',
  'start_date': datetime(2022,3,4),  ## If want to specify start_date from 5 days ago then can use airflow.dates.days_ago(5) as start_date
  ## Specify end_date if you want to stop task after some time
  'depends_on_past': False,
  'email': ['hhshshs@demo.com'],
  'email_on_failure':False
  'email_on_retry':False
  'retries':1,   ## If task fail then retry one time and retry after waiting 2 minutes
  'retry_delay': timedelta(minutes=2),
}
  
  
 ## Instantiate a DAG
   dag= DAG(
     'demo', default_args=default_args, catchup=False, description='Demo DAG',
     schdeule_interval=timedelta(days=1)
   )
    
##Task { for the example lets use dummyoperator}
start=DummyOperator(task_id='start',dag=dag)
middle=DummyOpearor(task_id='sleep',bash_command='sleep 2',dag=dag)
end=DummyOperator(task_id='end', dag=dag)
   
## Execution
start>>middle>>end
  
  


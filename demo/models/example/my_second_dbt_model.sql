{{
    config(
        materialized= 'table',
        database='ESG_US_DEV_DB'
    )
}}

with stg_employees AS (

    select * from {{source('ESG_STG','STG_EMPLOYEES')}}
)

SELECT 

*

FROM stg_employees
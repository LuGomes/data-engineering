class SqlQueries:
    visits_table_insert = ("""
        INSERT INTO public.visits
        SELECT
                md5(visitor_id || arrival_date) visit_id,
                year,
                month,
                airport_code,
                arrival_date,
                arrival_mode,
                state_code,
                departure_date,
                visitor_id
        FROM staging_visits
    """)
    
    visitors_table_insert = ("""
        INSERT INTO public.visitors
        SELECT DISTINCT visitor_id, citizenship, residency, age, gender, visa_category, visa_type
        FROM staging_visits
    """)
    
    airports_table_insert = ("""
        INSERT INTO public.airports
        SELECT DISTINCT city, type, airport_code
        FROM staging_airports
    """)
    
    cities_table_insert = ("""
        INSERT INTO public.cities
        SELECT DISTINCT *
        FROM staging_cities
    """)

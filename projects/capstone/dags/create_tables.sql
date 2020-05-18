DROP TABLE IF EXISTS public.staging_visits;
CREATE TABLE IF NOT EXISTS public.staging_visits (
    "year" INT2,
    "month" INT2,
    citizenship INT2,
    residency INT2,
    airport_code VARCHAR,
    state_code VARCHAR,
    age INT4,
    gender VARCHAR,
    visitor_id INT8,
    visa_type VARCHAR,
    arrival_date DATE,
    departure_date DATE,
    visa_category VARCHAR,
    arrival_mode VARCHAR
);

DROP TABLE IF EXISTS public.staging_airports;
CREATE TABLE IF NOT EXISTS public.staging_airports (
    airport_code VARCHAR,
    city VARCHAR,
    "type" VARCHAR
);

DROP TABLE IF EXISTS public.staging_cities;
CREATE TABLE IF NOT EXISTS public.staging_cities (
    city VARCHAR,
    state_name VARCHAR,
    avg_house_size VARCHAR,
    state_code VARCHAR,
    race VARCHAR,
    median_age INT2,
    male_pop INT4,
    female_pop INT4,
    total_pop INT4,
    veteran_pop INT4,
    foreign_born_pop INT4,
    race_count INT4
);


DROP TABLE IF EXISTS public.visits;
CREATE TABLE IF NOT EXISTS public.visits (
    visit_id VARCHAR NOT NULL,
    "year" INT2,
    "month" INT2,
    airport_code VARCHAR,
    arrival_date DATE,
    arrival_mode VARCHAR,
    state_code VARCHAR,
    departure_date DATE,
    visitor_id INT8,
    CONSTRAINT visits_pkey PRIMARY KEY (visit_id)
);


DROP TABLE IF EXISTS public.cities;
CREATE TABLE IF NOT EXISTS public.cities (     
    city VARCHAR NOT NULL,
    state_name VARCHAR,
    avg_house_size VARCHAR,
    state_code VARCHAR,
    race VARCHAR,
    median_age INT2,
    male_pop INT4,
    female_pop INT4,
    total_pop INT4,
    veteran_pop INT4,
    foreign_born_pop INT4,
    race_count INT4,
    CONSTRAINT cities_pkey PRIMARY KEY (city)
);

DROP TABLE IF EXISTS public.visitors;
CREATE TABLE IF NOT EXISTS public.visitors (     
    visitor_id INT8 NOT NULL,
    citizenship INT2,
    residency INT2,
    age INT4,
    gender VARCHAR,
    visa_category VARCHAR,
    visa_type VARCHAR,
    CONSTRAINT visitors_pkey PRIMARY KEY (visitor_id)
);


DROP TABLE IF EXISTS public.airports;
CREATE TABLE IF NOT EXISTS public.airports (    
    airport_code VARCHAR NOT NULL,
    city VARCHAR,
    "type" VARCHAR,
    CONSTRAINT airports_pkey PRIMARY KEY (airport_code)
);

DROP TABLE IF EXISTS public.countries;
CREATE TABLE IF NOT EXISTS public.countries (    
    country_code INT4 NOT NULL,
    country_name VARCHAR,
    CONSTRAINT countries_pkey PRIMARY KEY (country_code)
);

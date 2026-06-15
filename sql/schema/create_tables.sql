CREATE TABLE marketing_performance (
    campaign_id INTEGER PRIMARY KEY,
    campaign_date DATE,
    campaign_name TEXT,
    platform TEXT,
    target_audience TEXT,
    impressions INTEGER,
    clicks INTEGER,
    leads INTEGER,
    applications INTEGER,
    enrollments INTEGER,
    cost REAL,
    revenue REAL,
    region TEXT
);
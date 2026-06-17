

-- Campaign Performance (Fact Table)


CREATE TABLE campaign_performance (
    campaign_date DATE,
    campaign_id TEXT,
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
    region TEXT,

    FOREIGN KEY (campaign_id)
        REFERENCES campaign_meta(campaign_id)
);

/*
-- Campaign Metadata (Dimension Table)


CREATE TABLE campaign_meta (
    campaign_id TEXT PRIMARY KEY,
    objective TEXT,
    start_date DATE,
    end_date DATE,
    budget REAL,
    campaign_type TEXT,
    creative_type TEXT,
    manager TEXT,
    channel TEXT,
    conversion_goal TEXT
);

-- Channel Rates (Lookup Table)


CREATE TABLE channel_rates (
    channel TEXT PRIMARY KEY,
    avg_cpm REAL,
    avg_cpc REAL,
    remarks TEXT
);
*/


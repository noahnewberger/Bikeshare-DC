SELECT * FROM crosstab($$
    select distinct 
    main.startutc::date as pilot_date,
    main.operatorclean,
    count(distinct main.bikeid) as bikes_available
    from dockless_trips as main
    left join
    (select distinct 
    operatorclean, 
    bikeid,
    min(startutc::date) as first_ride,
    (date_trunc('day', max(startutc)) + interval '1 day')::date as last_ride_plus
    from dockless_trips
    group by 1, 2) as bike_age
    on main.operatorclean = bike_age.operatorclean and main.startutc::date between bike_age.first_ride and bike_age.last_ride_plus
    where main.startutc::date = '2017-12-01'
    group by 1, 2$$
    
    ,$$SELECT unnest('{jump,lime,mobike,ofo,spin}'::text[])$$)
AS ct ("pilot_date" date, "jump" int, "lime" int, "mobike" int, "ofo" int, "spin" int);
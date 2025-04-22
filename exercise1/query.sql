WITH RankedPatientSatisfaction AS (
    SELECT
        patient_id,
        JSON_EXTRACT(scores, "$.satisfaction") as satisfaction,
        CASE strftime("%m", date)
            WHEN "01" THEN "January"
            WHEN "02" THEN "February"
            WHEN "03" THEN "March"
            WHEN "04" THEN "April"
            WHEN "05" THEN "May"
            WHEN "06" THEN "June"
            WHEN "07" THEN "July"
            WHEN "08" THEN "August"
            WHEN "09" THEN "September"
            WHEN "10" THEN "October"
            WHEN "11" THEN "November"
            WHEN "12" THEN "December"
        END AS month,
        ROW_NUMBER() OVER (PARTITION BY strftime('%m', date), patient_id ORDER BY date DESC) AS rank
    FROM Scores
),
MonthlyPromotersDetractors AS (
    SELECT
        month,
        SUM(CASE
            WHEN satisfaction > 8 THEN 1
            ELSE 0
            END
        ) AS n_promoters,
        SUM(CASE
            WHEN satisfaction < 7 THEN 1
            ELSE 0
            END
        ) AS n_detractors,
        COUNT(*) AS n_patients
    FROM RankedPatientSatisfaction
    WHERE rank = 1
    GROUP BY month
)
SELECT
    month,
    ((CAST(n_promoters AS FLOAT) - n_detractors) / n_patients)*100 AS NPS
FROM MonthlyPromotersDetractors;
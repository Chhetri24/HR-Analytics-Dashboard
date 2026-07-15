USE hr_analytics;
-- Total Employees
SELECT COUNT(*) AS TotalEmployees
FROM employees;

-- Attrition Count
SELECT Attrition,
COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Attrition;

-- Attrition Rate
SELECT
ROUND(
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS AttritionRate
FROM employees;

-- Attrition by Department
SELECT
Department,
COUNT(*) AS TotalEmployees,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS AttritionCount,
ROUND(
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)
*100.0/COUNT(*),2
) AS AttritionRate
FROM employees
GROUP BY Department;
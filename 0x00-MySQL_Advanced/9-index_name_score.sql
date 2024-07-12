--  a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score
-- Assuming the names table is already imported

-- Create the index idx_name_first_score on the first letter of name and score
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1), score);


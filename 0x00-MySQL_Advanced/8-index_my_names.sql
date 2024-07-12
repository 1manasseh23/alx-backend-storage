USE holberton;  -- Assuming the database name is holberton

-- Drop the index if it already exists (optional step to ensure idempotence)
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create the index on the first letter of the name column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));


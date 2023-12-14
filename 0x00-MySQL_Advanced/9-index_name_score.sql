-- Create the index
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);


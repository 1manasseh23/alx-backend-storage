-- a SQL script that creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER //

CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_qty INT;
    
    -- Fetch current quantity of the item
    SELECT quantity INTO item_qty
    FROM items
    WHERE name = NEW.item_name;
    
    -- Update quantity in items table
    UPDATE items
    SET quantity = item_qty - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;


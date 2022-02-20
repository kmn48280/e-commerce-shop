-- DROP TABLE IF EXISTS "category" CASCADE
-- CREATE TABLE "category"(
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100),
--     level INTEGER,
--     products VARCHAR(50)
-- );

-- DROP TABLE IF EXISTS "item" CASCADE
-- CREATE TABLE item(
--     id SERIAL PRIMARY KEY,
--     "name" VARCHAR(100),
--     "desc" TEXT,
--     price DECIMAL(5,2),
--     img VARCHAR(100),
--     created_on DATE,
--     category_id INTEGER NOT NULL,
--     cart_id INTEGER,
--     FOREIGN KEY (category_id) REFERENCES category(category_id)
-- );

-- DROP TABLE IF EXISTS "cart" CASCADE
CREATE TABLE cart(
    user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    created_on DATE,
    FOREIGN KEY (user_id) REFERENCES public.user(user.id),
    FOREIGN KEY (item_id) REFERENCES item(item.id)
);



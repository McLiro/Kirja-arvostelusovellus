CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    score INTEGER,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE replies (
    id SERIAL PRIMARY KEY,
    content TEXT,
    review_id INTEGER REFERENCES reviews,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);
-- SQLite
INSERT INTO loads_measurements (id, demand, circuitBreaker, phase, neutral, grounding, conduit, typePhase)
VALUES (1, 0, 40, 10, 10, 6, 20, 'Monofásico'),
(2, 5, 63, 16, 16, 10, 50, 'Monofásico'),
(3, 8, 40, 10, 10, 16, 50, 'Trifásico'),
(4, 15, 50, 10, 10, 16, 50, 'Trifásico'),
(5, 19, 63, 16, 16, 16, 50, 'Trifásico'),
(6, 24, 100, 35, 35, 16, 50, 'Trifásico'),
(7, 38, 125, 35, 50, 35, 50, 'Trifásico'),
(8, 47, 175, 50, 50, 35, 50, 'Trifásico'),
(9, 65, 200, 95, 50, 35, 50, 'Trifásico'),
(10, 75, 200, 240, 120, 35, 75, 'Trifásico'),
(11, 150, 200, 400, 240, 35, 75, 'Trifásico');
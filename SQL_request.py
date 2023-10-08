$ ssh 6643425b-d989-4635-9863-7984d142ee1d@serverhub.praktikum-services.ru -p 4554
morty@1998a17238d0:~$ ^C
morty@1998a17238d0:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# ^C
scooter_rent=# SELECT track,
scooter_rent-#        CASE
scooter_rent-#            WHEN finished = true THEN 2
scooter_rent-#            WHEN cancelled = true THEN -1
scooter_rent-#            WHEN "inDelivery" = true THEN 1
scooter_rent-#            ELSE 0
scooter_rent-#        END AS status
scooter_rent-# FROM "Orders";
 track  | status
--------+--------
 870079 |      1
 870079 |      1
 125193 |      0
 691080 |      0
 118491 |      0
 516564 |      1
 516564 |      1
 503363 |      1
 503363 |      1
 455885 |      1
 455885 |      1
 157683 |      0
 887451 |      1
 887451 |      2
 367086 |      0
 639005 |     -1
(16 rows)

scooter_rent=# SELECT "courier"."login", COUNT(orders.id) AS number_of_orders
INNER JOIN "Orders" AS orders ON "courierId" = "orders"."courierId"
scooter_rent-# FROM "Couriers" AS courier
scooter_rent-# INNER JOIN "Orders" AS orders ON "courierId" = "orders"."courierId"
scooter_rent-# WHERE "orders"."inDelivery" = true
scooter_rent-# GROUP BY "courier"."login";
 login | number_of_orders
-------+------------------
 NINYA |               10
 ninja |               10
 Ninja |               10
(3 rows)

scooter_rent=# Connection to serverhub.praktikum-services.ru closed by remote host.
Connection to serverhub.praktikum-services.ru closed.

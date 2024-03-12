drop database if exists graph;
create database graph;
use graph;

create table node (
 node_id int primary key,
 type varchar(20)
 );
 
 create table edge (
 edge_id int primary key,
  in_node int,
  out_node int,
  type varchar(20)
  );
  
create table node_props (
  node_id int,
  propkey varchar(20),
  string_value varchar(100),
  num_value double
  );
  
 
 insert into node values 
 (1,'Person'),
 (2,'Person'),
 (3,'Person'),
 (4,'Person'),
 (5,'Person'),
 (6,'Book'),
 (7,'Book'),
 (8,'Book'),
 (9,'Book');
 
 insert into node_props values
 (1, 'name', 'Emily', null),
 (2, 'name', 'Spencer', null),
 (3, 'name', 'Brendan', null),
 (4, 'name', 'Trevor', null),
 (5, 'name', 'Paxton', null),
 (6, 'title', 'Cosmos', null),
 (6, 'price', null, 17.00),
 (7, 'title', 'Database Design', null),
 (7, 'price', null, 195.00),
 (8, 'title', 'The Life of Cronkite', null),
 (8, 'price', null, 29.95),
 (9, 'title', 'DNA and you', null),
 (9, 'price', null, 11.50);
 
 insert into edge values
 (1, 1, 7, 'bought'),
 (2, 2, 6, 'bought'),
 (3, 2, 7, 'bought'),
 (4, 3, 7, 'bought'),
 (5, 3, 9, 'bought'),
 (6, 4, 6, 'bought'),
 (7, 4, 7, 'bought'), 
 (8, 5, 7, 'bought'),
 (9, 5, 8, 'bought'),
 (10, 1,2,'knows'),
 (11, 2, 1, 'knows'),
 (12, 2, 3, 'knows');
 
 
-- a. What is the sum of all book prices? Give just the sum.
select sum(num_value) as sum_price
from node_props
where propkey = 'price';
/* OUTPUT
+ -------------- +
| sum_price      |
+ -------------- +
| 253.45         |
+ -------------- +
1 rows
*/


-- b. Who does Spencer know? Give just their names.
select string_value as name
from node_props
where node_id in (
	select edge.out_node
	from node_props join edge on node_props.node_id = edge.in_node 
	where edge.type = 'knows' and node_props.string_value = 'Spencer');
/* OUTPUT
+ --------- +
| name      |
+ --------- +
| Emily     |
| Brendan   |
+ --------- +
2 rows
*/


-- c. What books did Spencer buy? Give title and price.
select string_value as title, num_value as price
from (select node_id, string_value from node_props) as str 
inner join (select node_id, num_value from node_props) as num on num.node_id = str.node_id
where num.node_id in (
	select edge.out_node
	from node_props join edge on node_props.node_id = edge.in_node 
	where edge.type = 'bought' and node_props.string_value = 'Spencer')
    and num.num_value is not null and str.string_value is not null;
/* OUTPUT
+ ---------- + ---------- +
| title      | price      |
+ ---------- + ---------- +
| Cosmos     | 17         |
| Database Design | 195        |
+ ---------- + ---------- +
2 rows
*/


-- d. Who knows each other? Give just a pair of names.
select n1.string_value as name1, n2.string_value as name2
from edge as e1
join edge as e2 on e1.in_node = e2.out_node and e1.out_node = e2.in_node
join node_props as n1 on e1.in_node = n1.node_id
join node_props as n2 on e1.out_node = n2.node_id
where e1.type = 'knows' and e2.type = 'knows' and e1.edge_id < e2.edge_id;
/* OUTPUT
+ ---------- + ---------- +
| name1      | name2      |
+ ---------- + ---------- +
| Emily      | Spencer    |
+ ---------- + ---------- +
1 rows
*/


-- e. Demonstrate a simple recommendation engine by answering the following question with a SQL query: 
-- What books were purchased by people who Spencer knows? Exclude books that Spencer already owns. 
-- Warning: The algorithm we are using to make recommendations is conceptually simple, but you may find
-- that your SQL query is rather complicated. This is why we need graph databases!
select np.string_value as books
from (select distinct purch_e.out_node
	from node_props as purch_p join edge as purch_e on purch_p.node_id = purch_e.in_node
	where purch_e.type = 'bought' and
		purch_e.in_node in (
			select node_id
			from node_props
			where node_id in (
				select edge.out_node
				from node_props join edge on node_props.node_id = edge.in_node 
				where edge.type = 'knows' and node_props.string_value = 'Spencer'))) as purch_books 
join node_props as np on np.node_id = purch_books.out_node
where purch_books.out_node not in (
	select spencer_edge.out_node
    from edge as spencer_edge
    join node_props as spencer_props on spencer_edge.out_node = spencer_props.node_id
    where spencer_edge.type = 'bought' and spencer_props.string_value is not null and spencer_edge.in_node = 2)
    and np.string_value is not null;
/* OUTPUT
+ ---------- +
| books      |
+ ---------- +
| DNA and you |
+ ---------- +
1 rows
*/

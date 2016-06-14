# pip install neo4j-driver

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://172.22.17.1:7474", auth = basic_auth("neo4j", "monet+"))
session = driver.session()

session.run("CREATE (a:Person {name:'Arthur', title:'King'})")

result = session.run("MATCH (a:Person) WHERE a.name = 'Arthur' RETURN ")

for record in result:
    print("%s %s" % (record["title"], record["name"]))

session.close()
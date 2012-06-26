
Could you write me a todo list management application in Django where I can:
 - register and log in
 - I can have my todo list displayed
 - I can manipulate my list (add/remove/modify entries)
 - Assign priorities to the entries.
 - I could do the same using a very simple REST api.

I don't need any design/UI/logo, etc plain html is fine.


	INSTALL

Jun 26 2012. IMPORTANT Dev version has bugfixes:
pip install hg+https://bitbucket.org/jespern/django-piston/


		API
	
	Create:	
curl -u kittle:kittle -X POST -H "Content-Type: application/json" --data '{ "priority": "1", "todo": "foo" }' -v http://localhost:8000/api/item/

	Read:
curl -u kittle:kittle -X GET http://localhost:8000/api/items
curl -u kittle:kittle -X GET -v http://localhost:8000/api/item/12

	Update:
curl -u kittle:kittle -X PUT -H "Content-Type: application/json" --data '{ "priority": "11", "todo": "bar" }' -v http://localhost:8000/api/item/14

	Delete:
curl -u kittle:kittle -X DELETE -v http://localhost:8000/api/item/12


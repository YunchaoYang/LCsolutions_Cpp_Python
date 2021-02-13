
Web services: SOAP vs REST: Which one is better? 

### SOAP(Simple Object Access Protocal)
* Protocal
* work at any internet protocol
* permits only XML
* support SSL and WS-Security
* Envelope (big, require more bandwidth, header + body + WSDL)
* hide business logic
* overhead: whole envelope

1. send XML as SOAP request
2. receive XML file response.

### REST API:
* Architecture
* Works mostly HTTP
* REST uses HTT for all 4 CRUD operations - HTTP method
  - Create (POST)
  - Read (GET)
  - Update (PUT)
  - Delete (DELETE)
* Postcard (only not envelope)
* less bandwidth required
* permit XML, JSON, txt,
* URI (indicating resources) exposes business logic; secure as well as HTTPS is used.
* HTTP status code
* overhead: only postcard, less


https://www.youtube.com/watch?v=7YcW25PHnAA


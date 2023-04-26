openapi: 3.0.0
info:
  title: Heroes API
  version: 1.0.0
servers:
  - url: http://localhost:5000/
paths:
  /heroes:
    get:
      summary: Get all heroes
      responses:
        '200':
          description: A list of heroes
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: The hero's ID
                    name:
                      type: string
                      description: The hero's name
      tags:
        - Heroes

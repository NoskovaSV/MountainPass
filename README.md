openapi: 3.0.2
info:
  title: 'Mountain Pass'
  version: "0.1"
paths:
  /perevals/:
    get:
      operationId: listPerevals
      description: 'List of perevals'
      parameters: []
      responses:
        '200':
          content:
          application/json:
            schema:
              type: array
              items:
                  $ref: '#/components/schemas/Pereval'
          description: ''
      tags:
        - perevals

    post:
      operationId: createPereval
      description: 'Create Pereval'
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Pereval'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Pereval'
          description: ''
      tags:
        - perevals

components:
  schemas:
    Pereval:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 64
      required:
        - beauty_title
        - title
        - other titles
        - coord_id

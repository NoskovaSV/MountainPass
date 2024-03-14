payload:
  allShortcutsEnabled: false
  path: /
  repo:
    id: 765617967
    defaultBranch: master
    name: MountainPass
    ownerLogin: NoskovaSV
    currentUserCanPush: false
    isFork: false
    isEmpty: false
    createdAt: '2024-03-01T09:27:51.000Z'
    ownerAvatar: https://avatars.githubusercontent.com/u/142382581?v=4
    public: true
    private: false
    isOrgOwned: false
  currentUser: null
  refInfo:
    name: master
    listCacheKey: v0:1710405699.0
    canEdit: false
    refType: branch
    currentOid: c1cb224a2ff84f6afd0120162af085273f09d17b
  tree:
    items:
      - name: Pereval
        path: Pereval
        contentType: directory
      - name: .gitignore
        path: .gitignore
        contentType: file
      - name: README.md
        path: README.md
        contentType: file
      - name: main.py
        path: main.py
        contentType: file
    templateDirectorySuggestionUrl: null
    readme:
      displayName: README.md
      richText: >-
        <article class="markdown-body entry-content container-lg"
        itemprop="text"><p dir="auto">openapi: 3.0.2

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

        - perevals</p>

        <div class="snippet-clipboard-content notranslate position-relative
        overflow-auto" data-snippet-clipboard-copy-content="post:
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
            - perevals"><pre class="notranslate"><code>post:
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
        </code></pre></div>

        <p dir="auto">components:

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

        - coord_id</p>

        </article>
      errorMessage: null
      headerInfo:
        toc: []
        siteNavLoginPath: /login?return_to=https%3A%2F%2Fgithub.com%2FNoskovaSV%2FMountainPass
    totalCount: 4
    showBranchInfobar: false
  fileTree:
    '':
      items:
        - name: Pereval
          path: Pereval
          contentType: directory
        - name: .gitignore
          path: .gitignore
          contentType: file
        - name: README.md
          path: README.md
          contentType: file
        - name: main.py
          path: main.py
          contentType: file
      totalCount: 4
  fileTreeProcessingTime: 2.048768
  foldersToFetch: []
  treeExpanded: true
  symbolsExpanded: false
  csrf_tokens:
    /NoskovaSV/MountainPass/branches:
      post: >-
        FDdH5ch9klLD8Cz7PVWatEYGM17sKbbiriIJbfuYSNYhMqL55JQp39gzjyKUfOYb_6S6caXW-LjjYAuqdqRvtQ
title: MountainPass/ at master · NoskovaSV/MountainPass

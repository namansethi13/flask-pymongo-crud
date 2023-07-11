<h1>Simple RESTful CRUD using Flask and pymongo</h1>
<body>
  <h1>User Management API Documentation</h1>
   <h2>How to start</h2>
  <p>Just run the command python app.py in the root directory</p>
   <h2>Or create a docker image using</h2>
  <p>docker build -t image .</p>
  <h2>Endpoints</h2>

  <div class="endpoint">
    <div class="method">GET</div>
    <div class="endpoint-path">/users</div>
    <div class="description">Returns a list of all users.</div>
  </div>

  <div class="endpoint">
    <div class="method">GET</div>
    <div class="endpoint-path">/users/&lt;id&gt;</div>
    <div class="description">Returns the user with the specified ID.</div>
  </div>

  <div class="endpoint">
    <div class="method">POST</div>
    <div class="endpoint-path">/users</div>
    <div class="description">Creates a new user with the specified data.</div>
    <div class="request-example">
      <pre>
        <code>
{
  "name": "User's Name",
  "email": "user@example.com",
  "password": "userpassword"
}
        </code>
      </pre>
      <p>All fields are mandatory.</p>
    </div>
  </div>

  <div class="endpoint">
    <div class="method">PUT</div>
    <div class="endpoint-path">/users/&lt;id&gt;</div>
    <div class="description">Updates the user with the specified ID with the new data.</div>
    <div class="request-example">
      <pre>
        <code>
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "password": "updatedpassword"
}
        </code>
      </pre>
      <p>At least one field is needed, and all fields are optional. Provide the fields that need to be updated.</p>
    </div>
  </div>

  <div class="endpoint">
    <div class="method">DELETE</div>
    <div class="endpoint-path">/users/&lt;id&gt;</div>
    <div class="description">Deletes the user with the specified ID.</div>
  </div>

GET /users
        </code>
      </pre>
    </div>
    <div class="response-example">
      <pre>
        <code>
[
  {
    "name": "User 1",
    "email": "user1@example.com",
    "password": "hashedpassword1"
  },
  {
    "name": "User 2",
    "email": "user2@example.com",
    "password": "hashedpassword2"
  }
]
        </code>
      </pre>
    </div>
  </div>

  <div class="response-example">
    <h3>Get User by ID</h3>
    <div class="request-example">
      <pre>
        <code>
GET /users/12345
        </code>
      </pre>
    </div>
    <div class="response-example">
        <p>Response</p>
      <pre>
        <code>
{
  "name": "User 1",
  "email": "user1@example.com",
  "password": "hashedpassword1"
}
        </code>
      </pre>
    </div>
  </div>

  <div class="response-example">
    <h3>Create User</h3>
    <div class="request-example">
      <pre>
        <code>
POST /users

{
  "name": "New User",
  "email": "newuser@example.com",
  "password": "newuserpassword"
}
        </code>
      </pre>
    </div>
    <div class="response-example">
          <p>Response</p>
      <pre>
        <code>
User created successfully!
        </code>
      </pre>
    </div>
  </div>

  <div class="response-example">
    <h3>Update User</h3>
    <div class="request-example">
      <pre>
        <code>
PUT /users/12345
{
  "name": "Updated User",
  "email": "updateduser@example.com"
}
        </code>
      </pre>
    </div>
    <div class="response-example">
        <p>Response</p>
      <pre>
        <code>
User updated successfully!
        </code>
      </pre>
    </div>
  </div>

  <div class="response-example">
    <h3>Delete User</h3>
    <div class="request-example">
      <pre>
        <code>
DELETE /users/12345
        </code>
      </pre>
    </div>
    <div class="response-example">
        <p>Response</p>
      <pre>
        <code>
User deleted successfully!
        </code>
      </pre>
    </div>
  </div>

</body>

</html>

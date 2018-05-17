
# SQLAlchemy CRUD Lab

In this lab we will once again use SQLAlchemy to create a database and a table.  We also will practice establishing sessions for database communication.  By the end of the lab, we will be comfortable using sessions to interact with and make changes to our database table.

### Objective

* Become comfortable performing CRUD (Create, Read, Update, Delete) actions with SQLAlchemy

### Sessions

As a reminder, the `Session` establishes all communication to the database.  The `Session` object follows the [Unit of Work](https://martinfowler.com/eaaCatalog/unitOfWork.html) pattern for interacting with the database.  It keeps track of all changes separately in an ongoing transaction until we explicitly commit the changes to the database.  In other words, the session logs all the changes we make separately, whether they be table inserts, updates, or deletes, until we explicity **flush** the session with the `session.commit()` method. 

We create a session by establishing a connection to the database with `create_engine` as we saw in the last lab.

>     engine = create_engine('sqlite:///states.db', echo=True)

We configure our session class so that it is connected to our database via the engine variable from above.  Finally, we create a new instance of the session class that creates this particular interaction with the database.

>     Session = sessionmaker(bind=engine)
>     session = Session()


### Instructions

#### Create the table

Create the `states` table in the `schema.py` file.  We have provided you with all of the code for configuring the database.  Every state has an `id` (set as the primary key), a `name`, a `capital_city`, a `population`, and a `landlocked` column that holds a boolean depending upon whether the state borders a body of water.

Once this task is completed, execute the file by running `python schema.py` in your terminal to create the database and the `states` table.

#### CREATE

We will write all of our CRUD actions in the `states_controller.py` file.  We provided the starter code for starting a session in the first method to get you going.

* New York
    - name: 'New York'
    - capital: 'Albany'
    - population: 20000000
    - landlocked: no
    
* Wyoming
    - name: 'Wyoming'
    - capital: 'Cheyenne'
    - population: 579315
    - landlocked: yes

#### READ

* Query all states in the database

For now, we will just query all the data in our table.  We will explore more advanced queries in a later lesson.  Use `session.query()` and `.all()` to pull everything off of the table and set it to a variable.  Return this variable to get the test to pass.

#### UPDATE

Uncomment the `create_cali()` function.  In `update_cali()`:

* Find California by using `session.query()` in conjunction with `filter_by`.  You can read about the latter method [here](http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.filter_by).

* Change California's population to 50000000 then commit the update.

#### DELETE

Uncomment the `create_connecticut()` function.  In `delete_connecticut()`:

* Find the Connecticut object
* Delete it from the database 

### Session Rollbacks

Remember if we mistakenly change data during a session, we can rollback the error as long as we haven't already committed those changes to the database.  In the final method, uncomment the code for adding West Dakota to the table.  Write a rollback so that this "state" doesn't get added to the database when we commit the session.

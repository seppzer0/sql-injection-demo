# sql-injection-demo

This is a primitive demo of an SQL injection with PostgreSQL.

## Usage

To build the Docker image and setup the demo stand, in the root of the repository run:

```sh
docker build . -t sql-injection-demo
```

**Alternatively**, you can download a prebuilt image from the project's storage:

```sh
docker pull ghcr.io/seppzer0/sql-injection-demo
```

Finally, launch the demo using:

```sh
docker run -it --rm sql-injection-demo
```

Finally, when given a prompt, enter your query.

## Example queries

Normal input: `Danny`<br>
SQL injection: `Danny' UNION SELECT * FROM people WHERE isadmin = 'true`

## Debugging and playing around

If you want to play around with this demo within the provided Docker container, you can use the following command in the root of the repository:

```sh
docker run -it --rm --user root -v $(pwd):/app_debug -w /app_debug sql-injection-demo /bin/bash -c "service postgresql start && bash"
```

Keep in mind that you would still need to run `psql -f db.sql` and `python3 cmd.py` commands manually, as a "postgres" user. Which can be done using the `su - postgres` command.

# sql-injection-demo

This is a primitive demonstration of an SQL injection with PostgreSQL.

## Usage

To build the Docker image and setup the demo stand, in the root of the repository run:

```sh
docker build . -t sql-injection-demo
```

***Alternatively***, you can download a prebuilt image from the project's storage:

```sh
docker pull ghcr.io/seppzer0/sql-injection-demo
```

Once done, launch the demo using:

```sh
docker run -it --rm sql-injection-demo
```

Finally, when given a prompt, provide your input.

## Example inputs

Normal input: `Danny`<br>
SQL injection: `Danny' UNION SELECT * FROM people WHERE isadmin = 'true`

## Debugging and playing around

If you want to play around with this demo within the provided Docker container, you can use the following command in the root of the repository:

```sh
docker run -it --rm -v $(pwd):/app_debug -w /app_debug sql-injection-demo /bin/sh -c "pg_ctl start && /bin/sh"
```

This way you can edit the `cmd.py` (or any other source file) right in your text editor of choice on your host machine, and then test it immediately in the Docker container with a manual launch of the `python3 cmd.py` command.

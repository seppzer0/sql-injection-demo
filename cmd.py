import psycopg


def main(keyword: str) -> None:
    """Check the name provided from user."""
    with psycopg.connect(dbname="postgres", user="postgres") as connect:
        with connect.cursor() as cur:
            # NOTE: this is a very unsafe way of passing a query to an adapter (psycopg),
            #       which enables the SQL injection
            query = "SELECT * FROM people WHERE \"person_name\" = '{}';"
            cur.execute(query.format(keyword))
            # NOTE: a much safer way would be (comment 2 lines above and uncomment 4 lines below):
            #cur.execute(
            #    'SELECT * FROM people WHERE person_name = %s', 
            #    (keyword,)
            #)
            result = cur.fetchall()
            if not result:
                print("[\u2717] No data found on the provided name!")
            else:
                [print(print(f"\nResponse: {line}\n")) for line in result]
                print("[\u2713] Your request has been successfully processed!")


# launch the demo
if __name__ == "__main__":
    main(input("\n[?] Please, enter person\'s name: "))

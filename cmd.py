import psycopg


def launch(keyword: str) -> None:
    '''Check the name provided from user.'''
    with psycopg.connect(dbname='postgres', user='postgres') as connect:
        with connect.cursor() as cur:
            # this is a very unsafe way of passing a query to an adapter (psycopg),
            # which enables the SQL injection
            query = "SELECT * FROM people WHERE \"person_name\" = '{}';"
            cur.execute(query.format(keyword))
            # a much safer way would be (comment 2 lines above and uncomment 4 lines below):
            #cur.execute(
            #    'SELECT * FROM people WHERE person_name = %s', 
            #    (keyword,)
            #)
            result = cur.fetchall()
            if not result:
                print("[\u2717] No data found on the provided name!")
            else:
                for line in result:
                    print(f"\nResponse: {line}\n")
                print("[\u2713] Your request has been successfully processed!")


# launch the demo
if __name__ == "__main__":
    launch(input('\n[?] Please, enter person\'s name: '))

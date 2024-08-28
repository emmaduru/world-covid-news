from ..db import connect_to_db

# Remove all rows from the news table.
cur, conn = connect_to_db()
cur.execute("DELETE FROM News;")
cur.close()
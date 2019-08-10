
import psycopg2

dbname = psycopg2('news')

question_1 = "What are the most popular three articles of all time?"
question_2 = "Who are the most popular article authors of all time?"
question_3 = "On which days did more than 1% of requests lead to errors?"

def get_answers():

    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute("SELECT title, count(*) as views FROM articles JOIN log ON articles.slug = substring(log.path, 10) GROUP BY title ORDER BY views DESC LIMIT 3;")
    answer_1 = c.fetchall()
    c.execute("SELECT authors.name, count(*) as views FROM articles JOIN authors ON articles.author = authors.id JOIN log ON articles.slug = substring(log.path, 10) WHERE log.status = '200 OK' GROUP BY authors.name ORDER BY views DESC;")
    answer_2 = c.fetchall()
    c.execute("SELECT round((count*100.0)/total,3) as percentage from total_requests join total_errors on total_requests.request_date = total_errors.error_date  limit 1;")
    answer_3 = c.fetchall()
    db.close()

    # printing results of report

    print(question_1)
    # printing the answer of Q1
    for i in answer_1:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

    print(question_2)
    # printing the answer of Q2
    for i in answer_2:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

    print(question_3)
        # printing the answer of Q1
    for i in answer_3:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")

if __name__ == '__main__':
	# calling the function
    get_answers()

import similarity as similarity
import csv_loader_book1 as csv1
import csv_loader_book2 as csv2
import measurement as measure

from book import book as bk
import datetime


def nested_loop_by_name_jaccard():
    threshold = 0.75
    q = 3
    books1 = csv1.csv_loader_book1()
    books2 = csv2.csv_loader_book2()
    results = []
    book1 = bk()
    book2 = bk()
    id1 = 0
    id2 = 0
    title1 = None
    title2 = None
    start_time = datetime.datetime.now()
    for i in range(0, len(books1)):
        book1 = books1[i]
        id1 = book1.get_id()
        title1 = book1.get_title()
        for j in range(i + 1, len(books2)):
            book2 = books2[j]
            id2 = book2.get_id()
            title2 = book2.get_title()
            sim = similarity.calc_jaccard(title1, title2, q)
            if sim >= threshold:
                # print(sim)
                # print(str(id1) + '_' + str(id2))
                results.append(str(id1) + ',' + str(id2))

    end_time = datetime.datetime.now()
    time = end_time - start_time
    print("Total Time:", round(time.total_seconds() * 1000, 3), 'milliseconds')
    measure.load_benchmark()
    measure.calc_measure(results)


# End of function

nested_loop_by_name_jaccard()

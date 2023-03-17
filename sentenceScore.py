from rouge import Rouge 

for i in range(0, 10):
    fileName = 'summaries/summary_' + str(i) +  '.txt'
    file1 = open(fileName, 'r')
    Lines = file1.readlines()
    summaries = []
    for l in Lines:
        if l == '\n':
            continue
        else:
            summaries.append(l)


    print('summaries', len(summaries))


    hypothesis = summaries[0]


    #BenchMark Summary
    reference1 = summaries[1]
    reference2 = summaries[2]

    rouge = Rouge()
    scores1 = rouge.get_scores(hypothesis, reference1, avg=True)
    scores2 = rouge.get_scores(hypothesis, reference2, avg=True)

    MetricsFileName = 'summary_metrics/summary_' + str(i) + '.txt'

    f = open(MetricsFileName, "a")
    f.write(str(scores1))
    f.write('\n')
    f.write(str(scores1))
    f.close()

    print('scores1: ', scores1)
    print('scores2: ', scores2)

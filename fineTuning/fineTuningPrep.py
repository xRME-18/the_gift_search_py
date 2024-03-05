import json


def makeDatasets(num):
    file_path = (
        "./../finalJSON/Product_Embedding_EstyPersonalisedGiftDescription"
        + str(num)
        + ".json"
    )
    finalJSON = {}
    with open(file_path, "r") as file:
        finalJSON = json.load(file)

    corpus_file_path = "./../fineTuning/corpus" + ".jsonl"
    query_file_path = "./../fineTuning/query" + ".jsonl"
    training_file_path = "./../fineTuning/training" + ".tsv"

    with open(corpus_file_path, "a+") as corpus_file:
        with open(query_file_path, "a+") as query_file:
            with open(training_file_path, "a+") as training_file:
                for product in finalJSON:
                    data = product["data"]
                    targetAudiance = data["targetAudience"]
                    data.pop("targetAudience")

                    corpusId = product["metadata"]["productId"] + "corpus"
                    queryId = product["metadata"]["productId"] + "query"

                    corpusJSON = {
                        "_id": corpusId,
                        "text": str(data),
                    }

                    queryJSON = {
                        "_id": queryId,
                        "text": str(targetAudiance),
                    }

                    training_file.write(queryId + "\t" + corpusId + "\t" + "1" + "\n")

                    corpus_file.write(json.dumps(corpusJSON))
                    corpus_file.write("\n")
                    query_file.write(json.dumps(queryJSON))
                    query_file.write("\n")


for num in range(1, 14):
    makeDatasets(num)

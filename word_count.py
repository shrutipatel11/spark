from pyspark import SparkContext
 
if __name__ == "__main__":
    # Spark configuration
    sc = SparkContext("local","Frequency counter program using Spark")

    # Read the file line by line and split words
    words = sc.textFile("large_file.txt")
    words = words.flatMap(lambda line : line.split(" "))

    # Map phase
    map_words = words.map(lambda word : (word, 1))
    
    # Reduce phase
    freq_count = map_words.reduceByKey(lambda a , b : a + b)
 
    # Save the output in a file
    freq_count.saveAsTextFile("output/")
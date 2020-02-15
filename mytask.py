#Calculate the number of movies per director per genre
#i.e. For each director, calculate number of movies directed per genre
list1=[{
    "Genre": "Drama",
    "Rating": 4.5,
    "Director": "Michael Curtiz",
    },
    {
    "Genre": "romentic",
    "Rating": 5.5,
    "Director": "Curtiz",
    },
    {
    "Genre": "Drama",
    "Rating": 6.5,
    "Director": "Michael",
    },
    {
    "Genre": "Drama",
    "Rating": 8.5,
    "Director": "Michael Curtiz",
    },
    {
    "Genre": "romentic",
    "Rating": 8.5,
    "Director": "Michael Curtiz",
    }]

def fun(list1):
    d={}
    dic={}
    count = 0
    for i in range(len(list1)):
        count = 1
        name = list1[i].get("Director")
        genre = list1[i].get("Genre")
        #print(name,genre)
        for j in range(len(list1)):
            if(name == list1[j].get("Director") and genre == list1[j].get("Genre")):
                count +=1
            d[list1[j].get("Director"),list1[j].get("Genre")] = count
        #print(d)
        dic.update(d)
        #dic.update(d)
    print(dic)
#####################################################
fun(list1)

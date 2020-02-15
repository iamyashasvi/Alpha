def fun(list1):
	d={}
	dic={}
	for elem in list1:
		d[elem['Director']]=d.get(elem['Director'],dic)
		if 'Director' in elem and 'Genre' in elem:
			dic[elem['Genre']]=dic.get(elem['Genre'],0)+1

	print(d)
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
    },]

fun(list1)
#1. Calculate the number of movies per director
#2. Calculate the number of movies per director per genre
#i.e. For each director, calculate number of movies directed per genre
#3. Calculate average rating of movies per director

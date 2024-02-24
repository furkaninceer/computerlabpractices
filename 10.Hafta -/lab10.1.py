max_score=-1
try:
    infile=open("Eurovision.txt","r")
    Country_name=infile.readline()
    while Country_name!="":
        Singer_name=infile.readline()
        Song_Title=infile.readline()
        print(Country_name,Singer_name,Song_Title,sep="")
        score=int(input("Score:"))
        while score<0:
            score=int(input("Score:"))
        if score>=max_score:
            max_score=score
            max_score_country=Country_name
            max_score_singer=Singer_name
            max_score_song=Song_Title
        Country_name=infile.readline()
    infile.close()
except IOError:
    raise IOError("File could not be found")
except ValueError:
    print("İnvalid Data")
except:
    print("An error occured")
print("The wWinner:\n",max_score_country,max_score_singer,max_score_song,max_score)
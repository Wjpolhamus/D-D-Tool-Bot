import mysql.connector


def executequery(data_,query,fetch = False):
    mycursor = mydb.cursor()

    if isinstance(data_, dict) and fetch == False:
        print(1)
        data = []
        for key, value in data_.items():
            if key in ["level","strg","dex","con","intel","wis",
                       "cha","proficiency","ac","initiative","speed","guildid"]:
                data.append(int(value))
            else:
                data.append(value)
        params = tuple(data)
        mycursor.execute(query, params)

    elif isinstance(data_, (list, tuple)):
        #print(2)
        params = tuple(data_)
        mycursor.execute(query, params)
    else:
        #print(3)
        params = (data_,)
        mycursor.execute(query, params)

    if fetch:
        result = mycursor.fetchall()
        mycursor.close()
        return result
    else:
        mydb.commit()
        mycursor.close()
        return None

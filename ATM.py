import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='4010',database="customer")
if con.is_connected()==False:
    print("Error")
cur=con.cursor()
cur.execute("select* from users")
data=cur.fetchall()
print("WELCOME")
a=int(input("ENTER YOUR ID_NO:"))
for i in data:
    if a==i[0]:
        print("ACCESS GRANTED")
        print("WELCOME ",i[1])
        b=int(input("ENTER YOUR PIN:"))
        if b==i[2]:
            print("ENTER D FOR DEPOSIT")
            print("ENTER W FOR WITHDRAW")
            print("ENTER B FOR CHECKING BALANCE")
            j=input("WHAT OPERATION YOU WANT TO DO:")
            if j=='d' or j=='D':
                k=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:"))
                z=i[3]+k
                update_data="update users set balance=%s where ID_NO = %s;"
                value=(z,a)
                cur.execute(update_data,value)
                print("----------ACCOUNT UPDATED SUCCESSFULLY----------")
                break
            elif j=='W' or j=='w':
                o=int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW:"))
                v=i[3]-o
                update_data="update users set balance=%s where ID_NO = %s;"
                value=(v,a)
                cur.execute(update_data,value)
                print("----------ACCOUNT UPDATED SUCCESSFULLY----------")
                break
            elif j=='b' or j=='B':
                print("YOUR NET BALANCE IS ",i[3])
                break
            else:
                print("INVALID")
            
        else:
            print("ENTER CORRECT PIN")
else:
        print("ENTER CORRECT ID_NO")
con.commit()  
cur.close()  
con.close()
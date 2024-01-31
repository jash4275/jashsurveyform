from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns

mypass = "jash7977"
mydatabase="mydatabase"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "bookTable" 
def analysis ():
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Analysis", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    

    
    try:
        
        cur.execute("SELECT * FROM bookTable WHERE Num_Of_Copies < 10 AND Sales > 50")
        low_stock_high_sales_books = cur.fetchall()

       
        cur.execute("SELECT * FROM bookTable WHERE Sales < 10 AND Num_Of_Copies > 50")
        low_sales_high_stock_books = cur.fetchall()

        cur.execute("SELECT * FROM bookTable")
        all_books = cur.fetchall()
        
        y=0.2
        i=1
        Label(labelFrame, text="Books with Low Stock and High Sales:",bg='black',fg='white').place(relx=0.07,rely=0.1)
        for book in low_stock_high_sales_books:
            Label(labelFrame, text=f"{i}) Title: {book[1]}, Author: {book[2]}, Copies Available: {book[3]}, Total Sales: {book[4]}",bg='black',fg='white').place(relx=0.07,rely=y)
            y+=0.1
            i+=1
           
        j=1
        Label(labelFrame, text="\nBooks with Low Sales and High Stock:",bg='black',fg='white').place(relx=0.07,rely=y+0.1)
        for book in low_sales_high_stock_books:
            Label(labelFrame, text=f"{j}) Title: {book[1]}, Author: {book[2]}, Copies Available: {book[3]}, Total Sales: {book[4]}",bg='black',fg='white').place(relx=0.07,rely=y+0.3)
            y+=0.1
            j+=1

        plt.figure(figsize=(18, 6))

        
        plt.subplot(1, 3, 1)
        sns.barplot(x=[book[1] for book in all_books], y=[book[3] for book in all_books])
        plt.title('All Books (Availability)')
        plt.xticks(rotation=45, ha='right')

        
        plt.subplot(1, 3, 2)
        sns.barplot(x=[book[1] for book in low_stock_high_sales_books], y=[book[4] for book in low_stock_high_sales_books])
        plt.title('Books with Low Stock and High Sales (Sales)')
        plt.xticks(rotation=45, ha='right')

        
        plt.subplot(1, 3, 3)
        sns.barplot(x=[book[1] for book in low_sales_high_stock_books], y=[book[3] for book in low_sales_high_stock_books])
        plt.title('Books with Low Sales and High Stock (Stocks)')
        plt.xticks(rotation=45, ha='right')

        
        plt.tight_layout()
        plt.show()

    except:
        print("Error!!")
    root.mainloop() 
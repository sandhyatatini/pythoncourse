try:
   f=open("demo.txt","r")
   print(f.read())
   f.close()
except Exception as e:
    print("error occured",e)
finally:
    print("completed")
    
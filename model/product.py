import mysql.connector
import json
class product_management:
    #for setting up connection 
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="<your_password>",database="<your_basename>")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("conection successful")        
        except:
            print("connection failed") 

    # get all data
    def getall(self):
       self.cur.execute("SELECT * FROM <your_table>")
       result=self.cur.fetchall()
       if result:
        return json.dumps(result)
       else:
        return "the inventory is empty"
    # add data  
    def add(self,data):
     self.cur.execute(f"INSERT INTO <your_table>(name,link) VALUES('{data['name']}','{data['link']}')")
     if(self.cur.rowcount>0):
       return "added successfully"
     else:
       return "there was an error in insertion"
    # delete data
    def delete(self,id):
     self.cur.execute(f"DELETE FROM <your_table> WHERE id={id['id']}")
     if(self.cur.rowcount>0):
       return "deleted successfully"
     else:
       return "nothing to delete"
    # update data 
    def update(self,data):
      self.cur.execute(f"UPDATE <your_table> SET name='{data['name']}',link='{data['link']}' WHERE id={data['id']}")
      if(self.cur.rowcount>0):
        return "updated successfully"
      else:
        return "there no anime with this id"     
       
       

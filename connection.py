import pymysql
conn = pymysql.connect(user='root', passwd='G6#QnkyL]~N5FTzj', db='db')
cur = conn.cursor()


class DatabaseConn:
    def getCustInvoice(self, name, surname):
        cur.execute("call db.get_invoice('" + name + "', '" + surname + "');")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            invoiceDic = {
                "id": int(col[0]),
                "customer_id": int(col[1]),
                "invoice_date": col[2],
                "billing_adress": col[3],
                "billing_city": col[4],
                "billing_state": col[5],
                "billing_country": col[6],
                "billing_postal": col[7],
                "total": int(col[8])

            }
            Elist.append(invoiceDic)

        return Elist

    def getCustInfo(self, name, surname):
        cur.execute("call db.get_customer_info('" + name + "', '" + surname + "');")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            cust_info = {
                "id": int(col[0]),
                "FirstName": col[1],
                "LastName": col[2],
                "Company": col[3],
                "Adress": col[4],
                "City": col[5],
                "State": col[6],
                "Country": col[7],
                "PostalCode": col[8],
                "Email": col[9],
                "SupportRank": col[10]

            }
            Elist.append(cust_info)
        return Elist

    def addCustomer(self, name, lname, company, email, adress, city, country, postal, phone):
        cur.execute("call db.add_customer('" + name + "','" + lname + "','" + company +"','"+adress+"', '"+city+"', '"+country+"', '"+postal+"','"+phone+"','" +email+"','2');")
        conn.commit()
    def deleteCustomer(self, name, lname):
        cur.execute("call db.delete_custromers('"+name+"', '"+lname+"')")
        conn.commit()
    def patchCustomer(self,id,collumn,toWhat):
        cur.execute("call db.update_column('"+id+"','"+collumn+"','"+toWhat+"')")
        conn.commit()
    def getAllCustomers(self):
        cur.execute("call db.get_all_customers()")
        conn.commit()
        Elist = []
        for col in cur.fetchall():
            invoiceDic = {
                "id": int(col[0]),
                "FirstName": col[1],
                "LastName": col[2],
                "Company": col[3],
                "Adress": col[4],
                "City": col[5],
                "State": col[6],
                "Country": col[7],
                "PostalCode": col[8],
                "Phone": col[9],
                "FAX": col[10],
                "Email": col[11],
                "S.rank": col[12]
            }
            Elist.append(invoiceDic)
        return Elist







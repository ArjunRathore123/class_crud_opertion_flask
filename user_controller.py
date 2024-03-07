from flask import Flask,request
from connection_db import connect_db
from flask_restful import Resource

class User(Resource):
    def get(self):
        connection = connect_db()
        cursor = connection.cursor()

        select_query = "SELECT * FROM student;"
        cursor.execute(select_query)
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        user_list = [{'id': user[0], 'student_name': user[1], 'contact': user[2],'address':user[3],'college_name':user[4]} for user in users]
        return {'users': user_list}
        
    def post(self):
        connection = connect_db()
        cursor = connection.cursor()

        data = request.get_json()
        name = data.get('student_name', '')
        contact = data.get('contact', '')
        address = data.get('address', '')
        cllgname = data.get('college_name', '')

        query = "INSERT INTO student (student_name,contact,address,college_name) VALUES (%s, %s,%s,%s);"
        cursor.execute(query, (name,contact,address,cllgname))
        connection.commit()
        cursor.close()
        connection.close()
        
        return {'message': 'Item created successfully'}, 201

class SingleUser(Resource):
    def put(self, id):
        connection = connect_db()
        cursor = connection.cursor()
        data = request.get_json()
        new_name = data.get('student_name', '')
        new_contact=data.get('contact','')
        new_address=data.get('address','')
        new_cllgname=data.get('college_name','')
        query = "UPDATE student SET student_name = %s,contact=%s, address=%s,college_name=%s WHERE id = %s;"
        cursor.execute(query, (new_name, new_contact,new_address,new_cllgname,id))
        connection.commit()
        cursor.close()
        connection.close()
        return {'message': 'Item updated successfully'}

    def delete(self, id):
        connection = connect_db()
        cursor = connection.cursor()
        query = "DELETE FROM student WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
        return {'message': 'Item deleted successfully'}
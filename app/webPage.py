""" This is a program to show how flask can be used in web development"""

from flask import Flask, render_template,url_for,request
import base64
webPage=Flask(__name__)

user={}
key="passwordisnotsecure"
dict2={}
email=''
password=''
name=''

# @webPage.route('/')
# def sign_in():
# 	return render_template("web.html")
@webPage.route('/',methods=['POST','GET'])
def sign_up():
	return render_template("web.html")
@webPage.route('/Registration',methods=['POST','GET'])
def identification():
	return render_template("web_sig_up.html",user=user)

@webPage.route('/Home',methods=['POST','GET'])
def home_page():
	global dict2,email,password,name
	if request.method =='POST':
		name=request.form['name_entry']
		user[name]=dict2
		email=request.form['email_entry']
		password=request.form['password_entry']
		c_password=request.form['c_password_entry']
		# gender=request.form['gender']
		if password==c_password:
			
			dict2['email']=email
			encrpt_chars=[]
			# name['gender']=gender
			for i in range(len(password)):
				key_c = key[i % len(key)]
				encoded_c = chr(ord(password[i]) + ord(key_c) % 256)
				encrpt_chars.append(encoded_c)
			enc_str="".join(encrpt_chars)
			enc_password=enc_str.encode()
			dict2['password']=enc_password
			password=enc_password
			return render_template("web.html", name=name),dict2


@webPage.route('/decryption',methods=['POST','GET'])
def decryption():
	if  request.method =='POST':
		if dict2['email']==request.form['email_home_page']:
			passwordl=request.form['password_home_page']
			encrpt_chars=[]
			for i in range(len(passwordl)):
				key_c = key[i % len(key)]
				encoded_c = chr(ord(passwordl[i]) + ord(key_c) % 256)
				encrpt_chars.append(encoded_c)
			enc_str="".join(encrpt_chars)
			enc_password=enc_str.encode()
			if dict2['password']==enc_password:
				return render_template("web_home.html", name=name)
		else:
			success=True
			return render_template("web.html",message=message)

if __name__=="__main__":
	webPage.run(debug=True)
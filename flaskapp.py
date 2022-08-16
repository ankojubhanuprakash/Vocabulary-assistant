
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 	
import pandas as pd
import spacy
from spacy.lang.en import English
import PyPDF2 
import json
app = Flask(__name__)


@app.route('/',methods = ['GET', 'POST'])
def hello_world():
  if request.method == 'POST':
    f = request.files['file']
    try:
      f.save(secure_filename(f.filename))
    except :
      return 'error in upload'
    else:
      nlp = English()
      df = pd.read_csv('livingorg.csv')##network
      per_stop = pd.read_csv('stopwords.csv').words.str.lower().to_list()##network
      mainlist = df.Word.str.lower().to_list()
      storelist = []
      pdfFileObj = open(f.filename, 'rb') 
      # creating a pdf reader object 
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
      for i in range (pdfReader.numPages):# read every page text and collect new words
        text = pdfReader.getPage(i).extractText()
        doc = nlp(text)
        for token in doc: 
          if (token.is_alpha and not token.is_stop and token.lower_ not in mainlist and token.lower_ not in storelist and token.lower_ not in per_stop ): #collect newwords in store to_list
            storelist.append(token.lower_)
      pdfFileObj.close() 
      print(len(storelist))      
      return render_template('index.html',wordlist= storelist)
  else:
    return render_template('index.html',wordlist= [])
    #return render_template('proceed.html')
  

@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
  if request.method == 'POST':
    f = request.files['file']
    try:
      f.save(secure_filename(f.filename))
    except :
      return 'error in upload'
    else:
      nlp = English()
      df = pd.read_csv('https://www.cgs.iitk.ac.in/wwwrw/ankojubhan20/livingorg.csv')
      mainlist = df.Word.to_list()
      storelist = []
      pdfFileObj = open('beer1997.pdf', 'rb') 
      # creating a pdf reader object 
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
      for i in range (pdfReader.numPages):# read every page text and collect new words
        text = pdfReader.getPage(i).extractText()
        doc = nlp(text)
        for token in doc: 
          if (token.is_alpha and not token.is_stop and token.text not in mainlist and token.text not in storelist): #collect newwords in store to_list
            storelist.append(token.text)
      pdfFileObj.close()       
      return render_template('index.html',wordlist= storelist)
  else:
    return 'No Upload'
		
@app.route('/proceed',methods=['GET','POST'])
def getmeanings():
  from getdata import getstuff
  if request.method == 'POST':
    conten_mean = []
    conten_exmp = []
    content = request.form['data']
    content = json.loads(content)
    content_word = content['word']
    stopword =content['stop_words']
    for word in content_word:
      mean,exmp = getstuff(word)
      conten_mean.append(mean)
      conten_exmp.append(exmp)
    
    complete_data = {'Word':content_word,'Meaning':conten_mean,'Usage':conten_exmp} 
    print(complete_data)
    print(len(content_word),len(conten_mean),len(conten_exmp))
    complete_data_df = pd.DataFrame(complete_data) 
    stopword_df = pd.DataFrame(stopword)
    complete_data_df.to_csv('livingorg.csv',mode='a',index = False, header=False)#mainVocab##neywork
    complete_data_df.to_csv('recent.csv',index = False, header=False)#recent Vocab##network
    stopword_df.to_csv('stopwords1.csv',mode='a',index=False,header=False)##network
    complete_data=json.dumps(complete_data)
    #return 1
    return complete_data
  
    

    

if(__name__ == '__main__'):
	app.run()
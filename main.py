#!/usr/bin/env python
# coding: utf-8

# ## `Name : Berchmans S`
# ## `RollNo : 215229107`

# ### Lab10 : Deployment of DNN as a web service

# In[2]:


from flask import request

from flask import jsonify

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('BK_SentimentAnalysis.html')

@app.route('/', methods=['POST'])
def my_form_post():    
    text = request.form['text']    
    nltk.download('vader_lexicon')  
    
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    sid = SentimentIntensityAnalyzer()    
    score = ((sid.polarity_scores(str(text))))['compound']    
    if(score > 0):        
        label = 'This sentence is positive'    
    elif(score == 0):        
        label = 'This sentence is neutral'    
    else:        
        label = 'This sentence is negative'    
    
    return(render_template('BK_SentimentAnalysis.html', variable=label))

    if __name__ == "__main__":    
        app.run(port='8088', threaded=False, debug=True)


# In[ ]:





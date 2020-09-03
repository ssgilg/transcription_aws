import wikipedia
import re
from nltk.tokenize import sent_tokenize


# query = "aws transcribe"
# text  = wikipedia.search(query)
# print(text)
# print(text[0])

# wiki = wikipedia.page(text[0])
# text = wiki.summary
# print("Summary")
# print(text)
# print("\n")
# quit()

def get_wiki_summary(keyword):
    try:
        wiki = wikipedia.page(keyword)
        text = wiki.content
        #text = wiki.summary
    except:
        
        text = wikipedia.suggest(keyword)
        print(text)
        wiki = wikipedia.page(text)
        text = wiki.content
        #text = wiki.summary
        print(wiki.summary)
        #print(text)
        
    text =     " ".join(text.split()) 
    text = re.sub(r'==.*?==+', '', text)
    text = re.sub(r'\[.*?\]+', '', text)
    text = re.sub(r'\{.*?\}+', '', text)
    text = re.sub(r'\(.*?\)+', '', text)
    text = re.sub(r'\}', '', text)
    text = re.sub(r'ö', 'o', text)
    
    text = text.replace('\n', '')

    return text

my_vocab = ["Functional programing", "Programing paradigm",
"Computer code",  "computer program", "debugging",
"Object Oriented Programming",
"NLP ML",
"NER nlp",
"apache spark",
"algorithm",
"java program",
"Typescript", "HTML5", "CSS", "IDE software", "VSCode",
"Linter software" , "Performance (Big O notation)",
"node javascript",
"react JS",
"big data",
"udemy",
"video",
"problem",
"online learning course",
"method test",
"vocabulary",
"aws services",
"aws transcribe",
"aws deploymnet",
"sql",
"back-end front-end",
"scala programming language",
"hadoop",
"machine learning",
"chatbot", 
"cluster analysis",
"embedding",
"technology",
"artificial intelligence",
"test cased code benchmarks",
"scrum meeting deadline schedule",
"data",
"matrix factorization",
"lemmatization",
"spacy nlp",
"supervised unsupervised learning",
"word-to-vec",
"coding programming exercise",
"update progress coding project weekly status",
"vacations days off", "sick days going to doctor",
"car parking", "office supplies", "Visa process appointments",
"academic degree college university transcripts"
]

super_text = []
for word in my_vocab:
    print(word)
    text = get_wiki_summary(word)
    toks = sent_tokenize(text)
    print(toks)
    for tok in toks:
        tok = re.sub(r'[^\w]', ' ', tok)
       
        super_text.append(tok)
    print("\n")


#text_file = open("my_file.txt", "w", encoding = "utf-8")

#for item in super_text:
#    text_file.write(item+"\n")
 
#text_file.close()
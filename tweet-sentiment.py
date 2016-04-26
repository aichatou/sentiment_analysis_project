#Importation des librairies 
import sys
import json
import operator
import re
import string




def main():
  # Restructuration di fichier Afinn-111.Txt en dictionnaire
  afinnfile = open(sys.argv[1])
  scores = {} # initialiser un dictionnaire vide
  for line in afinnfile:
    term, score  = line.split("\t")  # le fichier est delimite par tabulation "\t" entre les 2 termes
    scores[term] = int(score)  # Convertir le score en entier.

  tweet_file = open(sys.argv[2])                        
  t = []  # initilaiser une liste vide                                 
  for tweet_line in tweet_file:                       
    tweet = json.loads(tweet_line) 
    #Pour recuperer les donnees du  fichier 'jsonloads.txt, faire: 
    #print(json.dumps(tweet))                   
    if "id" in tweet.keys(): 
      t.append(tweet["text"]) #ajouter dans la liste le text de chaque tweet
 
 #Definition de regex pour supprimer dans les text tweets, les caracteres inutiles 
  emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
  regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else                                                                    +                            

              ]
  
  tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
  emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
  
  inter = []
  term_trouves = []  
  scores_term_trouves = []                                                   
  for item in t:
        # Restructurer le text de chaque tweet en eliminant tous les precedents regex retrouves    
        tokens = tokens_re.findall(item)
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        terms_only = [term for term in tokens if not term.startswith(('#', '@'))]

        inter = [term.encode('ascii', 'ignore') for term in terms_only] # ignorer l'encodage ASCII des tweets pour remedier aux problemes de lecture des donnees
        #Pour recuperer le fichier 'jsontext.txt, faire ici: 
        #print(inter)
        term_trouves = [term  for term in inter if scores.has_key(term)]# liste des termes du fichier AFINN, retrouves dans chaque tweet
        #Pour recuperer les donnees du fichier 'termes.txt, faire ici: 
        #print(term_trouves)
        scores_term_trouves = [scores[term]  for term in inter if scores.has_key(term)] # liste des scores des termes du fichier AFINN, retrouves dans chaque tweet
        #Pour recuperer les donnees du fichier 'scores.txt, faire ici: 
        #print(scores_term_trouves)
        print sum(scores_term_trouves)

if __name__ == '__main__':
  if len(sys.argv) == 4:
    main()   
  else:
    print('Nombre d"arguments systeme incorrect')




 


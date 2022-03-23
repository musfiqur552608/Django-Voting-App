from http.client import HTTPResponse
import imp
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

lang = ['Java', 'C', 'Python', 'C++', '.NET', 'C#', 'PHP', 'JavaScript', 'SQL', 'Objective-C', 'Delphi', 'Ruby', 'MATLAB', 'Assembly language', 'Swift', 'Go', 'Perl', 'R', 'SQL', 'Visual Basic', 'SAS', 'Dart', 'F#', 'COBOL', 'Scala', 'ABAP', 'Fortran', 'Lua', 'Rust', 'Lisp', 'Groovy', 'LabVIEW', 'Prolog', 'Ada', 'Julia', 'Haskell', 'Apex', 'Kotlin', 'Bash', 'Ladder Logic', 'Clojure', 'Scheme']

globalcnt = dict()

def index(request):
   
   dict = {
      "lang" : lang
   }
   return render(request, 'index.html', context=dict)

def getquery(request):
   q = request.GET['languages']
   if q in globalcnt:
      globalcnt[q] = globalcnt[q]+1
   else:
      globalcnt[q] = 1
   
   dict = {
      "lang" : lang,
      "globalcnt" : globalcnt
   }
   return render(request, 'index.html', context=dict)

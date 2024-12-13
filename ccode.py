
def attributs(content,simbols):
    ttrue=True
    cursors=0
    pos=0
    posactual=0
    posactual2=0
    posactual3=0
    returnlist=[]
    chars=""
    returnstring=""
    ons=0
    
    while ttrue:
        chars=""
        posactual=-1
        pos=-1
        for simbol in simbols:
            posactual=content.find(simbol,ons)
            if posactual!=-1:
                if posactual<=pos or pos==-1:
                    pos=posactual
                    chars=simbol
        if pos>-1:
            
            if chars=="'" or chars=='"':
                posactual3=content.find('"',pos+1)
                posactual2=content.find("'",pos+1)
                if posactual3<0:
                    posactual3=posactual2
                if posactual2<0:
                    posactual2=posactual3
                if posactual3<posactual2:
                    posactual2=posactual3
                if posactual2>-1:
                    pos=posactual2+1
                    ons=pos
                    
            
            
            if chars==simbols[0]:
                returnstring=content[cursors:pos].strip()
                if 0==0:
                     returnstring=returnlist=returnlist+[returnstring]
                     
                cursors=pos+1
                    
                ons=cursors
                
        else:
            returnstring=content[cursors:].strip()
            
            if 0==0:
                returnlist=returnlist+[returnstring]
            ttrue=False
    
    return returnlist

def processs(content):
    l1=[";","'",'"']
    tags=attributs(content,l1)
    
    
    for tag in tags:
        print(tag)
        
    
contents="funcA();funcB();funcC();funcD();"
contents=contents.replace("\n","\\n")
contents=contents.replace("\r","\\r")
processs(contents)



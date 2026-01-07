class Solution:
    def entityParser(self, text: str) -> str:
        
        l = list(text)
        s = text
        try:
            l = s.split("&amp;") 
            
            s = '&null'.join(l)
        except:
            pass
        
        try:
            l = s.split("&quot;") 
            
            s = '"null'.join(l)
        except:
            pass
        
        try:
            l = s.split("&apos;") 
            
            s = "'null".join(l)
        except:
            pass
        try:
            l = s.split("&gt;") 
            
            s = '>null'.join(l)
        except:
            pass
        try:
            l = s.split("&lt;") 
            
            s = '<null'.join(l)
        except:
            pass
        
        try:
            l = s.split("&frasl;") 
            
            s = '/null'.join(l)
        except:
            pass
        
        try:
            l = s.split("null") 
            
            s = ''.join(l)
        except:
            pass
        
        return s
        
                
            
                
            
            
      

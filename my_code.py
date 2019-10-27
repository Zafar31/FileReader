import os.path
import re
"""
This code works with text files which are not too large
"""

class FileHandler:
    def __init__(self,path): 
        self._is_validPath = True
        try:
            self.file=open(path, "r+")
            self.length=len(self.file.read())
        except Exception as ex:
            self._is_validPath = False
            print("There was error during file opening. Please check file for existanse ", ex)    
    
    # This method reads data from file and returns 2 values: Boolean and Text
    def read(self, byte_from=0, byte_to=-1):
        if not self._is_validPath:
            return False 
        if not self.check_position(byte_from, byte_to):
            return False    
        else:
            try:
                self.file.seek(byte_from)
                content = self.file.read(byte_to - byte_from)
                return True, content;            
            except Exception as ex:
                print("There was an error during reading the file ", ex)            
                return False
                
    # This method writes data to the file and returns Boolean value
    def write(self, pos_byte, data):
        if not self._is_validPath:
            return False 
        if not self.check_position(pos_byte):
            return False    
        else:
            try:
                self.file.seek(pos_byte)
                content= data + self.file.read()
            
                self.file.seek(pos_byte)
                self.file.write(content)
                return True  
            except Exception as ex:
                print("There was an error during writing to the file ", ex)            
                return False          

    # This method searches data from file and returns 2 values: Boolean and Dict of positions            
    def search(self, pos_byte, search_data):  
        if not self._is_validPath:
            return False 
        if not self.check_position(pos_byte):
            return False    
        else:    
            try:        
                self.file.seek(0)
                content = self.file.read()
                occurance=[m.start() for m in re.finditer(search_data, content)]
                result = {i : occurance[i] for i in range(0, len(occurance))}
                return True, result
            except Exception as ex:
                print("There was an error during searching in the file ", ex)            
                return False                      
    
    # This method validates given positions and returns Boolean value    
    def check_position(self, *args):
        for i in args:
            if not type(i)==int or i < 0 and i > self.length:
                print("Error: Please check value of position")
                return False
        return True        
    
    def __del__(self):
        print("closing file")
        if self._is_validPath:
           self.file.close()
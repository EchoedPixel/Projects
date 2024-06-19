class Assembler(object):
    def __init__(self, asmpath='', mripath='', rripath='', ioipath='') -> None:
        """
        Assembler class constructor.

        Initializes 7 important properties of the Assembler class:
        -   self.__address_symbol_table (dict): stores labels (scanned in the first pass)
            as keys and their locations as values.
        -   self.__bin (dict): stores locations (or addresses) as keys and the binary 
            representations of the instructions at these locations (job of the second pass) 
            as values.
        -   self.__asmfile (str): the file name of the assembly code file. This property
            is initialized and defined in the read_code() method.
        -   self.__asm (list): list of lists, where each outer list represents one line of 
            assembly code and the inner list is a list of the symbols in that line.
            for example:
                ORG 100
                CLE
            will yiels __asm = [['org', '100'] , ['cle']]
            Notice that all symbols in self.__asm are in lower case.
        -   self.__mri_table (dict): stores memory-reference instructions as keys, and their
            binary representations as values.
        -   self.__rri_table (dict): stores register-reference instructions as keys, and their
            binary representations as values.
        -   self.__ioi_table (dict): stores input-output instructions as keys, and their
            binary representations as values.
        
        Thie constructor receives four optional arguments:
        -   asmpath (str): path to the assembly code file.
        -   mripath (str): path to text file containing the MRI instructions. The file should
            include each intruction and its binary representation separated by a space in a
            separate line. Their must be no empty lines in this file.
        -   rripath (str): path to text file containing the RRI instructions. The file should
            include each intruction and its binary representation separated by a space in a
            separate line. Their must be no empty lines in this file.
        -   ioipath (str): path to text file containing the IOI instructions. The file should
            include each intruction and its binary representation separated by a space in a
            separate line. Their must be no empty lines in this file.
        """
        super().__init__()
        # Address symbol table dict -> {symbol: location}
        self.__address_symbol_table = {}
        # Assembled machine code dict -> {location: binary representation}
        self.__bin = {}
        # Load assembly code if the asmpath argument was provided.
        if asmpath:
            self.read_code(asmpath)   
        # memory-reference instructions
        self.__mri_table = self.__load_table(mripath) if mripath else {}
        # register-reference instructions
        self.__rri_table = self.__load_table(rripath) if rripath else {}
        # input-output instructions
        self.__ioi_table = self.__load_table(ioipath) if ioipath else {}

    def read_code(self, path:str):
        """
        opens .asm file found in path and stores it in self.__asmfile.
        Returns None
        """
        assert path.endswith('.asm') or path.endswith('.S'), \
                        'file provided does not end with .asm or .S'
        self.__asmfile = path.split('/')[-1] # on unix-like systems
        with open(path, 'r') as f:
            # remove '\n' from each line, convert it to lower case, and split
            # it by the whitespaces between the symbols in that line.
            self.__asm = [lines.rstrip().lower().split() for lines in f.readlines()]

    def __format2bin(self, lc:str, lc_format:str, format_bits:int) -> str:
        """
        converts lc from lcformat (hex or dec) to binary representation with
        max format_bits. If the lcber after conversion is less than format_bits
        long, the formatted text will be left-padded with zeros.
        Arguments:
            lc (str): the lcber to be formatted as binary. It can be in either
                        decimal or hexadecimal format.
            lcformat (str): the format of lc; either 'hex' or 'dec'.
            format_bits (int): the lcber of bits you want lc to be converted to
        """
        if lc_format == 'dec':
            return '{:b}'.format(int(lc)).zfill(format_bits)
        elif lc_format == 'hex':
            return '{:b}'.format(int(lc, 16)).zfill(format_bits)
        else:
            raise Exception('format2bin: not supported format provided.')

    def assemble(self, Input='') -> dict:
        assert self.__asm or Input, 'no assembly file provided'
        if Input:
            assert Input.endswith('.asm') or Input.endswith('.S'), \
                        'file provided does not end with .asm or .S'
        # if assembly file was not loaded, load it.
        if not self.__asm:
            self.read_code(Input)
        # remove comments from loaded assembly code.
        self.__rm_comments()
        # do first pass.
        self.__first_pass()
        # do second pass.
        self.__second_pass()
        # The previous two calls should store the assembled binary
        # code inside self.__bin. So the final step is to return
        # self.__bin
        return self.__bin
        
    def __load_table(self, path) -> dict:
        """
        loads any of ISA tables (MRI, RRI, IOI)
        """
        with open(path, 'r') as f:
            t = [lines.rstrip().lower().split() for lines in f.readlines()]
        return {opcode:binary for opcode,binary in t}

    def __islabel(self, string) -> bool:
        """
        returns True if string is a label (ends with ,) otherwise False
        """
        return string.endswith(',')

    def __rm_comments(self) -> None:
        """
        remove comments from code
        """
        for i in range(len(self.__asm)):
            for j in range(len(self.__asm[i])):
                if self.__asm[i][j].startswith('/'):
                    del self.__asm[i][j:]
                    break

    def __first_pass(self) -> None: 
        """
        Runs the first pass over the assmebly code in self.__asm.
        Should search for labels, and store the labels alongside their locations in
        self.__address_symbol_table. The location must be in binary (not hex or dec).
        Returns None
        """
        lc = 0
        for i in self.__asm:
            if i[0] == "org":
                lc = int(i[1] , 16)
                continue  #(Set lc)start the program and go to first instruction
            elif i[0] == "end":
                break  #go to second pass
            elif __islabel :
                #store label in asm, key -> label , value -> lc
                self.__address_symbol_table[i[0]] = self.__format2bin(str(lc), "dec" , 12 )
            lc = lc + 1

    def __second_pass(self):
        """
        Runs the second pass on the code in self.__asm.
        Should translate every instruction into its binary representation using
        the tables self.__mri_table, self.__rri_table and self.__ioi_table. It should
        also store the translated instruction's binary representation alongside its 
        location (in binary too) in self.__bin.
        """
        lc = 0
        for i in self.__asm:
            if __islabel:
                i = i[0:3]  
            if i[0] == "org":
                lc = int(i[1] , 16)
                continue
            elif i[0] == "end":
                break
            elif i[0] == "dec" or i[0] =="hex":
                x = self.__format2bin(i[1] , i[0] , 16 )
                self.__bin[self.__format2bin(str(lc),"dec" , 12 )] = x
            elif i[0] in self.__mri_table.keys(): 
                y = self.__mri_table[i[0]]
                x = self.__address_symbol_table[i[1] + ","] 
                if "i" in i :
                    F = "1"+y+x #indirect , 1-mri-opcode-address
                else:
                    F = "0" + y + x #direct , 0-mri-opcode-address
                self.__bin[self.__format2bin(str(lc), "dec", 12)] = F #assemble all parts to binary, store location given by lc
            else:
                if i[0] in self.__rri_table.keys():
                    self.__bin[self.__format2bin(str(lc), "dec", 12)] = self.__rri_table[i[0]] #store location given by lc
                elif i[0] in self.__ioi_table.keys():
                    self.__bin[self.__format2bin(str(lc), "dec", 12)] = self.__ioi_table[i[0]] #store location given by lc
                else:
                    print("Not Valid")
            lc = lc + 1 
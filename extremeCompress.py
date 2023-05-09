import tkinter as tk #line:1
def compress (O000OO00OO0000OOO ):#line:3
    return str (len (O000OO00OO0000OOO )%10 )#line:5
def decompress (OO0000O0000O0O0O0 ):#line:7
    return "The original string was: "+compressed_dict [OO0000O0000O0O0O0 ]#line:9
def on_compress_click ():#line:11
    O0OO0O00O0OO0OOOO =input_entry .get ()#line:13
    OOO0O000O0O000OOO =compress (O0OO0O00O0OO0OOOO )#line:14
    compressed_dict [OOO0O000O0O000OOO ]=O0OO0O00O0OO0OOOO #line:15
    output_label .config (text ="The compressed number is: "+OOO0O000O0O000OOO )#line:16
    input_entry .delete (0 ,tk .END )#line:17
    input_entry .insert (0 ,OOO0O000O0O000OOO )#line:18
def on_decompress_click ():#line:20
    O000O0OO0OO0000O0 =input_entry .get ()#line:22
    OOOO0OO0OOO0OOOO0 =decompress (O000O0OO0OO0000O0 )#line:23
    output_label .config (text =OOOO0OO0OOO0OOOO0 )#line:24
root =tk .Tk ()#line:27
root .title ("Extreme Compression")#line:28
input_label =tk .Label (root ,text ="Enter a string to compress or a number to decompress:")#line:31
input_label .pack ()#line:32
input_entry =tk .Entry (root )#line:33
input_entry .pack ()#line:34
compress_button =tk .Button (root ,text ="Compress",command =on_compress_click )#line:37
compress_button .pack ()#line:38
decompress_button =tk .Button (root ,text ="Decompress",command =on_decompress_click )#line:41
decompress_button .pack ()#line:42
output_label =tk .Label (root ,text ="")#line:45
output_label .pack ()#line:46
compressed_dict ={}#line:49
root .mainloop ()

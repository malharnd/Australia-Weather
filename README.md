# Buffer-Overloading

A simple buffer overloading operation using few inbuilt-kali tools, Immunity Debugger and a windows-based TCP, Vulnserver. 

_________________________________________________________________________________________________________________________________________________________________________________

1.SPIKING 

Attach vulnserver to Immunity debugger after running both of them as administrator.
 
<img width="500" alt="Screenshot 2022-12-03 at 12 56 25 AM" src="https://user-images.githubusercontent.com/64124824/205371068-ad9d0cf3-ec66-4744-aa88-02e14146de87.png">




Make sure Imminity debugger Is in a running state.

<img width="500" alt="Screenshot 2022-12-03 at 12 56 40 AM" src="https://user-images.githubusercontent.com/64124824/205371148-d99fcd0d-9529-4215-8483-3293bba30504.png">


 
Use netcat to connect to vulnserver using the default port 9999

<img width="500" alt="Screenshot 2022-12-03 at 12 56 52 AM" src="https://user-images.githubusercontent.com/64124824/205371189-ccd4e4ab-0f79-4e90-95c9-14af8060f320.png">


 
Create spk files for stats and trun to check if they can be spiked.  (check if they crash)

<img width="500" alt="Screenshot 2022-12-03 at 12 57 10 AM" src="https://user-images.githubusercontent.com/64124824/205371226-c03f2355-857d-43ec-b67d-88e9c71b9298.png">

 
![image](https://user-images.githubusercontent.com/61798852/125417708-539a96b9-b39b-4a6a-9991-31729799093d.png)

![image](https://user-images.githubusercontent.com/61798852/125417720-c4220444-9fde-4ed0-bb48-8a97c4aa7000.png)

 
Trun command crashes and hence can be exploited.

![image](https://user-images.githubusercontent.com/61798852/125417751-07d07f61-74b1-4b4e-8760-62b6caedd280.png)

_________________________________________________________________________________________________________________________________________________________________________________
 
 
2.	FUZZING

Now we know trun command is vulnerable.
  1.	Run vulnserver and immunity bugger as admin. Attach them.
  2.	Create a python script to deploy As to the buffer.
  3.	Get the approx bytes it crashed at.
  
  ![image](https://user-images.githubusercontent.com/61798852/125417782-e856276d-a1bc-4634-a519-c09e135f44d9.png)
  
  ![image](https://user-images.githubusercontent.com/61798852/125417792-790b9bdd-5f4b-4114-9486-6d015e6d29f4.png)

As we see, it crashed around 3000 bytes.
  
 _________________________________________________________________________________________________________________________________________________________________________________
  
  
3.	OFFSET 

we use metasploit to generate this alphanumeric string pattern which will overflow till the EIP.

![image](https://user-images.githubusercontent.com/61798852/125417835-74632823-88d0-4b9f-b0b8-6d441da44121.png)

![image](https://user-images.githubusercontent.com/61798852/125417846-1e243528-e201-49ce-abb0-f099324f18b6.png)
 
After passing the offset,it flows till the EIP which stores '386F4337' which we make use of.
using pattern_offset command in metasploit, we are able to point a pattern of it amongst the entire offset buffer string we had sent earlier.

![image](https://user-images.githubusercontent.com/61798852/125417874-16248f0d-a469-4ab1-b6e4-4935a84627c2.png)

  So at 2003 bytes it found a pattern telling us that at this point we can control the eip.

_________________________________________________________________________________________________________________________________________________________________________________


4.	OVERWRITE EIP:
 
 Run the overwriting python script. As we can see, EIP stores 424242 which is B in hex.
hence we have successfully overwritten the EIP and have it in control.

![image](https://user-images.githubusercontent.com/61798852/125417915-04336801-90dc-499a-9954-214746507fbe.png)

_________________________________________________________________________________________________________________________________________________________________________________


5.	FIND BADCARS

We run the script and look at immunity. We check the EIP and we have 42s.
Then we want to view the ESP in the hex dump. (follow in hex dump by right clicking ESP)
 
 ![image](https://user-images.githubusercontent.com/61798852/125417943-b05da67c-db21-46e5-9576-4f78fe8e76a1.png)


Scan through the hex dump to find any bad characters and take a note of them.

![image](https://user-images.githubusercontent.com/61798852/125417958-01190adc-74f3-4a74-82dc-a6b6dd1d79cf.png)

There are no badchars in vulnserver.

_________________________________________________________________________________________________________________________________________________________________________________


6.	FIND RIGHT MODULE IN MONA

 Find some part of Vulnserver that does not have any sort of memory protections. 

The topmost module fits the requirement as all protections are false. 

![image](https://user-images.githubusercontent.com/61798852/125417998-904dbb80-82c7-4699-bb08-de5391508aeb.png)


Find the opcode equivalent of JMP ESP. using a tool called nasm shell. 

JMP ESP opcode equivalent is “FFE4”.
 
![image](https://user-images.githubusercontent.com/61798852/125418023-80273324-0516-4e41-b8db-898e8fecb084.png)


Find addresses in the module which can be used as a pointer. 

![image](https://user-images.githubusercontent.com/61798852/125418034-5409a974-8569-462c-a317-70cb720c963d.png)

 
Prepare your script with the address. Test if it works.
Search for “625011AF” in the immunity panel and hit F2 to set it as the breaking point.
 
 ![image](https://user-images.githubusercontent.com/61798852/125418054-7b14f1d9-4592-4d84-83b3-921e12055ad6.png)


If you run your script and it triggers immunity debugger, then it works.

_________________________________________________________________________________________________________________________________________________________________________________


7.	GAINING ROOT ACCESS WITH SHELLCODE

Use msfvenom to generate an exploit and add it to your script.

![image](https://user-images.githubusercontent.com/61798852/125418092-dcc18581-f07a-497a-ac79-6acb004b0a34.png)

 
Set up netcat to its default port 4444. If vulnserver connects due to our exploit, netcat will listen on port 4444 and it will appear here.

![image](https://user-images.githubusercontent.com/61798852/125418109-b86ba449-4f6d-411d-ac42-4f821ed6f848.png)

Vulnserver has been successfully exploited as we got the root.

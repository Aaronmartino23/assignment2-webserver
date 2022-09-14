# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=6789):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    
   
  
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
  
      message == connectionSocket.recv(1024)#Fill in end #
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:]) #fill in start #fill in end)
      #fill in end
      
      outputdata = f.read(1024)      #Fill in start -This variable can store your headers you want to send for any valid or invalid request. 
      #Content-Type above is an example on how to send a header as bytes
      #Fill in end

      #Send an HTTP header line into socket for a valid request.
       connectionSocket.sendall('HTTP/1.1 200 OK\r\n'.encode())
      #Fill in end

      #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
      # Send response message for invalid request due to the file not being found (404)
      #Fill in start
       connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())    
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()      #Fill in end
      
      except (ConnectionResetError, BrokenPipeError):
      pass      
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(6789)

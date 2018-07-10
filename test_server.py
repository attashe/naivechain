import pickle
from flask import Flask
from flask import request
import requests

from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def start():
	print(request.data)
	response = requests.get('http://127.0.0.1:5000/blocks')
	print(response.content)
	return "Hello world"

@app.route("/blocks", methods = ['GET'])
def getblocks():
	# print(request.data)
	# return str(blockchain.__dict__)
	return 


@app.route("/mineblocks", methods = ['POST'])
def mineblock():
	newBlock = generate_next_block(request)

@socketio.on('connection')
def connection_sock(message):
	sockets.append(ws);

    initMessageHandler(ws);
    initErrorHandler(ws);
	write(ws, queryChainLengthMsg())


 @socketio.on('message')
 def recv_message(message):
    print('Received message' str(message));
    if(message['type'] == MessageType['QUERY_LATEST']):
        emit(message);	
        case MessageType.QUERY_ALL:
            write(ws, responseChainMsg());
            break;
        case MessageType.RESPONSE_BLOCKCHAIN:
            handleBlockchainResponse(message);
            break;
    }
});

import socket
import datetime
import time
import hashlib
class Block:
    def __init__(self,index, previousHash, timestamp, data, hash_):
        self.index = index
        self.previousHash = str(previousHash)
        self.timestamp = timestamp
        self.data = data
        self.hash = str(hash_)
sockets = []
adresses = []  # [(ip, port), ...


MessageType = {
    "QUERY_LATEST": 0,
    "QUERY_ALL": 1,
    "RESPONSE_BLOCKCHAIN": 2
}
http_port = 3001
p2p_port = 6001
initialPeers = []
getGenesisBlock = lambda :Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7");
blockchain = [getGenesisBlock()]
hash(getGenesisBlock)

def broadcast(message):
	# sockets.forEach(socket => write(socket, message));
	for i in range(len(sockets)):
		s = sockets[i]
		s.connect(adresses[i][0], adresses[i][1])
		s.send(message)


def generateNextBlock(blockData):
    previousBlock = getLatestBlock();
    nextIndex = previousBlock.index + 1;
    nextTimestamp = int(time.time()) // 1000;
    nextHash = calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData);
    return Block(nextIndex, previousBlock.hash, nextTimestamp, blockData, nextHash);


def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data);

def calculateHash(index, previousHash, timestamp, data):
    m = hashlib.sha256()
    m.update(
        (str(index) + previousHash + str(timestamp) + data).encode('utf-8'))
    return m.hexdigest()

def addBlock(newBlock):
    if (isValidNewBlock(newBlock, getLatestBlock())):
        blockchain.push(newBlock)

def getLatestBlock():
	return blockchain[-1]


def isValidChain(blockchainToValidate):
    if (blockchainToValidate[0] == getGenesisBlock()):
        return false
    tempBlocks = [blockchainToValidate[0]]
    for i in range(1, len(blockchainToValidate)):
        if (isValidNewBlock(blockchainToValidate[i], tempBlocks[i - 1])):
            tempBlocks.push(blockchainToValidate[i])
        else:
            return False
    return True


def isValidNewBlock(newBlock, previousBlock):
    if (previousBlock.index + 1 != newBlock.index):
        print('invalid index');
        return False
    elif (previousBlock.hash != newBlock.previousHash):
        print('invalid previous hash')
        return False
    elif (calculateHashForBlock(newBlock) != newBlock.hash):
        print(type(newBlock.hash) + ' ' + type(calculateHashForBlock(newBlock)))
        print('invalid hash: ' + calculateHashForBlock(newBlock) + ' ' + newBlock.hash)
        return False
    return True


def replaceChain(newBlocks):
    if (isValidChain(newBlocks) and (len(newBlocks) > len(blockchain))):
        print('Received blockchain is valid. Replacing current blockchain with received blockchain');
        blockchain = newBlocks
        broadcast(responseLatestMsg())
    else :
        print('Received blockchain invalid')

def responseLatestMsg():
	return {
		    'type': MessageType.RESPONSE_BLOCKCHAIN,
		    'data': JSON.stringify([getLatestBlock()])
		    }


# websocket

lambda ws: str(ws.uri.WebSocketURI.host) + ':' + str(ws.uri.WebSocketURI.port)


if __name__ == '__main__': 
	app.run(host='127.0.0.0',port='5001')
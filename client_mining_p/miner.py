import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 
def proof_search(coins_mined):
    #this was my testing to get a hold of requests
    # res = requests.get('http://0.0.0.0:5000/chain')
    # res.json()
    # return res.json()['chain'][0]['proof']
    new_proof = 0
    searching = True
    r = requests.get('http://0.0.0.0:5000/last_proof')
    last_proof = r.json()['last_proof']
    while searching:
        validate_proof = requests.post('http://0.0.0.0:5000/mine',json={'proof':new_proof,'last_proof':last_proof})
    
        if str(validate_proof.json()["message"]) == "Failure":
            new_proof += 1
        else:
            
            print(f"Coins: {coins_mined}")
            searching = False
    
    
    

    




if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    
    print('searching...')
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        proof_search(coins_mined)
        coins_mined += 1

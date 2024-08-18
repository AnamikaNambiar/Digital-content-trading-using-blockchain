import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask import Flask, abort, send_file
from flask_script import Manager
from flask_cors import CORS
import os
import requests
import ipfshttpclient
import logging
# 0x5631352809adDdda2bdd0199de032dE8b2B0b964
from DBConnection import Db
app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
manager = Manager(app)

import json

from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = r"C:\Users\Archana\PycharmProjects\dctb\node_modules\.bin\build\contracts\dctb.json"
# Deployed contract address (see migrate command output: contract address)
deployed_contract_address = '0x5631352809adDdda2bdd0199de032dE8b2B0b964'

def download(url):
    h = {"Accept-Encoding": "identity"}
    r = requests.get(url, stream=True, verify=False, headers=h)
    try:
        r.raise_for_status()
        if "content-type" in r.headers:
            r.raise_for_status()
            if "content-type" in r.headers:
                return send_file(r.raw, mimetype=r.headers["content-type"])
    except requests.exceptions.HTTPError as e:
        return "IPFS Server Error! \n", 503
    return "File Download Error!", 500


@app.route("/down/<path:path>")
def down(path):
    try:
        p = os.path.splitext(path)
        hash = str(p[0])
        if not hash or not hash.startswith('Qm'):
            return "<Invalid Path>", 404
        url = app.config['IPFS_FILE_URL'] + hash
        print(url, "iii")
        return download(url)
    except Exception as e:
        print(e)
@app.route('/<filepath>/<lid>')
def hello_world(filepath, lid):
    # log.info("file name: {}".format(file.filename), {'app': 'dfile-up-req'})
    client = ipfshttpclient.connect(app.config['IPFS_CONNECT_URL'])
    res = client.add(filepath)
    # res = client.add(r"C:\Users\Archana\PycharmProjects\dctb\dctbapp\static\img\15022024-162614.jpg")
    url = app.config['DOMAIN'] + '/' + str(res['Hash'])


    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    db = Db()
    q = db.selectOne("select * from dctbapp_hashvalue where hashvalue='"+str(res['Hash'])+"'")
    if q is None:

        db.insert("insert into `dctbapp_hashvalue`(`id`,`hashvalue`,`LOGIN_id`) values ( NULL,'"+str(res['Hash'])+"','"+str(lid)+"');")
        message2 = contract.functions.addFile(int(lid),str(res['Hash']),str(datetime.datetime.now().date()),int(blocknumber)+1).transact()
        print(url)
        return url
    else:
        if str(lid) == str(q['LOGIN_id']):
            return "you"
        else:

            q2 = db.selectOne("select * from dctbapp_login where id ='"+str(q['LOGIN_id'])+"'")
            import smtplib

            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("dctb2022@gmail.com", "rzgx puuf sqtj fxbb")
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = "dctb2022@gmail.com"
            msg['To'] = q2['username']
            msg['Subject'] = "Alert message! Someone uploaded your same file"
            body = "Your file <br> <a href='http://127.0.0.1:5000/down/"+str(q['hashvalue'])+"'>Click here to view file</a>"
            msg.attach(MIMEText(body, 'html'))
            s.send_message(msg)

            return "no"



if __name__ == '__main__':
    app.run()

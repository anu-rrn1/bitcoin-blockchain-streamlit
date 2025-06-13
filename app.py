# app.py
import streamlit as st
from blockchain import BlockChain

# Session state for blockchain
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = BlockChain()

blockchain = st.session_state.blockchain

st.title("💰 Transfer of Bitcoins - Blockchain Demo")

# Form for transaction
st.header("📤 Add a Transaction")
sender = st.text_input("Sender")
recipient = st.text_input("Recipient")
amount = st.text_input("Amount (e.g., 2 BTC)")

if st.button("➕ Add Transaction"):
    if sender and recipient and amount:
        index = blockchain.new_transaction(sender, recipient, amount)
        st.success(f"✅ Transaction will be added to Block {index}")
    else:
        st.error("Please enter all fields!")

# Mine Block
st.header("⛏️ Mine New Block")
if st.button("⛏️ Mine Block"):
    previous_proof = blockchain.last_block['proof']
    proof = previous_proof + 1  # dummy proof for simulation
    block = blockchain.new_block(proof)
    st.success("✅ Block Mined!")
    st.json(block)

# Show Blockchain
st.header("📚 Current Blockchain")
if st.button("📜 Show Blockchain"):
    for block in blockchain.chain:
        st.write(f"### Block {block['index']}")
        st.json(block)

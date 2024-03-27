import payu_sdk

# Replace with your actual Payu credentials
PAYU_API_KEY = "3DNANNQaHu71Kv3f46vditCgSo"
PAYU_MERCHANT_ID = "PKm78vx9Hvv9431n76GzC833gB"

client = payu_sdk.payUClient({
    "key": PAYU_API_KEY,
    "salt": PAYU_MERCHANT_ID,
    "env": "https://test.payu.in/merchant/postservice.php?form=2"
  }
)
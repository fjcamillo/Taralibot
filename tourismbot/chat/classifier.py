training_Set = [
    'Hi',
    'Good Day',
    'Arrived',
    'Walked In',
    'I Just Arrived',
    'I want one mocha frapuccino',
    "nothing thanks.",
    "I'm back",
    "yes",
    "no",
    "I'm right here",
    "no, is there anything new to the menu?",
    "clicked the beverage",
    "ah yes. can I have the Menu again?",
    "ok,thanks.",
    "okay",
    "Nothing Thanks."
    "Checkout"
]

labels = [
    'Good Day, How can Taralibot help you today?',
    'Nice to see you again',
    'Hi, What can I get for you today, sir?',
    'Good morning! Can I take your order?',
    "Hi! Here's our service, you can now order. To order, Just click the item you are going to order. And the bill will go straight to your bank account.",
    "Ok. We recieved your order. Your order will be served to you within 3 minutes. Is there anything you want to add?",
    "ok sir, have a Good Day! Come Again.",
    "Welcome back. Do you want the usual?",
    "ok. your order will be ready in 3 minutes. Have a Good Day!, is there anthing else?",
    "ok sir, have a Good Day! Come Again.",
    "Welcome back mel. Do you want the usual?",
    "ok sir. Click the item that you want to order and it will be served to you",
    "Ok. We recieved your order. Your order will be served to you within 3 minutes. Is there anything you want to add?",
    "ok sir, here's the menu just the same process to add order.",
    "ok sir, we recieved your additional order, just wait for a few minutes and your order will be ready.",
    "Is there anything else?",
    "Thank you Sir, Have a Good Day! Come Again."
]

def getTrainSet():
    return training_Set

def getLabels():
    return labels
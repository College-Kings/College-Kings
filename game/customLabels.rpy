label checkReplies(contact=None, customMessage="I need to check my phone"):
    if not contact:
        return
    
    call screen phone
    if contact.getReplies():
        u customMessage
        return checkReplies(contact)
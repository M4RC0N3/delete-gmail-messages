import imaplib

gmail_server = 'imap.gmail.com'
gmail_port = 993

email = 'email address'
password = 'email-password'

imap_connection = imaplib.IMAP4_SSL(gmail_server, gmail_port)

imap_connection.login(email, password)

imap_connection.select('inbox')

status, message_ids = imap_connection.search(None, 'ALL')

if status == 'OK':
    for message_id in message_ids[0].split():
        imap_connection.store(message_id, '+FLAGS', '\\Deleted')

    imap_connection.expunge()
    print("All messages in the inbox have been successfully restored.")

imap_connection.close()
imap_connection.logout()

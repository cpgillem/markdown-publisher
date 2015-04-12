import mailer

mailing_list_filename = "mailing_list.json"

def read_json_mailing_list():
    print mailer.get_mailing_list(mailing_list_filename)

def get_meetings_mailing_list():
    print mailer.get_emails(mailer.get_mailing_list(mailing_list_filename), 'meetings')

get_meetings_mailing_list()

#!/usr/bin/python

'''
Computer Club of WMU Mailer
by cpg

This is a library of functions for managing an email list and sending out
emails to the proper list.

It uses a json file to store the email list in an array called "mailing_list".
This array is composed of objects containing a key for "email" and 
"subscriptions".
The "subscriptions" key has an array of subscriptions for its value. This
array's items should correspond to directories in the data directory in this
repo.
'''

import json

def load_mailing_list(mailing_list_filename):
    ''' Gets the mailing list from a json file. '''
    with open(mailing_list_filename, 'r') as mailing_list_file:
        return json.load(mailing_list_file)["mailing_list"]

def save_mailing_list(mailing_list, mailing_list_filename):
    ''' Saves a mailing list to a file, overwriting. '''
    with open(mailing_list_filename, 'w') as mailing_list_file:
        json.dump({mailing_list}, mailing_list_file)

def add_email(mailing_list, email):
    ''' Adds an email address to the mailing list, with no subscriptions. '''
    if email not in mailing_list:
        mailing_list.append({ "email": email, subscriptions: []})

def add_subscription(mailing_list, email, subscription):
    ''' Adds a subscription associated with the given email address. '''
    if email in mailing_list
    mailing_list[mailing_list.index(email)]["subscriptions"].append(subscription)

def remove_subscription(mailing_list, email, subscription):
    ''' Removes a subscription from the given email address. '''
    mailing_list[mailing_list.index(email)]["subscriptions"].

def get_emails(mailing_list, subscription):
    ''' Gets a list of emails that have signed up for a given subscription. '''
    # Array to hold email addresses
    emails = []

    # For ever email entry in the mailing list, check whether the subscription
    # is in the subscriptions array. If it is, add it to the emails list.
    for email_entry in mailing_list:
        if subscription in email_entry["subscriptions"]:
            emails.append(email_entry["email"])

    return emails

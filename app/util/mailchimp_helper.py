from mailchimp3 import MailChimp
from config import MAILCHIMP_USERNAME, MAILCHIMP_SECRET_KEY, MAILCHIMP_LISTS


def add_subscriber(email_address, list_name='Leads'):
    """
    Adds a user to the specified mailchimp list.

    :param email_address: str, Email address of the subscriber
    :param first_name: str, First name of the subscriber
    :returns: mailchimp subscriber response object
    """
    client = MailChimp(MAILCHIMP_USERNAME, MAILCHIMP_SECRET_KEY)
    list_id = MAILCHIMP_LISTS.get(list_name)

    client.lists.members.create(list_id, {
        'email_address': email_address,
        'status': 'subscribed',
    })

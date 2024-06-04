"""

The insurance guy calls again and apologizes.

They found another policy made by your spouse, but this one is limited to cover a particular maximum in losses (for
example, 50,000€).

You send a bill to your spouse for the difference you lost.

Given a dict of the stolen items and a limit, return the difference between the total value of those items and the
limit of the policy."""


def calc_diff(obj, limit):
    total = sum(list(obj.values()))

    return total - limit

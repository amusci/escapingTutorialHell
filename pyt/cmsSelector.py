'''

Write a function that takes a list of strings and a pattern (string) and returns the strings that contain the pattern in alphabetical order.

If the pattern is an empty string, return all the strings passed in the input list.

cms_selector(["WordPress", "Joomla", "Drupal"], "w") ➞ ["WordPress"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "ru") ➞ ["Drupal"]

cms_selector(["WordPress", "Joomla", "Drupal", "Magento"], "") ➞ ["Drupal", "Joomla", "Magento", "WordPress"]

'''


def cms_selector(lst, txt):
    if not txt:
        return sorted(lst)
    ans = []

    for i in lst:
        if txt in i.lower():
            ans.append(i)
    return sorted(ans)
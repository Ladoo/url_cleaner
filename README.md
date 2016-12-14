# Squid URL Cleaner

This little utility will remove any marketing parameters from URLs, which will ensure
that your pages get cached in Squid.

For example, a page with the following query parameters:

```bash
http://mywebsite.com.au/search?query=test&utm_source=Marketo&mkt_token=...very long and constantly changing token...
```

Will never get cached, due to the fact that mkt_token will change for every each session / user.

With this program, these pages will get cached based on the following key:

```bash
http://mywebsite.com.au/search?query=test
```

## Installation

```bash
# Login as root
sudo su -

# Navigate to the squid directory
cd /etc/squid/

# Pull in code from git repo, alternatively you'll need to manually transfer all files into this folder
git clone --depth 1 https://github.com/Ladoo/url_cleaner.git

# Give Squid ownership of these files
chown -R squid:squid url_cleaner/

# Give users execute access to the squid_url_cleaner program
chmod +x url_cleaner/squid_url_cleaner.py

# Verify unit tests
python -m unittest url_cleaner/url_cleaner_test
```

Add the following configuration entries into your /etc/squid/squid.conf file:

```bash
# Create ACL to capture only URLs with a query string (?something) that will be passed to url cleaner
acl URLS_WITH_PARAMS url_regex \?.*

# Program to pass urls for cleaning : This program must be accessible and executable by user running squid process usually 'squid'
url_rewrite_program /etc/squid/url_cleaner/squid_url_cleaner.py

# Helps with scalability, you can decrease or increase this value as you see fit
url_rewrite_children 12

# Allow rule for passing all the urls captured via the acl 'URLS_WITH_UTM_PAR' to url_rewrite_program
# This combined with acl configuration makes sure only 'required' urls are passed to url_cleaner
url_rewrite_access allow URLS_WITH_PARAMS
```

Reload Squid:

```bash
# <= CentOS 5 / RHEL 5
service squid reload

# >= Centos 6 / RHEL 6
systemctl reload squid
```

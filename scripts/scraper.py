#!/usr/bin/env python

import mechanize

basepage = 'https://www.research.gov/grfp/AwardeeList.do?method=loadAwardeeList'

br = mechanize.Browser()
br.set_handle_robots(False)
br.open(basepage)


br.select_form('awardeeListForm')
control = br.form.find_control('awardYear')
award_type = br.form.find_control('awardType')

for itm in control.items[1:]:
    br.select_form('awardeeListForm')
    control = br.form.find_control('awardYear')
    print itm
    br[control.name] = [itm.name]
    #br[award_type.name] = ['H']
    response = br.submit()
    # now in specific year
    exp = br.links()[12] # excel export link
    req = br.click_link(exp)
    resp = br.follow_link(exp)
    open('../data/%s-grfp.data' % itm.name.replace('*', ''), 'w').write(resp.read())
    br.back()

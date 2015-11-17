from selenium import webdriver
import sqlite3


# Create a Chrome instance
co = webdriver.ChromeOptions()
# Save all user data (cookies) in a database
co.add_argument("--user-data-dir=userdir")
# Create a WebDriver instance
browser = webdriver.Chrome(chrome_options=co)


sites = {
    'komplett.no': 'http://www.komplett.no',
    'blivakker.no': 'http://www.blivakker.no',
    'nelly.com': 'http://www.nelly.com',
    'apotek1.no': 'http://www.apotek1.no',
    'ark.no': 'http://www.ark.no',
    'blush.no': 'http://www.blush.no',
    'brandos.no': 'http://www.brandos.no',
    'cdon.no': 'http://www.cdon.no',
    'clasohlson.no': 'http://www.clasohlson.no',
    'coolstuff.no': 'http://www.coolstuff.no',
    'coverbrands.no': 'http://www.coverbrands.no',
    'dustinhome.no': 'http://www.dustinhome.no',
    'elkjop.no': 'http://www.elkjop.no',
    'ellos.no': 'http://www.ellos.no',
    'enklereliv.no': 'http://www.enklereliv.no',
    'expert.no': 'http://www.exptert.no',
    'footway.no': 'http://www.footway.no',
    'godtlevert.no': 'http://www.godtlevert.no',
    'gymgrossisten.no': 'http://www.gymgrossisten.no',
    'hm.com': 'http://www.hm.com',
    'ikea.no': 'http://www.ikea.no',
    'interflora.no': 'http://www.interflora.no',
    'jollyroom.no': 'http://www.jollyroom.no',
    'kolonial.no': 'http://www.kolonial.no',
    'kondomeriet.no': 'http://www.kondomeriet.no',
    'lefdal.no': 'http://www.lefdal.no',
    'lekmer.no': 'http://www.lekmer.no',
    'lensit.no': 'http://www.lensit.no',
    'miinto.no': 'http://www.miinto.no',
    'mpx..no': 'http://www.mpx.no',
    'netonnet.no': 'http://www.netonnet.no',
    'nethandelen.no': 'http://www.netthandelen.no',
    'retthjem.no': 'http://www.retthjem.no',
    'sportmann.no': 'http://www.sportmann.no',
    'vinmonopolet.no': 'http://www.vinmonopolet.no',
    'stormberg.com': 'http://www.stormberg.com',
    'stylepit.no': 'http://www.stylepit.no',
    'zalando.no': 'http://www.zalando.no',
    'zara.no': 'http://www.zara.no',
    'x-life.no': 'http://www.x-life.no',
}


for site in sites:
    # Visit one page once
    browser.get(sites[site])
    browser.implicitly_wait(1000)
# Close the browser
browser.quit()

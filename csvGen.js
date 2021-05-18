const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {

    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://bet.szerencsejatek.hu/jatekok/putto/sorsolasok/');

    const linkSelector = "body > div.main-container > div.wrapper > div > div.grid.grid-twothird.wrap > div.box.draw-information.clear.ng-scope > form > nav > ul > li.next > a"

    await page.waitForSelector(linkSelector);


    await page.evaluate(() => {
        let year = document.getElementById('year')
        let week = document.getElementById('week')
        let day = document.getElementById('day')
        year.value = "2015"
        week.value = "5"
        day.value = "5"
    });


    await Promise.all([
        page.click(linkSelector),
        page.waitForNavigation({ waitUntil: 'networkidle2' })
    ]);

    await page.screenshot({
        path: 'screenshot.png'
    })

    for (var i = 0; i < 10000; i++) {

        const data = await page.evaluate(() => {
            const rows = document.querySelectorAll('table tbody tr');
            return [].slice.call(rows)
                .map(function (row) {
                    // Query all cells
                    const cells = row.querySelectorAll('td');
                    return [].slice.call(cells)
                        .map(function (cell) {
                            return cell.textContent.replace(/\s+/g, '');
                        })
                        .join(';');
                })
                .join('\n');
        });


        fs.writeFile('./csvs/gyorsabb' + i + '.csv', data, err => {
            if (err) {
                console.error(err)
                return
            }
            //file written successfully
        })

        await page.waitForSelector(linkSelector);
        await Promise.all([
            page.click(linkSelector),
            page.waitForNavigation({ waitUntil: 'domcontentloaded' })
        ]);

    }
    await browser.close()


})();




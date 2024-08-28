/**
 * ---------------------------------------
 * This demo was created using amCharts 5.
 *
 * For more information visit:
 * https://www.amcharts.com/
 *
 * Documentation is available at:
 * https://www.amcharts.com/docs/v5/
 * ---------------------------------------
 */

// Create root and chart
var root = am5.Root.new("chartdiv"); 



// Set themes
root.setThemes([
  am5themes_Dark.new(root),
]);

var chart = root.container.children.push(
  am5map.MapChart.new(root, {
    panX: "rotateX",
    projection: am5map.geoNaturalEarth1()
  })
);

// Create polygon series
var polygonSeries = chart.series.push(
  am5map.MapPolygonSeries.new(root, {
    geoJSON: am5geodata_worldLow,
    exclude: ["AQ"]
  })
);

polygonSeries.mapPolygons.template.setAll({
  tooltipText: "{name}",
  templateField: "polygonSettings",
});

polygonSeries.mapPolygons.template.states.create("hover", {
  fill: am5.color(0x677935)
});

polygonSeries.mapPolygons.template.events.on("click", async function (ev) {
  await getCountryInfo(ev, ev.target.dataItem.dataContext.id)
})

const getCountryInfo = async (e, id) => {
	try {
		const res = await fetch("/countries")
		const data = await res.json()

    if (data) {
      country = data[e.target.dataItem.dataContext.id]
			const info_header = document.querySelector("#info-header")
      info_header.textContent = `${country["Name"]}`

      const info_body = document.querySelector("#info-body")
      info_body.innerHTML = `
        <strong>Official Name:</strong>
        <span class="official-name">${country["Official Name"]}</span> <br />
        <strong>Population:</strong>
        <span class="population">${country["Population"]}</span> <br />
        <strong>Continent:</strong>
        <span class="continent">${country["Continent"]}</span> <br />
        <strong>Flag:</strong>
        <a href=${country["Flag"]} target="_blank">
          <span class="flag"
            ><img
              class="country-flag"
              src=${country["Flag"]}
              alt="The Flag of ${country["Official Name"]}"
          /></span>
        </a>
      `
      const newsCard = document.querySelector("#news-card")
      newsCard.classList.add("card")
      let spinner = `
        <div class="spinner-grow text-primary m-2 mx-auto" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      `  
      newsCard.innerHTML = setNewsContent(e.target.dataItem.dataContext.name, spinner)
      newsItems = await getNews(id)
      newsCard.innerHTML = setNewsContent(e.target.dataItem.dataContext.name, newsItems)
		} else {
			alert("Could not get country info.")
		}
	} catch (err) {
		console.log(err)
	}
}

const getNews = async (id) => {
  let newsItems = ""
  
  try {
    const res = await fetch(`/news/${id}`)
    const data = await res.json()

    

    if (data.length == 0) {
      newsItems = `<div class="list-group-item">No covid news for this country.</div>`
    } else {

      data.forEach(item => {
        newsItems += `<a
            href="${item.Url}" target="_blank"
            class="list-group-item list-group-item-action"
            >${item.Title}<br>
            <small class="text-muted">by ${item["Clean Url"]} </small>
            </a
          >`
      })
    }
    
    return newsItems
  
  } catch (err) {
    console.log(err)
    newsItems = `<div class="list-group-item">Could not get covid news for this country.</div>`
    return newsItems
  }
  
}

const setNewsContent = (name, content) => {
  html = `
      <h5 class="card-header" id="info-header">
        ${name} Covid News
      </h5>
      <div
        class="list-group card-body p-0 m-0 news-card-body"
      >
        ${content}
      </div>
    `
  return html
}




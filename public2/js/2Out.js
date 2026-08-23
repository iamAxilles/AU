
const ls = (location.search).substr(0,wls.indexOf("-"));

async function output(SR) {
  const dataEl = document.querySelector('data'); 
  dataEl.innerHTML = '';

  // translate badges in parallel
  const badgeEnList = await Promise.all(
    SR.map(sr => google1(sr.Badge))
  );

  dataEl.innerHTML = SR.map((sr, i) => `
    <output>
      <a href="/car${ls}#${sr.Id}" target="_blank">
        <img src="${sr.image_data}">
        <img src="${sr.image_data2}">
      </a>
      <ul>
        <li>« ${badgeEnList[i]} »</li>
        <li>₩${(sr.Price * 10000).toLocaleString()}</li>
        <li>${(sr.Mileage).toLocaleString()}km</li>
        <li>${sr.Year / 100}</li>
      </ul>
    </output>
  `);

  console.log(SR.length);

  window.scrollTo(0, 600);
  document.querySelector("select[name='sort']").style.visibility = 'visible';
}

window.sorts = {

    dates: (RR) => { RR.sort((s, r) => new Date((r.ModifiedDate).slice(0,19)) - new Date((s.ModifiedDate).slice(0,19))); output(RR); },

    pricelow: (RR) => { RR.sort((s, r) => s.Price - r.Price); output(RR); },

    kmlow: (RR) => { RR.sort((s, r) => s.Mileage - r.Mileage); output(RR);  }

  };

const cache = new Map();

async function google1(T) {
  const key = T.trim();        

  if (cache.has(key)) return cache.get(key);

  const p = (async () => {
    const url =
      "https://translate.googleapis.com/translate_a/single" +
      "?client=gtx&sl=ko&tl=en" +
      "&dt=t&format=json&q=" + encodeURIComponent(key);

    const res = await fetch(url);
    const data = await res.json();

    return data?.[0]?.[0]?.[0] ?? ""; })();

  cache.set(key, p);
  return p;
}




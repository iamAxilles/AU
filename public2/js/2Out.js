
const ls = (location.search).substr(0,wls.indexOf("-"));

async function output(SR) {

  const badgeEnList = await Promise.all(
    SR.map(sr => translate(sr.Badge))
  );

  const dataEl = document.querySelector('data'); 
  dataEl.innerHTML = '';

  dataEl.innerHTML = SR.map((sr, i) => 
    `<output>
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
    </output>`);

  console.log(SR.length);

  window.scrollTo(0, 600);
  document.querySelector("select[name='sort']").style.visibility = 'visible';

}

window.sorts = {

    dates: (RR) => { RR.sort((s, r) => new Date((r.ModifiedDate).slice(0,19)) - new Date((s.ModifiedDate).slice(0,19))); output(RR); },

    pricelow: (RR) => { RR.sort((s, r) => s.Price - r.Price); output(RR); },

    kmlow: (RR) => { RR.sort((s, r) => s.Mileage - r.Mileage); output(RR);  }

  };


// const cache = new Map();

// async function google1(T) {
//   const key = T.trim();        

//   if (cache.has(key)) return cache.get(key);

//   const p = (async () => {
//     const url =
//       "translate.googleapis.com/translate_a/single" +
//       "?client=gtx&sl=ko&tl=en" +
//       "&dt=t&format=json&q=" + encodeURIComponent(key);

//     const res = await fetch(url);
//     const data = await res.json();

//     return data?.[0]?.[0]?.[0] ?? ""; })();

//   cache.set(key, p);
//   return p;
// }

const translationCache = new Map();

async function translate(text, sourceLang = 'ko', targetLang = 'en') {
    const cacheKey = JSON.stringify({
        text
    });

    // Перевод уже есть в кэше или запрос выполняется
    if (translationCache.has(cacheKey)) {
        return translationCache.get(cacheKey);
    }

    const params = new URLSearchParams({
        q: text,
        langpair: `${sourceLang}|${targetLang}`
    });

    const request = fetch(
        `https://api.mymemory.translated.net/get?${params}`
    )
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            if (data.responseStatus === 200) {
                return data.responseData.translatedText;
            }

            throw new Error(data.responseDetails || text);
        })
        .catch(error => {
            // Ошибочные запросы не оставляем в кэше
            translationCache.delete(cacheKey);
            throw error;
        });

    // Сохраняем Promise, чтобы объединить одинаковые параллельные запросы
    translationCache.set(cacheKey, request);
    // console.dir(translationCache);
    // console.info(cacheKey)
    return request;
} 
//https://lilting.ch/en/articles/mymemory-api





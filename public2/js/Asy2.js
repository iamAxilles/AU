    let wls = window.location.search;

    let wla = l => window.location.assign(l);


    (async function(link) {
        let fe = await fetch(link, {
            method: 'GET',
            credentials: 'include'
        })
            let FER = await fe.json();
         //SRjson = JSON.parse(FER);
        localStorage.setItem("1st", wls);

        try { sorts.dates(FER); }
        catch (err) { console.log(err); }


    //function KZ(v) {
    //            var fed = FER.filter(ff => ff.Model.includes(v)); output(fed); return fed };
//
   //$(`select.kuzova`).change(function(){var kuval=$(this).val();console.log(kuval);
    //            KZ(kuval);
    //    });
        

    $(`select[name='sort']`).change(function(){var sor = $(this).val() //console.info(sor)
            switch (sor){
                case 'updated':
                    sorts.dates(FER);
                    localStorage["sort"] = "updated"
                    break;
                case 'pricelow':
                    sorts.pricelow(FER);
                    localStorage["sort"] = "pricelow"
                    break;
                case 'kmlow':
                    sorts.kmlow(FER);
                    localStorage["sort"] = "kmlow"
                    break;
              }

    });

    const Storage = localStorage['sort'];
        switch (Storage){
            case 'updated':
                sorts.dates(FER);
            $('select[name="sort"]').val("pricelow");
                        break;
            case 'pricelow':
                sorts.pricelow(FER);
            $('select[name="sort"]').val("pricelow");
                        break;
            case 'kmlow':
                sorts.kmlow(FER);
            $('select[name="sort"]').val("kmlow");
                        break;
        }

    return FER })('/cars/'+wls.slice(1));






   /*function KZ(v) { const REF = asy2('/cars/' + wls.slice(1) );
                    let fed = REF.filter(ff => ff.Model.includes(v) ); output(fed); }*/

    $(`select.kuzova`).change(function(){var kuval=$(this).val(); console.info(kuval);
        //Asy2('/cars/'+wls.slice(1,-1) + kuval)
        // kuval==`Generation`? wla(wls.slice(0,-2)+wls.substr(-2)) :
        //  ses = sessionStorage.getItem("1st")
        //    kuval==`Generation`? wla(ses + wls.substr(-2) ):
             wla(`/vehs?`+wls.substr(1,wls.indexOf("-")) + kuval +`/1`);
                //KZ(kuval);
        });




    //const butt = document.createElement('button');butt.innerHTML='click';butt.onclick=()=>
    //$('.section').append(butt);



//const wlSS = window.location.search;
    //switch (wlSS){
    //    case wlSS.includes('?bmw=3'):
    //        $('select.kuzova option:contains("Generation")').prop('selected', true)
    //    //f05f.classList.replace("u-section-1", "bmw3");
    //        break
    //    case wlSS=`?bmw=3-G20`:
    //        $('select.kuzova option:contains("G20")').prop('selected', true)
    //        break
    //    case wlSS=`?bmw=3-F30`:
    //        $('select.kuzova option:contains("F30")').prop('selected', true)
    //        break
    //    case wlSS=`?bmw=3-E90`:
    //        $('select.kuzova option:contains("E90")').prop('selected', true)
    //        break
    //    } //для перекидывания ссылки в кузове

const WL$ = window.location.search;

const f05f = document.getElementById('sec-f05f');

//let autos = window.location.hash.slice(1);
//window.res = await G(`/${autos}`);

//let currentUrl = new URL('http://127.0.0.1:33/vehs');

//BMW
$(`#3Series`).click(async() => {
    //let cars = await G(`bmw/3`);
    //    SR = cars.SearchResults;
    //
    //      outputting(SR);

    //currentUrl.searchParams.set(`bmw`, `3`);
    //    history.pushState({}, '', currentUrl);
    window.location.assign('vehs?bmw=3-er/1')
    });

  if (WL$.includes(`bmw=3`) ) { f05f.style.backgroundImage = "url('../css/images/bmw3pics/30.jpg')";
      $(`.kuzova`).append(`
          <option>G20</option>
          <option>F30</option>
          <option>E90</option>
          <option><2006</option>
          `)
  } if (WL$.includes('G20') ) { f05f.style.backgroundImage = "url('../css/images/bmw3pics/g20/20.webp')";
    $('select.kuzova option:contains("G20")').prop('selected', true)
  } if (WL$.includes('F30') ) { f05f.style.backgroundImage = "url('../css/images/bmw3pics/f30/303.jpg')";
    $('select.kuzova option:contains("F30")').prop('selected', true)
  } if (WL$.includes('E90') ) { f05f.style.backgroundImage = "url('../css/images/bmw3pics/e90/907.jpg')";
    $('select.kuzova option:contains("E90")').prop('selected', true)
  };


$(`#5Series`).click(async()=>{
    //let cars = await G(`vehi/${moden}/${idd}`);

        window.location.assign('/vehs?bmw=5')

    });
if (WL$.includes(`bmw=5`) ) { f05f.style.backgroundImage = "url('../css/images//')";
        $(`.kuzova`).append(`
            <option>G60</option>
            <option>G30</option>
            <option>F10</option>
            <option>E60</option>
            <option><2003</option>
            `) }
      if (WL$.includes('G60') ) { f05f.style.backgroundImage = "url('../css/images//')";
      $('select.kuzova option:contains("G60")').prop('selected', true)
    } if (WL$.includes('G30') ) { f05f.style.backgroundImage = "url('../css/images//')";
      $('select.kuzova option:contains("G30")').prop('selected', true)
    } if (WL$.includes('F10') ) { f05f.style.backgroundImage = "url('../css/images//')";
      $('select.kuzova option:contains("F10")').prop('selected', true)
    } if (WL$.includes('E60') ) { f05f.style.backgroundImage = "url('../css/images//')";
      $('select.kuzova option:contains("E60")').prop('selected', true)
    };


$(`#X5`).click(async()=>{

    window.location.href = `/vehs?/bmw/X5`;
    //window.location.reload();
    //console.log(autos)

    $(`.kuzova`).append(`
            <option>E53</option>
            <option>E70</option>
            <option>F15</option>
            <option>G05</option>
            `)
    })
//-----------------------------------------------------------------------------------------------
//Mercedes-benz
// $(`#C-klasse`).click(async()=>{

        // window.location.assign('/vehs?benz=C-kl/1')

    // });
if (WL$.includes(`Mercedes=C`) ) { f05f.style.backgroundImage = "url('../css/images/benzCpics/C.jpeg')";
        $(`.kuzova`).append(`
            <option>W206</option>
            <option>W205</option>
            <option>W204</option>
            <option>2007</option>

            `) };
      if (WL$.includes('W206') ) { //f05f.style.backgroundImage = "url('../css/images/benzCpics/')";
      $('select.kuzova option:contains("W206")').prop('selected', true)
    } if (WL$.includes('W205') ) { //f05f.style.backgroundImage = "url('../css/images/benzCpics/')";
      $('select.kuzova option:contains("W205")').prop('selected', true)
    } if (WL$.includes('W204') ) { //f05f.style.backgroundImage = "url('../css/images/benzCpics/')";
      $('select.kuzova option:contains("W204")').prop('selected', true)
    } if (WL$.includes('<07') ) { f05f.style.backgroundImage = "url('../css/images/benzCpics/')";
      $('select.kuzova option:contains("<07")').prop('selected', true)
    };
/*window.C_klasse = {
    W206: (RR) => { w206 = RR.filter(rr => rr.Model.includes('W206')); output(w206); }
    ?
};*/

/* Chevrolet */
// $tb = $("ul.Chevy li").attr('text','Trailblazer');
// $tb.click(async() => {
//     window.location.assign('vehs?chevy=trailblazer-gm/1')
//     });
  if (WL$.includes(`Chevy=Trailblazer`) ) { f05f.style.backgroundImage = "url('../css/images/chevy/tb24.jpg')";
      $(`.kuzova`).append(`
          <option value="20">2020</option>
          <option value="23">2023</option>
          `)
  } if (WL$.includes('23') ) { f05f.style.backgroundImage = "url('../css/images/Chevy/.webp')";
    $('select.kuzova option:contains("G20")').prop('selected', true)
  }

    document.querySelectorAll('#list .menu-item a').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const ul = a.closest('ul');

      $CL = ul?.className;
      $DS = a.getAttribute('datasrc');

      location.assign(`vehs?${$CL}=${$DS}/1`);
    });
  });
  // $("ul#list").click(function () {
  //   $ulClass = $(this).prop('className')
  //   console.log( $ulClass )
  // })
  // $(".menu-item a").click(function () {
  //   $ulA = $(this).attr('datasrc')
  //   console.log( $ulA );
  // })


//$('a').click(function(event) { return false; });  // Прокрутки не будет

//window.onbeforeunload = () => sessionStorage.setItem('scrollPos', window.scrollY);
//window.onload = () => window.scrollTo(0, sessionStorage.getItem('scrollPos') || 0);

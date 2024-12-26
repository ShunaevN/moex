const securityBlock = document.querySelector(".main_security_block");
const securityTemplate = document.querySelector("#security_template");
const crossBlock = document.querySelector(".main_cross_block");
const crossTemplate = document.querySelector("#cross_template");

getSecurities()
function getSecurities() {
    fetch('/api/securities', {
    headers : {
        'Content-Type' : 'application/json'
        },
    method : 'GET'})
    .then(function (response){
        if(response.ok) {
            response.json()
            .then(function(response) {
                for (let key in response) {
                    // клонируем и заполняем template команд
                    const clone = securityTemplate.content.cloneNode(true);
                    let id = clone.querySelector(".security_template_id");
                    let secid = clone.querySelector(".security_template_secid");
                    let regnumber = clone.querySelector(".security_template_regnumber");
                    let name = clone.querySelector(".security_template_name");
                    let emitent_title = clone.querySelector(".security_template_emitent_title");

                    id.textContent = response[key].id;
                    secid.textContent = response[key].secid;
                    regnumber.textContent = response[key].regnumber;
                    name.textContent = response[key].name;
                    emitent_title.textContent = response[key].emitent_title;

                    securityBlock.appendChild(clone);
                }
            })
        }
        else {
            throw Error('Something went wrong');
        }
    })
    .catch(function(error) {
        console.log(error);
  })
}

getCross()
function getCross() {
    fetch('/api/cross', {
    headers : {
        'Content-Type' : 'application/json'
        },
    method : 'GET'})
    .then(function (response){
        if(response.ok) {
            response.json()
            .then(function(response) {
                for (let key in response) {
                    // клонируем и заполняем template команд
                    const clone = crossTemplate.content.cloneNode(true);

                    let secid = clone.querySelector(".cross_template_secid");
                    let regnumber = clone.querySelector(".cross_template_regnumber");
                    let name = clone.querySelector(".cross_template_name");
                    let emitent_title = clone.querySelector(".cross_template_emitent_title");

                    let tradedate = clone.querySelector(".cross_template_tradedate");
                    let numtrade = clone.querySelector(".cross_template_numtrade");
                    let open = clone.querySelector(".cross_template_open");
                    let close = clone.querySelector(".cross_template_close");

                    secid.textContent = response[key].secid;
                    regnumber.textContent = response[key].regnumber;
                    name.textContent = response[key].name;
                    emitent_title.textContent = response[key].emitent_title;

                    tradedate.textContent = response[key].tradedate;
                    numtrade.textContent = response[key].numtrade;
                    open.textContent = response[key].open;
                    close.textContent = response[key].close;

                    crossBlock.appendChild(clone);
                }
            })
        }
        else {
            throw Error('Something went wrong');
        }
    })
    .catch(function(error) {
        console.log(error);
  })
}
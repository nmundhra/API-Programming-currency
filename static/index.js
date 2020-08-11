document.addEventListener('DOMContentLoaded', () => {

//function to get exchange rate from Euro to any other currency
  document.querySelector('#form').onsubmit = () => {

    const request = new XMLHttpRequest();
    const type = document.querySelector('#currency').value;
    request.open('POST', '/convert');

    request.onload = () => {

      const data = JSON.parse(request.responseText);

      if (data.success) {
        const contents = `1 EUR is equal to ${data.rate} ${type}.`
        document.querySelector('#result').innerHTML = contents;
      }
      else {
        document.querySelector('#result').innerHTML = ` ${data.error}`
      }
    }

    const data = new FormData();
    data.append('currency', type);

    request.send(data);
    return false;
  };
//function #form close

//function to convert the currency to any amount
  document.querySelector("#conrate").onsubmit = () => {

    const from = document.querySelector("#cur1").value;
    const to = document.querySelector("#cur2").value;
    const amt = document.querySelector("#amt").value;

    const xhtml = new XMLHttpRequest();
    xhtml.open('POST', '/getamount');

    xhtml.onload = () => {
      //add the code once the route is defined in application.py
      const data = JSON.parse(xhtml.responseText);

      if (data.success) {
        document.querySelector("#amt").value = `${data.result}`
      }
      else {
        document.querySelector("#result1").innerHTML = `${data.error}`
      }
    }
    const data = new FormData();
    data.append('from_cur', from);
    data.append('to_cur', to);
    data.append('amount', amt);

    xhtml.send(data);
    return false;
  };
//function #conrate close


//function to get the historical rate and display on the screen
  document.querySelector("#hist").onsubmit = () => {

    const symbol = document.querySelector("#symbol").value;
    const todate = document.querySelector("#date").value;

    const xhtml = new XMLHttpRequest();
    xhtml.open('POST', "/historydata");

    xhtml.onload = () => {
      const data = JSON.parse(xhtml.responseText);
      if (data.success) {
        const result = `1 EUR is equal to ${data.result} ${symbol} on ${todate}.`
        document.querySelector("#result2").innerHTML = result;
      }
      else {
        document.querySelector("#result2").innerHTML = `${data.error}`;
      }
    }

    const data = new FormData();
    data.append("symbol", symbol);
    data.append("todate", todate);

    xhtml.send(data);
    return false;

  };

});

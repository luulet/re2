const target = document.querySelector('#target');

 const f = document.createTextNode('First item');
 const s = document.createTextNode('Second item');
 const t = document.createTextNode('Third item');
const first = document.createElement('li');
first.appendChild(f);
target.appendChild(first);

const second = document.createElement('li');
second.appendChild(s);
target.appendChild(second);

const third = document.createElement('li');
third.appendChild(t);
target.appendChild(third);
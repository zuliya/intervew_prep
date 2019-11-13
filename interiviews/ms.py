def func_a(a):
    print(a)

print(func_a("aedfw"))


// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution() {
    var elements_td = document.getElementsByTagName("td");
    for (var i=0; i<elements_td.length; i++)
    {
        if (elements_td[i].style.backgroundColor != elements_td[i].style.color){
            final_string += elements_td[i].textContent
        }
    }
    return final_string
}

template: `

          < input  # newHero
          (keyup.enter) = "addHero(newHero.value)"
(blur) = "addHero(newHero.value); newHero.value='' " >

         < button(click) = "addHero(newHero.value)" > Add < / button >

                                                              < ul > < li * ngFor = "let hero of heroes" > {
    {hero}} < / li > < / ul >

                         `,
                         styles: [`
.is -done
{
    text - decoration: line - through;
}
`]
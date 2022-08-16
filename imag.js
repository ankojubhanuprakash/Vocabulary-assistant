function hi(){
    console.log('boo')
}
servelist = ['spbq01.jpg', 'tasq01.jpg', 'vcaa01.jpg', 'hurd01.jpg', 'pjbh01.jpg', 'jlnr01.jpg', 'szng01.jpg', 'ukqu01.jpg', 'bfam01.jpg',
            'dfpm01.jpg', 'pnzs01.jpg', 'ttna02.jpg', 'fapu02.jpg', 'odzm02.jpg', 'srnz02.jpg', 'glrq02.jpg', 'uyml02.jpg', 'aebh02.jpg',
            'ohop02.jpg', 'qiyk02.jpg', 'gzbb02.jpg', 'txes02.jpg', 'bden02.jpg', 'suhi03.jpg', 'btpw03.jpg', 'faue03.jpg', 'gkcv03.jpg',
            'zedy03.jpg', 'rroz03.jpg', 'knis03.jpg', 'vzfo03.jpg', 'zcey03.jpg', 'nkya03.jpg', 'ufcx04.jpg', 'iklv04.jpg', 'lrkn04.jpg',
            'ykfz04.jpg', 'lkiv04.jpg', 'qnfu04.jpg', 'edln04.jpg', 'wxrn04.jpg', 'ooyb04.jpg', 'egss05.jpg', 'lmxj05.jpg', 'deqd05.jpg',
            'svdi05.jpg', 'yfsg05.jpg', 'ymut05.jpg', 'szql05.jpg', 'oosd05.jpg', 'axeb05.jpg', 'vneh05.jpg', 'hkzs06.jpg', 'tsdc06.jpg', 
            'inak06.jpg', 'rwwc06.jpg', 'wdqi06.jpg','ypoi06.jpg', 'frsw06.jpg', 'lqxq06.jpg', 'gtck06.jpg', 'mtpe06.jpg', 'ijvk07.jpg', 
            'wmkp07.jpg', 'sgbt07.jpg', 'nklw07.jpg', 'agwe07.jpg', 'ijkh07.jpg', 'vfko07.jpg', 'srqj07.jpg', 'jfqo07.jpg', 'zetn07.jpg', 
            'byop07.jpg', 'jiif07.jpg', 'makm08.jpg', 'zmpu08.jpg', 'wyly08.jpg', 'dagl08.jpg', 'qcso08.jpg', 'blgq08.jpg', 'hnwn08.jpg', 
            'hufz08.jpg', 'mpoi08.jpg', 'vusi09.jpg', 'rcvm09.jpg', 'kiiq09.jpg', 'isph09.jpg', 'opru09.jpg', 'ibft09.jpg', 'qeym09.jpg',
            'swur09.jpg', 'axak10.jpg', 'stjh10.jpg', 'utvt10.jpg', 'hmfo10.jpg', 'zbre10.jpg', 'tpxk10.jpg', 'umlz10.jpg', 'pwnj10.jpg', 
            'zlvk10.jpg']



var lv = document.getElementById('lv');
var rv = document.getElementById('rv');
alert(lv.innerText)
console.log(lv.innerText)
//output.innerHTML = slider.value;
loader()  

lv.addEventListener('change',()=>{
    console.log('hi')
    loader()})
rv.addEventListener('change',()=>{loader()})




function loader(){
    lreq = parseInt(lv.innerText)
    rreq = parseInt(rv.innerText)
    console.log(lreq,rreq)
    
    i=0 
    document.querySelector('.image_container').innerHTML=' '
    servelist.forEach((element) => {
        
        elemval= parseInt(element.slice(4,6))
        //console.log(elemval)
        if (elemval <= rreq && elemval >= lreq){
            console.log(element)
            document.querySelector('.image_container').innerHTML +=`<div id="block_${i}" class="block" ><img src = "imagsrc/${element}"></img></div>`
        } 
        
    });
}            

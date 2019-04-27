let X  = function (data){
    console.log(data)
    var produtos=[]
    produtos=data;

    function oldprice(antigo){
        if (antigo == null){
            return '';
        } else {
            return 'De'+' '+antigo;
        }        
    }
    function produtosTemplate(produtos){
        return `
        <div class="div-carousel-slide"> 
            <ul class="lista-carousel-slide">
                <li class= "lista">   
                    <img classs="correção" src="${produtos.imageName}">
                    <h2>${produtos.name}<h2/>
                    <span>${oldprice(produtos.oldPrice)}</span>
                    <span class="span">Por ${produtos.price}</span>
                    <span class="span">${produtos.productInfo.paymentConditions}</span>
                <li/>
            <ul>
        </div>
        `
    }
    document.getElementById("carousel-container").innerHTML = `
        ${produtos.data.recommendation.map(produtosTemplate).join('')}
        <button id="prevBtn">Prev</button>
        <button id="nextBtn">Next</button>
    `
}


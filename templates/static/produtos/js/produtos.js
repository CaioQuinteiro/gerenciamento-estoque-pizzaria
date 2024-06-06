function exibir_form(tipo){

    add_produto = document.getElementById('add-produto')
    att_produto = document.getElementById('att-produto')

    if(tipo == "1"){
        att_produto.style.display = "none"
        add_produto.style.display = "block"
    }else if(tipo == "2"){
        add_produto.style.display = "none"
        att_produto.style.display = "block"
    }

}

function dados_produto(){
    produto = document.getElementById('produto-select')

    fetch("/produtos/atualiza_produto/", {
        method: "POST",
        headers: {
            pass
        }
    })
}
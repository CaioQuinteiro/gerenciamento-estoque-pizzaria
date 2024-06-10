function exibir_form(tipo){

    add_produto = document.getElementById('add-produto')
    att_produto = document.getElementById('att-produto')
    lista_produto = document.getElementById('lista-produto')

    if(tipo == "1"){
        att_produto.style.display = "none"
        add_produto.style.display = "block"
        lista_produto.style.display = "none"
    }else if(tipo == "2"){
        add_produto.style.display = "none"
        att_produto.style.display = "block"
        lista_produto.style.display = "none"
    }else if(tipo == "3"){
        add_produto.style.display = "none"
        att_produto.style.display = "none"
        lista_produto.style.display = "block"
    }

}

function dados_produto(){
    produto = document.getElementById('produto-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_produto = produto.value

    data = new FormData()
    data.append('id_produto', id_produto)

    fetch("/produtos/atualiza_produto/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-produto').style.display = 'block'

        id = document.getElementById('id')
        id.value = data['produto_id']

        nome = document.getElementById('nome')
        nome.value = data['produto']['nome']

        descricao = document.getElementById('descricao')
        descricao.value = data['produto']['descricao']

        qtde_estoque = document.getElementById('qtde_estoque')
        qtde_estoque.value = data['produto']['qtde_estoque']

        unidade_medida = document.getElementById('unidade_medida')
        unidade_medida.value = data['produto']['unidade_medida']

    })
}

function update_produto(){
    id = document.getElementById('id').value
    nome = document.getElementById('nome').value
    descricao = document.getElementById('descricao').value
    qtde_estoque = document.getElementById('qtde_estoque').value
    unidade_medida = document.getElementById('unidade_medida').value

    fetch('/produtos/update_produto/' + id, {
        method: 'POST', 
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            descricao: descricao,
            qtde_estoque: qtde_estoque,
            unidade_medida: unidade_medida
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if (data['status'] == '200'){
            nome = data['nome']
            descricao = data['descricao']
            qtde_estoque = data['qtde_estoque']
            unidade_medida = data['unidade_medida']
            console.log('Dados alterados com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }
        
    })
}
function exibir_form(tipo){

    add_fornecedor = document.getElementById('add-fornecedor')
    att_fornecedor = document.getElementById('att-fornecedor')
    lista_fornecedor = document.getElementById('lista-fornecedor')

    if(tipo == "1"){
        att_fornecedor.style.display = "none"
        add_fornecedor.style.display = "block"
        lista_fornecedor.style.display = "none"
    }else if(tipo == "2"){
        add_fornecedor.style.display = "none"
        att_fornecedor.style.display = "block"
        lista_fornecedor.style.display = "none"
    }else if(tipo == "3"){
        add_fornecedor.style.display = "none"
        att_fornecedor.style.display = "none"
        lista_fornecedor.style.display = "block"
    }

}

function dados_fornecedor(){
    fornecedor = document.getElementById('fornecedor-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_fornecedor = fornecedor.value

    data = new FormData()
    data.append('id_fornecedor', id_fornecedor)

    fetch("/fornecedores/atualiza_fornecedor/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(){
        document.getElementById('form-att-fornecedor').style.display = 'block'

        id = document.getElementById('id')
        id.value = data['fornecedor_id']

        nome = document.getElementById('nome')
        nome.value = data['fornecedor']['nome']

        email = document.getElementById('email')
        email.value = data['fornecedor']['email']

        telefone = document.getElementById('telefone')
        telefone.value = data['fornecedor']['telefone']

    })
}

function update_fornecedor(){
    id = document.getElementById('id').value
    nome = document.getElementById('nome').value
    email = document.getElementById('email').value
    telefone = document.getElementById('telefone').value

    fetch('/fornecedores/update_fornecedor/' + id, {
        method: 'POST', 
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            email: email,
            telefone: telefone,
        })

    }).then(function(result){
        return result.json()
    }).then(function(data){

        if (data['status'] == '200'){
            nome = data['nome']
            email = data['email']
            telefone = data['telefone']
            console.log('Dados alterados com sucesso')
        }else{
            console.log('Ocorreu algum erro')
        }
        
    })
}
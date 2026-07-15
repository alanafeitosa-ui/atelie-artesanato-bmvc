(function () {
    if (typeof io === "undefined") return;

    const socket = io();

    socket.on("connect", () => atualizarIndicadorConexao(true));
    socket.on("disconnect", () => atualizarIndicadorConexao(false));

    socket.on("estoque_atualizado", (dados) => {
        if (!dados || dados.id === undefined || !dados.tipo) return;
        if (dados.tipo === "produto") {
            atualizarEstoqueProduto(dados.id, dados.estoque);
        } else if (dados.tipo === "materia_prima") {
            atualizarEstoqueMateria(dados.id, dados.estoque);
        }
    });

    function atualizarEstoqueProduto(produtoId, novaQuantidade) {
        const span = document.querySelector(`[data-estoque-produto="${produtoId}"]`);
        if (!span) return;
        span.textContent = novaQuantidade;
        destacarElemento(span.closest(".card"));
    }

    function atualizarEstoqueMateria(materiaId, novaQuantidade) {
        const span = document.querySelector(`[data-estoque-materia="${materiaId}"]`);
        if (!span) return;
        span.textContent = novaQuantidade;

        const card = span.closest(".card");
        destacarElemento(card);

        if (card) {
            const minimo = parseFloat(card.dataset.minimo || "0");
            if (parseFloat(novaQuantidade) <= minimo) {
                card.classList.add("estoque-baixo");
            } else {
                card.classList.remove("estoque-baixo");
            }
        }
    }

    function destacarElemento(elemento) {
        if (!elemento) return;
        elemento.classList.remove("card-atualizado");
        void elemento.offsetWidth;
        elemento.classList.add("card-atualizado");
    }

    function atualizarIndicadorConexao(conectado) {
        let indicador = document.getElementById("status-tempo-real");
        if (!indicador) {
            indicador = document.createElement("div");
            indicador.id = "status-tempo-real";
            document.body.appendChild(indicador);
        }
        indicador.textContent = conectado ? "● Tempo real ativo" : "○ Reconectando...";
        indicador.className = conectado ? "conectado" : "desconectado";
    }
})();
## 🧠 - Proposta do Desafio
O desafio consistia em implementar um algoritmo em linguagem de programação que encontrasse o caminho de um ponto A para um ponto B em uma matriz tridimensional. O objetivo era encontrar o caminho mais curto possível utilizando o menor número de movimentos.

- **Instrutor**: Sergio Yoshioka 
- **Matéria**: Teoria da Computação e Complexidade de Algoritmos 


## 💭 - Metodologia
Para resolver o problema, usamos a heurística de Manhattan e o algoritmo A*.
A heurística de Manhattan mede a distância entre dois pontos em uma grade.O algoritmo A* é uma das melhores soluções para encontrar o caminho mais curto em um grafo. 

Representamos o grafo do algoritmo como uma matriz em Python, onde cada elemento representava um ponto na matriz. O algoritmo A* recebeu a lista de pontos, o ponto de partida e o ponto de destino. Ele usa uma lista de prioridade para armazenar os pontos a serem analisados. Essa lista é ordenada pelo custo estimado do caminho mais curto do ponto de partida até o ponto atual, adicionado com a heurística de Manhattan. Em cada iteração, o algoritmo remove o ponto de menor custo da lista de prioridade e verifica se ele é o ponto de destino.


## 🌱 - Conclusão

A metodologia utilizada se mostrou bastante eficiente para encontrar o caminho mais curto em uma matriz realizado em testes de uma matriz de 1000x1000x1000. A heurística de Manhattan combinada com o algoritmo A* proporcionou um bom desempenho e eficiência. O algoritmo pode ser utilizado em diferentes aplicações, como jogos, robótica e planejamento de rotas.

## 💬 - Recursos

- https://dicionariotec.com/public_html/index.php/posts/algoritmo-a-a-estrela
- https://iq.opengenus.org/manhattan-distance/
- https://www.redblobgames.com/pathfinding/a-star/introduction.html
- https://www.geeksforgeeks.org/a-search-algorithm/

## 💬 - Contato

Desenvolvido por Pedro Abel

- **Email**: pedrooabell@gmail.com
- **Linkedin**: https://www.linkedin.com/in/pedro-abel/
- **Perfil do Github**: https://github.com/pedroabel

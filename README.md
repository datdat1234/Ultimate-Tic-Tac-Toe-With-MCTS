# Ultimate-Tic-Tac-Toe With MCTS

This project aims to use the MCTS (Monte Carlo Tree Search) algorithm to compete against a random strategy during the gameplay of Ultimate Tic-Tac-Toe.

## Requirements

This project requires Python 3.11.

## Usage

To run the project with visualization:

```sh
python test_game.py
```

To run the project with command line result:

```sh
python main.py
```
## Optimization

### Exploration Parameter c

You can leverage your heuristic experience or strategy to determine the appropriate value for 'c', which will yield distinct results. For this project, I have opted to utilize the value of 'c' as the square root of 2 (sqrt(2)).

### Simulation Number simulation_no

If you have a more powerful computer (than mine :D), you can try this project with a higher simulation number. It would definitely yield better results.

## References

I would like to extend my sincere gratitude and appreciation to:

* [MCTS explaination with Ultimate Tic-Tac-Toe](https://ai-boson.github.io/mcts/)
* [MCTS presentation MIT](https://www.youtube.com/watch?v=xmImNoDc9Z4)
* [PHƯƠNG PHÁP CẢI TIẾN HIỆU QUẢ CÂY TÌM KIẾM MONTE CARLO](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/view/2329)
import random


class Minesweeper:
    """
    Minesweeper game representation.
    """

    def __init__(self, height=8, width=8, mines=8):
        self.height = height
        self.width = width

        self.board = []
        for _ in range(self.height):
            self.board.append([False] * self.width)

        self.mines = set()
        while len(self.mines) != mines:
            i = random.randrange(self.height)
            j = random.randrange(self.width)

            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                print("|X" if self.board[i][j] else "| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """
        count = 0

        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue

                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence:
    """
    Logical statement about a Minesweeper game.

    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return set(self.cells)

        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return set(self.cells)

        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI:
    """
    Minesweeper game player.
    """

    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width

        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)

        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)

        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def _remove_empty_and_duplicate_sentences(self):
        """
        Removes sentences that no longer contain cells and removes
        exact duplicates from the knowledge base.
        """
        cleaned_knowledge = []

        for sentence in self.knowledge:
            if not sentence.cells:
                continue

            if sentence not in cleaned_knowledge:
                cleaned_knowledge.append(sentence)

        changed = len(cleaned_knowledge) != len(self.knowledge)
        self.knowledge = cleaned_knowledge
        return changed

    def _infer_until_stable(self):
        """
        Repeatedly applies direct and subset-based inference until no
        additional knowledge can be derived.
        """
        changed = True

        while changed:
            changed = self._remove_empty_and_duplicate_sentences()

            newly_safe = set()
            newly_mined = set()

            for sentence in self.knowledge:
                newly_safe.update(sentence.known_safes())
                newly_mined.update(sentence.known_mines())

            newly_safe -= self.safes
            newly_mined -= self.mines

            if newly_safe or newly_mined:
                changed = True

                for safe in newly_safe:
                    self.mark_safe(safe)

                for mine in newly_mined:
                    self.mark_mine(mine)

                continue

            inferred_sentences = []
            knowledge_snapshot = list(self.knowledge)

            for first in knowledge_snapshot:
                for second in knowledge_snapshot:
                    if first is second:
                        continue

                    if first.cells < second.cells:
                        difference_cells = second.cells - first.cells
                        difference_count = second.count - first.count

                        if not 0 <= difference_count <= len(difference_cells):
                            continue

                        new_sentence = Sentence(difference_cells, difference_count)

                        if (
                            new_sentence not in self.knowledge
                            and new_sentence not in inferred_sentences
                        ):
                            inferred_sentences.append(new_sentence)

            if inferred_sentences:
                self.knowledge.extend(inferred_sentences)
                changed = True

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function:
          1) marks the cell as a move that has been made,
          2) marks the cell as safe,
          3) adds a new sentence based on the cell and count, and
          4) marks any additional cells as safe or as mines, and
             adds any new sentences to the AI's knowledge base.
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)

        unknown_neighbors = set()
        adjusted_count = count
        row, column = cell

        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                neighbor = (i, j)

                if neighbor == cell:
                    continue

                if not (0 <= i < self.height and 0 <= j < self.width):
                    continue

                if neighbor in self.mines:
                    adjusted_count -= 1
                elif neighbor not in self.safes:
                    unknown_neighbors.add(neighbor)

        if unknown_neighbors:
            new_sentence = Sentence(unknown_neighbors, adjusted_count)

            if (
                0 <= adjusted_count <= len(unknown_neighbors)
                and new_sentence not in self.knowledge
            ):
                self.knowledge.append(new_sentence)

        self._infer_until_stable()

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must not already have been made.

        This function may use the knowledge in self.mines,
        self.safes, and self.moves_made, but should not modify
        any of those sets.
        """
        available_safe_moves = self.safes - self.moves_made

        if available_safe_moves:
            return next(iter(available_safe_moves))

        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        The move must not have been made already and must not be
        a cell known to be a mine.
        """
        possible_moves = []

        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)

                if cell not in self.moves_made and cell not in self.mines:
                    possible_moves.append(cell)

        if possible_moves:
            return random.choice(possible_moves)

        return None

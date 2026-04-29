#  CineGraph — Movie Recommendation System

> **Algorithms & Data Structures — Final Project**
> Al-Farabi Kazakh National University | 2024–2025


##  Team
| Name | Country |
|------|---------|
| Mahmudul Hasan Niloy | 🇧🇩 Bangladesh |
| Myeirim Khairat | 🇲🇳 Mongolia |
| Sayed Rahmat | 🇦🇫 Afghanistan |

**Supervisor:** Ualiyeva Irina Maratovn

##  What This Project Does

A fully functional movie recommendation engine built from scratch using:
- **Hash Tables** — O(1) movie storage and rating updates
- **FIFO Queue** — Bounded viewing history (last 5 films)
- **Graph + BFS** — Genre-based recommendation engine


##  Project Files

| File | Description |
|------|-------------|
| `Final_Project.html` | Interactive website — open in any browser |
| `Final_Project` | Complete Python source code |
| `Final_Project.docx` | Full technical report |



##  Data Structures Used

| Component | Structure | Complexity |
|-----------|-----------|------------|
| Movie storage | Hash Table (dict) | O(1) lookup |
| Viewing history | FIFO Queue (deque) | O(1) enqueue |
| Recommendations | Graph + BFS | O(V+E) |
| Rating system | Aggregated Model | O(1) update |
| Top-5 ranking | Timsort | O(n log n) |

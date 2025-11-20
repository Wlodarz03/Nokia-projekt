# Cheat-sheet Openspec, Speckit i BMAD
Ten plik to krótki overview każdej z tych trzech metod. Jest bardzo nieszczegółowy; po więcej informacji można wejść w linki pod każdą z metod.

# Openspec
[github](https://github.com/Fission-AI/OpenSpec)


Spec-driven workflow. Idea to:
1. AI pisze *proposal*.
2. My robimy review i ew. tweaksy.
3. AI implementuje ten proposal
4. Archiwizacja zmian (taki swego rodzaju commit)


Komendy dostępne dla nas:
- /openspec:proposal
- /openspec:apply
- /openspec:archive

# Speckit
[github](https://github.com/github/spec-kit)

[ok artykuł o tej metodzie](https://virtuslab.com/blog/ai/spec-kit-tames-ai-coding-chaos/)


1. **Specify**: definiujemy *co* i *dlaczego*. Robimy to używając komendy `/specify` wraz z opisem funkcjonalności. Po tym jak to zrobimy mamy plik `spec.md`.
2. **Plan**: definiujemy *jak* dany cel ma być osiągnięty. Używamy komendy `/plan`. Dostajemy potem pliki `plan.md`, `data-model.md` oraz `api-spec.json`. Reprezentują one techniczny plan implementacji.
3. **Tasks**: Używając komendy `/tasks`, dostajemy `plan.md` w którym mamy listę kroków aby zaimplementować plan.
4. **Implement**: Wrzucamy do AI kroki zdefiniowane w `plan.md` i weryfikujemy output.

# BMAD
[github](https://github.com/bmad-code-org/BMAD-METHOD)

[quick start guide z GH](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/modules/bmm/docs/quick-start.md)

Idea: Jest to metoda do większych projektów. Dostajemy 12 agentów, którzy reprezentują różne role projektowe. Rozwijamy projekt tak, jakbyśmy zarządzali grupą specjalistów.


Workflow *(wzięty z quick start guide)*:
- Phase 1: Analysis (Optional) - Brainstorming, Research, Product Brief
- Phase 2: Planning (Required) - Create your requirements (tech-spec or PRD)
- Phase 3: Solutioning (Track-dependent) - Design the architecture for BMad Method and Enterprise tracks
- Phase 4: Implementation (Required) - Build your software Epic by Epic, Story by Story


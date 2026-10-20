# 🎓 Sistema de Gestão Acadêmica

## 📋 Documentação de Validação dos Dados

**Tecnologias:** Python · Arquivos TXT

**Objetivo:** Documentar as regras de validação dos dados do sistema.

---

## 📑 Sumário

1. [Equipe ALFA — Alunos e Cursos](#-1-equipe-alfa--alunos-e-cursos)
2. [Equipe BETA — Professores e Disciplinas](#-2-equipe-beta--professores-e-disciplinas)
3. [Regras Gerais](#-3-regras-gerais)
4. [Conclusão](#-4-conclusão)

---

## 👥 1. Equipe ALFA — Alunos e Cursos

### 🧑‍🎓 Classe Aluno

| Campo | Tipo | Validação |
|---|---|---|
| Matrícula | `str` | De 6 a 12 dígitos, sem duplicidade. |
| Nome | `str` | De 3 a 100 caracteres. |
| CPF | `str` | CPF válido com 11 dígitos. |

### 📚 Classe Curso

| Campo | Tipo | Validação |
|---|---|---|
| Código | `int` | Maior que zero, sem duplicidade. |
| Nome | `str` | De 3 a 100 caracteres. |
| Modalidade | `str` | `Presencial` ou `EAD`. |

---

## 👨‍🏫 2. Equipe BETA — Professores e Disciplinas

Documentação das regras de validação de professores e disciplinas.

---

## 🛡️ 3. Regras Gerais

- Nenhum campo obrigatório pode ficar vazio.
- Códigos e matrículas não podem se repetir.
- CPF e e-mail devem ser válidos.
- Os dados devem ser validados antes de serem salvos.

---

## ✅ 4. Conclusão

O sistema busca garantir dados consistentes, confiáveis e organizados.

---

📌 **Projeto acadêmico desenvolvido em Python, com arquivos TXT.**

# AGENTS.md - High-Fidelity Federated Node: Trabajo Social

> Este repositorio es un Nodo Puro de Nivel 5 bajo la Arquitectura Federada v8.1.5.
> Opera bajo la Constitución centralizada en:
> `/home/erick-fcs/Capital_Workstation/capital-workstation-libs/.github/copilot-instructions.md`

## 1. Identidad y Gobernanza del Nodo

| Campo | Valor |
| --- | --- |
| **Nodo** | Trabajo Social |
| **Estado** | Activo - Fase de Creación |
| **Carrera** | Trabajo Social (Nodo Académico Independiente) |
| **Biblioteca Central** | `ecs_quantitative` (capital-workstation-libs) |
| **Nivel de Inteligencia** | 5 - Ecosistema Inteligente con Autonomía Controlada |
| **Gatekeeper** | `tests/system/test_architecture.py` |
| **RAG** | `global_knowledge` (Vector Store Federado) |

## 2. Capacidades de Inteligencia Avanzada (v1.0)

Este nodo está diseñado para la gestión del conocimiento y soporte en Trabajo Social:

1. **Gestión Documental y Literatura**: Indexación y estructuración de libros, lecturas y leyes aplicables al Trabajo Social.
2. **Consumo de Memoria RAG**: Acceso integrado a la base de conocimiento global a través del exocórtex.
3. **Escritura e Informes Académicos**: Generación de reportes de investigación y narrativas en formato APA 7 usando Quarto.

## 3. Arquitectura de Carpetas (Nivel 5)

```text
.
├── docs/
│   ├── vaults/            # Talleres, casos y reportes estructurados por ciclo
│   │   ├── ciclo_01/      # Tareas y proyectos del Primer Ciclo
│   │   └── ciclo_02/      # Tareas y proyectos del Segundo Ciclo
│   ├── writing/           # Capa narrativa y entregables en formato Quarto (TIC.qmd, PIIC.qmd)
│   ├── readings/          # Bóveda de literatura, artículos y libros en PDF
│   ├── management/        # Planificación, arquitectura local y hoja de ruta
│   └── syllabus/          # Sílabo de la materia y guía curricular
├── src/                   # Lógica reutilizable y procesamiento de datos
├── scripts/               # Scripts de soporte y tareas de mantenimiento
├── tests/                 # Gatekeepers de calidad y cumplimiento de arquitectura
└── AGENTS.md              # Este archivo de gobernanza
```

## 4. Estrategia de Resiliencia y Leyes Operativas

1. **Aislamiento**: Ningún script de análisis (`.py`) debe flotar en la raíz; la lógica operativa se mantiene en `src/` o en los scripts estructurados.
2. **Soberanía de Rutas**: Todas las rutas de archivos deben ser dinámicas usando `pathlib`, no hardcodeadas.
3. **Control del Exocórtex**: Toda literatura en PDF en `readings/` debe ser indexada formalmente en la base de datos central antes de considerarse lista.

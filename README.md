# Nodo Académico de Trabajo Social

Este repositorio es un nodo federado autónomo diseñado para gestionar tareas, documentación, lecturas y trabajos académicos relacionados con la carrera de **Trabajo Social**.

## Estructura de Trabajo
El nodo sigue estrictamente la arquitectura de **Nivel 5**:
- `docs/vaults/`: Unidades de análisis, casos de estudio y talleres prácticos.
- `docs/readings/`: Biblioteca de literatura en Trabajo Social y PDFs de referencia.
- `docs/writing/`: Reportes de Quarto e informes listos para entrega.
- `docs/management/`: Planificación y gestión administrativa del nodo.

## Uso del Entorno
Este proyecto utiliza `uv` como gestor de paquetes y dependencias. Para sincronizar el entorno local:
```bash
uv sync
```
Y para verificar la integridad del nodo:
```bash
uv run pytest
```

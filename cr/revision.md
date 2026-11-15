# Revisión de la versión v1.1 (checklist y hallazgos)

| Criterio | Resultado |
|---|---|
| IDs con el formato de la convención | 100% (sin errores en el reporte) |
| Cobertura de RF con la cadena completa | 13 de 13 |
| RNF con prueba propia | 5 de 6 (RNF-05 se verifica con control de costo) |
| CR-01 con todos los campos de la plantilla | Sí |
| Artefactos afectados con versión nueva | 8 de 8 |
| Revisión hecha por una persona distinta del autor | No |

## Hallazgos y correcciones
- H-1: los RNF no tenían prueba propia → se definen CP-RNF01 a CP-RNF04 y CP-RNF06 (corregido).
- H-2: el Alcance (Paso 1, 1.2) no figura en los artefactos afectados por CR-01 → se recomienda incluirlo (pendiente).
- H-3: Entregable llegaría a 6 asociaciones directas con AccesoCliente → AccesoCliente consulta por dependencia (corregido).
- H-4: el efecto de CR-01 en el calendario no estaba calculado → C3 pasa de 4 a 6 semanas y T1 se desplaza 2 semanas (calculado).

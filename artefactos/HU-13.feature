# language: es
@HU-13 @RF-13
Característica: HU-13 Consultar estado de entregables con enlace seguro
  Como entidad cliente
  quiero consultar con un enlace seguro el estado de los entregables de mi contrato
  para dar seguimiento sin pedir informes

  Escenario: Consulta con enlace vigente
    Dado que Symmetry emitió un enlace vigente para el contrato
    Cuando la entidad cliente abre el enlace
    Entonces ve solo el estado y las fechas de los entregables del contrato
    Y no ve datos personales

  Escenario: Enlace vencido o alterado
    Dado que el enlace venció o fue alterado
    Cuando la entidad cliente intenta abrirlo
    Entonces el sistema rechaza el acceso

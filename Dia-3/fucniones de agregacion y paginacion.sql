-- FUNCIONES DE AGREGACION
-- agragados

use minimarket;

SELECT * FROM PRODUCTOS;

-- Para utilizar cualquier funcion de agregacion se tiene que indicar la clausula GROUP BY y esta clausula
-- servira para indicar como queremos que se realice la agrupacion antes de usar la funcion
-- si solamente queremos obtener un solo resultado entonces la clausula GROUP BY no se puede tomar en consideracion


SELECT catgeoria_id , AVG (PRECIO)
FROM PRODUCTOS
GROUP BY categoria_id;
-- 2  9.20 ....
-- MAX  el valior maximo de la columna
SELECT  MAX(PRECIO)
FROM PRODUCTOS;

-- MIN  el valior maximo de la columna
SELECT  MIN(PRECIO)
FROM PRODUCTOS;

-- COUNT (COLUMNA) CUENTA CUNATOS REGISTROS TENEMOS
SELECT COUNT(NOMBRE)
FROM PRODUCTOS;

-- SUM (COLUMNA) SUMA EL CONTENIDO DE ESA COLUMNA
-- PostgreSQL  oSQL devuelve error cuando se suma un valor que no es numerico
SELECT SUM(PRECIO)
FROM PRODUCTOS;

-- PAGINACION
-- SIRVE PARA DEVOLVER LA INFORMACION NECESARIA
SELECT * FROM PRODUCTOS
LIMIT 2
-- INDICA CUANTOS REGISTROS MOSTRARA POR PAGINA
OFFSET 0;
-- INIDCA CUANTOS REGISTROS NO SE MOSTRARAN Y SE SALTARAN AL SIGUIENTE

SELECT * FROM PRODUCTOS;


-- ORDENAMIENTO 
SELECT * FROM PRODUCTOS
ORDER BY  FECHA_VENCIMIENTO DESC, NOMBRE DESC;    -- ASC  > ASCENDETE  -- DESC > DESCENDENTE

-- EN MYSQL  obligatoriamnete para usar el OFfSET debemos inidcar el LIMIT
SELECT SUM(P.PRECIO) 
FROM PRODUCTOS AS P INNER JOIN CATEGORIAS AS C ON P.CATGEORIA_ID=C.ID
WHERE C.NOMBRE= "OTROS"
GROUP BY P.ID
ORDER BY FECHA_VENCIMIENTO DESC
LIMIT 1
OFFSET 0;


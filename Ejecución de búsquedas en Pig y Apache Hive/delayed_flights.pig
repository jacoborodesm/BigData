
-- registro de la librería PiggyBank
REGISTER piggybank.jar

-- Lectura CSV

AIRPORTS = LOAD '$airports_file' USING
    org.apache.pig.piggybank.storage.CSVExcelStorage(',','NO_MULTILINE','UNIX','SKIP_INPUT_HEADER')
    AS (airportid:chararray, city:chararray, state:chararray, airportname:chararray);

FLIGHTS = LOAD '$flights_file' USING
    org.apache.pig.piggybank.storage.CSVExcelStorage(',','NO_MULTILINE','UNIX','SKIP_INPUT_HEADER')
    AS (dayofmonth:int, dayofweek:int, carrier:chararray,
           depairport:chararray, arrairportid:chararray, depdelay:int, arrdelay:int);

-- Seleccionamos los vuelos retrasados
vuelos_retrasados = FILTER FLIGHTS BY arrdelay > 15;

-- Cuenta de los vuelos retrasados relacionandolos con la compañía
contar_retrasos = GROUP vuelos_retrasados BY carrier;
total_retrasos = FOREACH contar_retrasos GENERATE group AS carrier, COUNT(vuelos_retrasados) AS total_retrasos;

-- Ordenar DESC y limitar a 5 las compañías
top5_retrasos = ORDER total_retrasos BY total_retrasos DESC;
top5_retrasos = LIMIT top5_retrasos 5;

-- DUMP del resultado
DUMP top5_retrasos;


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
vuelos_retrasados = FILTER FLIGHTS BY depdelay > 15;

-- Seleccionamos los vuelos retrasados que llegaron sin retraso
vuelos_recuperados = FILTER vuelos_retrasados BY arrdelay <= 15;

-- Contamos los vuelos recuperados por cada compañía
contar_recuperados = GROUP vuelos_recuperados BY carrier;
total_recuperados = FOREACH contar_recuperados GENERATE group AS carrier, COUNT(vuelos_recuperados) AS vuelos_recuperados;

-- Contamos los vuelos retrasados por cada compañía
contar_retrasos = GROUP vuelos_retrasados BY carrier;
total_retrasos = FOREACH contar_retrasos GENERATE group AS carrier, COUNT(vuelos_retrasados) AS total_retrasos;

-- Calcular porcentaje de recuperación
recover = JOIN total_recuperados BY carrier, total_retrasos BY carrier;
recover = FOREACH recover GENERATE
    $0 AS carrier,
    ($1 * 1.0 / $3) AS recover;

-- Ordenar y limitar a 5 compañías
top5 = ORDER recover BY recover DESC;
top5 = LIMIT top5 5;

-- DUMP del TOP5
DUMP top5;

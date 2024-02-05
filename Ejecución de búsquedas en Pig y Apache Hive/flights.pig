
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

-- Nos quedamos con 10 aeropuertos
AIRPORTS_10 = LIMIT AIRPORTS 10;

-- Muestra de 10 aeropuertos
DUMP AIRPORTS_10;

-- Mismo procedimiento con los vuelos
FLIGHTS_10 = LIMIT FLIGHTS 10;
DUMP FLIGHTS_10;

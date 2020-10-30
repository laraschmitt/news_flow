
--- https://query.wikidata.org/ 
-- queries in SPARQL (SPARQL Protocol and RDF Query Language to shape and return linked data from a triplestore) 

SELECT DISTINCT ?city ?country ?countryLabel ?alpha2Code (LANG(?cityLabel) AS ?language) ?cityLabel ?cityCoords ?countryCoords ?population ?capitalLabel ?capitalLabela WHERE {
  ?city (wdt:P31/(wdt:P279*)) wd:Q515;
    wdt:P17 ?country.
  OPTIONAL { ?country rdfs:label ?countryLabel. }
  OPTIONAL { ?city rdfs:label ?cityLabel. }
  OPTIONAL { ?city wdt:P625 ?cityCoords. }
  OPTIONAL { ?country wdt:P625 ?countryCoords. }
  OPTIONAL { ?country wdt:P297 ?alpha2Code. }
  OPTIONAL { ?city wdt:P1082 ?population. }
  OPTIONAL { ?country wdt:P36 ?capitalLabel.}
  OPTIONAL { ?capitalLabel rdfs:label ?capitalLabela.}
}

                  
SELECT DISTINCT ?city ?country (lang(?cityLabel) AS ?language) ?cityLabel ?alpha2Code ?cityCoords
WHERE 
{
    ?city wdt:P31/wdt:P279* wd:Q515 .  # find instances of subclasses of city
    ?city wdt:P17 ?country .  # Also find the country of the city
    ?city rdfs:label ?cityLabel.
    ?country wdt:P297 ?alpha2Code.
    ?city wdt:P625 ?cityCoords
}

                  
SELECT ?city ?cityLabel  ?cityCoords ?population
WHERE 
{
    ?city wdt:P31/wdt:P279* wd:Q515 .  # find instances of subclasses of city
    ?city wdt:P625 ?cityCoords.
    ?city wdt:P1082 ?population.
    # choose language
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "en" .
    }
} 

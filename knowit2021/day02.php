<?php
function haversine($lon1, $lat1, $lon2, $lat2) {
    $lon1 = deg2rad($lon1);
    $lat1 = deg2rad($lat1);
    $lon2 = deg2rad($lon2);
    $lat2 = deg2rad($lat2);
    
    $dlon = $lon2 - $lon1;
    $dlat = $lat2 - $lat1;
    $a = sin($dlat/2)**2 + cos($lat1) * cos($lat2) * sin($dlon/2)**2;
    $c = 2 * asin(sqrt($a));
    $r = 6371;
    return $c * $r;
}
    

$fp = fopen("input/02", "rb");

$cities = [];
$skip = true;

while ($row = fgetcsv($fp)) {
    if ($skip) {
        $skip = false;
        continue;
    }
    
    $parts = explode(' ', $row[1]);
    $lon = explode('(', $parts[0])[1];
    $lat = explode(')', $parts[1])[0];
    
    $cities[$row[0]] = [
        'lat' => (double) $lat,
        'lon' => (double) $lon,
    ];
}

$current = ['lat' => 90, 'lon' => 0];
$distance = 0;

while ($cities) {
    $best_distance = 9999999999;
    $next_city = null;
    
    foreach ($cities as $city => $coords) {
        $this_dist = haversine($current['lon'], $current['lat'], $coords['lon'], $coords['lat']);
        
        if ($this_dist < $best_distance) {
            $best_distance = $this_dist;
            $next_city = $city;
        }
    }
    
    $distance += $best_distance;
    $current = $cities[$next_city];
    unset($cities[$next_city]);
    print("moving to " . $next_city . " " . $distance . " " . $best_distance . "\n");
}

$distance += haversine($current['lon'], $current['lat'], 0, 90);
print($distance);
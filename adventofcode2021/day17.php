<?php
$highest = [];
$unique = [];
$unique_s = [];

for ($x = 2; $x < 200; $x++) {
    for ($y = -200; $y < 200; $y++) {
        $x_v = $x;
        $y_v = $y;
        $x_pos = 0;
        $y_pos = 0;

        $best = 0;

        while (true) {
            $x_pos += $x_v;
            $y_pos += $y_v;

            if ($x_v > 0) {
                $x_v -= 1;
            }

            $y_v -= 1;

            if ($y_pos > $best) {
                $best = $y_pos;
            }

            if ($x_pos >= 150 && $x_pos <= 171 && $y_pos >= -129 && $y_pos <= -70) {
                $highest[] = $best;
                $unique[] = [$x_pos, $y_pos];
                $unique_s[] = $x_pos . ',' . $y_pos;
                break;
            }

            if ($x_pos > 171) {
                break;
            }

            if ($y_pos < -129) {
                break;
            }
        }
    }
}

print(max($highest) . ' - ' . count($unique) . ' - ' . count(array_unique($unique_s)));
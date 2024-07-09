d_coin = 25.75; // coin diameter, 22.5 for pound, 23.25 for 1 euro, 25.75 for 2 euros
t_coin = 2.2; // coin thickness, 3.15 for pound, 2.33 for 1 euro, 2.20 for 2 euros
d_hole = 7; // hole diameter
l_tail = 37; // distance from coin center to hole center
$fn = 150; // render quality

coinToken();

// functions
module coinToken()
{
  union(){
    difference()
    {
        // coin
        cylinder(h=t_coin, d=d_coin);

        // cutout
        translate([-(d_coin+1)/2,-d_coin,-0.5]) cube([d_coin+1,d_coin,t_coin+1]);
    }
    copyMirror() {
      hull() {
          translate([-d_coin*7/16,0,0]) cylinder(d=d_coin/8, h=t_coin);
          cylinder(d=d_coin/16, h=t_coin);
        }
    }
    difference() {
        translate([-d_coin/4,-d_coin/5,0]) cube([d_coin/2, d_coin/4 ,t_coin]);
      copyMirror(){
        translate([-d_coin/4.1,-d_coin/5.75,-0.5]) cylinder(d=d_coin/4, h=t_coin+1);
      }
    }
  }
  difference() {
    hull()
    {
      cylinder(h=t_coin, d=5.1);
      translate([0, -l_tail, 0]) cylinder(h=t_coin, d=13);
    }
    translate([0, -l_tail, -0.5]) cylinder(h=t_coin+1, d=6);
  }    
}

module copyMirror(vec=[1,0,0])
{
    children();
    mirror(vec) children();
}

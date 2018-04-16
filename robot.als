open util/ordering [time] as t
open util/ordering [coor] as c

--coordinates,strictly ordered 
sig time {}

sig coor {}
-- position models the individual position in the grid
sig position {x:coor,y:coor}

--four cardinal direction 
abstract sig direction {}

one sig north,south,east,west extends direction {}
some sig robot {
 --dierction rover is facing at any one time
 dir: direction one ->time,
--rovers position at any one time
 pos: position one ->time,
--rovers on/off status at any time 
 on: set time
}
pred turn_on [rov:robot,t,t':time]{
--pre condition
robot is off at time t(!is_on)
--post condition 
robot is on at time t'(is_on)

--Frame condition 

All other robot stay on or off they were(no_on_changes)
No other robot chenges direction(no_direction_changes)

}
pred show() {}

run show

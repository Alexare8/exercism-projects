#include "doctor_data.h"

heaven::Vessel::Vessel(std::string name, int generation, star_map::System system) {
    this->name = name;
    this->generation = generation;
    this->current_system = system;
}

heaven::Vessel heaven::Vessel::replicate(std::string new_name) {
    return heaven::Vessel(new_name, (generation + 1));
}

void heaven::Vessel::make_buster() {
    ++busters;
}

bool heaven::Vessel::shoot_buster() {
    if (busters > 0) {
        --busters;
        return true;
    }
    return false;
}

std::string heaven::get_older_bob(Vessel first, Vessel second) {
    if (first.generation > second.generation) {
        return second.name;
    }
    return first.name;
}
bool heaven::in_the_same_system(Vessel first, Vessel second) {
    return (first.current_system == second.current_system);
}
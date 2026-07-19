#if !defined(DOCTOR_DATA_H)
#define DOCTOR_DATA_H
#include <string>

namespace star_map {
    enum class System {
        AlphaCentauri,
        BetaHydri,
        DeltaEridani,
        EpsilonEridani,
        Sol,
        Omicron2Eridani
    };
}   // namespace star_map

namespace heaven {
    class Vessel {
        public:
            Vessel(std::string name, int generation,
                    star_map::System system = star_map::System::Sol);
            void make_buster();
            bool shoot_buster();
            Vessel replicate(std::string name);
    
            std::string name{};
            int generation{};
            star_map::System current_system;
            int busters{0};
            
    };
    std::string get_older_bob(Vessel first, Vessel second);
    bool in_the_same_system(Vessel first, Vessel second);
}   // namespace heaven
#endif
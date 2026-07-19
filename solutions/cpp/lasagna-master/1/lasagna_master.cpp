#include "lasagna_master.h"

namespace lasagna_master {

int preparationTime(const std::vector<std::string>& layers, int averageTime) {
    return layers.size() * averageTime;
}

amount quantities(const std::vector<std::string>& layers) {
    amount recipe{0, 0.0};
    for (std::string layer : layers) {
        if (layer == "noodles") {
            recipe.noodles += 50;
        }
        if (layer == "sauce") {
            recipe.sauce += 0.2;
        }
    }
    return recipe;
}

void addSecretIngredient(std::vector<std::string>& myRecipe, const std::vector<std::string>& friendRecipe) {
    myRecipe.back() = friendRecipe.back();
}

std::vector<double> scaleRecipe(const std::vector<double>& quantities, int portions) {
    std::vector<double> adjustedQuantities{};
    for (double quantity : quantities) {
        adjustedQuantities.emplace_back((quantity / 2 * portions));
    }
    return adjustedQuantities;
}

void addSecretIngredient(std::vector<std::string>& myRecipe, std::string secretIngredient) {
    myRecipe.back() = secretIngredient;
}
    
}  // namespace lasagna_master

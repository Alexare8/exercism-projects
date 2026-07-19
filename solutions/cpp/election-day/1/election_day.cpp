#include <string>
#include <vector>

namespace election {

// The election result struct is already created for you:

struct ElectionResult {
    // Name of the candidate
    std::string name{};
    // Number of votes the candidate has
    int votes{};
};

int vote_count(ElectionResult result) {
    return result.votes;
}

void increment_vote_count(ElectionResult& result, int votes) {
    result.votes = result.votes + votes;
}

ElectionResult& determine_result(std::vector<ElectionResult>& results) {
    int winnerIndex{0};
    for (int i{0}; i < results.size(); ++i) {
        if (results[i].votes > results[winnerIndex].votes) {
            winnerIndex = i;
        }
    }
    results[winnerIndex].name = "President " + results[winnerIndex].name;
    return results[winnerIndex];
}

}  // namespace election
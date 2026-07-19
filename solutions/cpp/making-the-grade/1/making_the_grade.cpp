#include <array>
#include <string>
#include <vector>

// Round down all provided student scores.
std::vector<int> round_down_scores(std::vector<double> student_scores) {
    std::vector<int> scores;
    for (int i{0}; i < student_scores.size(); ++i) {
        scores.emplace_back((int)student_scores.at(i));
    }
    return scores;
}

// Count the number of failing students out of the group provided.
int count_failed_students(std::vector<int> student_scores) {
    int fails{0};
    while (not student_scores.empty()) {
        if (student_scores.back() <= 40) {
            ++fails;
        }
        student_scores.pop_back();
    }
    return fails;
}

// Determine how many of the provided student scores were 'the best' based on the provided threshold.
std::vector<int> above_threshold(std::vector<int> student_scores, int threshold) {
    std::vector<int> best;
    for (int i{0}; i < student_scores.size(); ++i) {
        if (student_scores.at(i) >= threshold) {
            best.emplace_back(student_scores.at(i));
        }
    }
    return best;
}

// Create a list of grade thresholds based on the provided highest grade.
std::array<int, 4> letter_grades(int highest_score) {
    int interval{(highest_score - 40) / 4};
    int threshold{41};
    std::array<int, 4> grades;
    for (int i{0}; i < 4; ++i) {
        grades[i] = threshold + interval * i;
    }
    return grades;
}

// Organize the student's rank, name, and grade information in ascending order.
std::vector<std::string> student_ranking(std::vector<int> student_scores, std::vector<std::string> student_names) {
    std::vector<std::string> rankings;
    for (int i{0}; i < student_scores.size(); ++i) {
        rankings.emplace_back(std::to_string(i + 1) + ". " + student_names[i] + ": " + std::to_string(student_scores[i]));
    }
    return rankings;
}

// Create a string that contains the name of the first student to make a perfect score on the exam.
std::string perfect_score(std::vector<int> student_scores, std::vector<std::string> student_names) {
    for (int i{0}; i < student_scores.size(); ++i) {
        if (student_scores[i] == 100) {
            return student_names[i];
        }
    }
    return "";
}

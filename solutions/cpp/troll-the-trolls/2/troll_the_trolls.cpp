namespace hellmath {

enum class AccountStatus {
    troll, 
    guest,
    user,
    mod
};

enum class Action {
    read,
    write,
    remove
};

bool display_post(AccountStatus poster, AccountStatus viewer) {
    return (poster != AccountStatus::troll or poster == viewer);
}


bool permission_check(Action action, AccountStatus status) {
    switch (status) {
        case AccountStatus::mod:
            return true;
        case AccountStatus::user:
        case AccountStatus::troll:
            return (action != Action::remove);
        default:
            return (action == Action::read);
    }
}

bool valid_player_combination(AccountStatus p1, AccountStatus p2) {
    switch (p1) {
        case AccountStatus::guest:
            return false;
        case AccountStatus::troll:
            return (p2 == AccountStatus::troll);
        default:
            break;
    }
    switch (p2) {
        case AccountStatus::guest:
        case AccountStatus::troll:
            return false;
        default:
            return true;
    }
}

bool has_priority(AccountStatus p1, AccountStatus p2) {
    return p1 > p2;
}

}  // namespace hellmath
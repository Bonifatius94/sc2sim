from sc2sim import SC2Env

def test_should_respawn_beacon_on_environment_reset():
    env = SC2Env()
    state_before = env.state
    state_after = env.reset()
    assert(state_before.beacon_pos != state_after.beacon_pos \
        and state_before.marine_pos == state_after.marine_pos)

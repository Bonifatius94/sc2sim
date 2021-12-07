from sc2sim import SC2Env, SC2Action

def test_marine_should_initially_be_at_beacon():
    env = SC2Env()
    _, reward = env.step(SC2Action.BOT_LEFT)
    assert(reward == 1)

def test_marine_should_reach_lefthand_beacon_after_left_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(62, 64))
    _, reward = env.step(SC2Action.LEFT)
    assert(reward == 1)

def test_marine_should_reach_lefthand_beacon_after_topleft_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(62, 64))
    _, reward = env.step(SC2Action.TOP_LEFT)
    assert(reward == 1)

def test_marine_should_reach_lefthand_beacon_after_botleft_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(62, 64))
    _, reward = env.step(SC2Action.BOT_LEFT)
    assert(reward == 1)

def test_marine_should_reach_righthand_beacon_after_right_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(66, 64))
    _, reward = env.step(SC2Action.RIGHT)
    assert(reward == 1)

def test_marine_should_reach_righthand_beacon_after_topright_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(66, 64))
    _, reward = env.step(SC2Action.TOP_RIGHT)
    assert(reward == 1)

def test_marine_should_reach_righthand_beacon_after_botright_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(66, 64))
    _, reward = env.step(SC2Action.BOT_RIGHT)
    assert(reward == 1)

def test_marine_should_reach_bothand_beacon_after_bot_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 62))
    _, reward = env.step(SC2Action.BOT)
    assert(reward == 1)

def test_marine_should_reach_bothand_beacon_after_botright_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 62))
    _, reward = env.step(SC2Action.BOT_RIGHT)
    assert(reward == 1)

def test_marine_should_reach_bothand_beacon_after_botleft_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 62))
    _, reward = env.step(SC2Action.BOT_LEFT)
    assert(reward == 1)

def test_marine_should_reach_tophand_beacon_after_top_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 66))
    _, reward = env.step(SC2Action.TOP)
    assert(reward == 1)

def test_marine_should_reach_tophand_beacon_after_topright_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 66))
    _, reward = env.step(SC2Action.TOP_RIGHT)
    assert(reward == 1)

def test_marine_should_reach_tophand_beacon_after_topleft_step():
    env = SC2Env(world_width=128, world_height=128, norm_marine_pos=(64, 64), norm_beacon_pos=(64, 66))
    _, reward = env.step(SC2Action.TOP_LEFT)
    assert(reward == 1)
